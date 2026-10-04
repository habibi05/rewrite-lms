#!/usr/bin/env python3
"""
Generate an AI-friendly, read-only MySQL schema snapshot as Markdown.

The generator queries INFORMATION_SCHEMA only. It does not create, alter,
insert, update, or delete any database object or data.

Dependency:
    pip install mysql-connector-python
    pip install python-dotenv

Authentication:
    Prefer a MySQL client option file (for example ~/.my.cnf) or another
    environment-specific credential mechanism. This script intentionally
    does not write or store database credentials.

Environment:
    The script loads tools/.env when present. Existing environment variables
    are intentionally overridden by that file so the local generator config
    is deterministic.

    MYSQL_HOST       default: 127.0.0.1
    MYSQL_PORT       default: 3306
    MYSQL_DATABASE   required
    MYSQL_USER       optional
    MYSQL_CONFIG     optional path to a MySQL option file

Usage:
    python tools/generate-legacy-schema.py
    python tools/generate-legacy-schema.py --output analysis/legacy-schema-snapshot.md
    python tools/generate-legacy-schema.py --database legacy_lms
"""

from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import mysql.connector
    from mysql.connector import Error
except ImportError:
    print(
        "Missing dependency: mysql-connector-python. "
        "Install it with: pip install mysql-connector-python",
        file=sys.stderr,
    )
    raise SystemExit(1)

try:
    from dotenv import load_dotenv
except ImportError:
    print(
        "Missing dependency: python-dotenv. "
        "Install it with: pip install python-dotenv",
        file=sys.stderr,
    )
    raise SystemExit(1)


DEFAULT_OUTPUT = "analysis/legacy-schema-snapshot.md"
ENV_FILE = Path(__file__).resolve().parent / ".env"


def get_env(name: str, default: str | None = None, required: bool = False) -> str:
    value = os.getenv(name, default)
    if required and not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value or ""


def md_cell(value: Any) -> str:
    if value is None:
        return "—"
    return str(value).replace("|", "\|").replace("\n", " ")


def fetch_all(cursor, sql: str, params: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
    cursor.execute(sql, params)
    return list(cursor.fetchall())


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a read-only MySQL schema snapshot in Markdown."
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help=f"Output Markdown path (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument("--database", default=None, help="Override MYSQL_DATABASE.")
    args = parser.parse_args()

    load_dotenv(ENV_FILE, override=True)

    host = get_env("MYSQL_HOST", "127.0.0.1")
    port = int(get_env("MYSQL_PORT", "3306"))
    database = args.database or get_env("MYSQL_DATABASE", required=True)
    user = get_env("MYSQL_USER", "")
    config_file = get_env("MYSQL_CONFIG", "")

    connection_args: dict[str, Any] = {
        "host": host,
        "port": port,
        "database": database,
    }
    if user:
        connection_args["user"] = user
    if config_file:
        connection_args["option_files"] = [config_file]

    try:
        connection = mysql.connector.connect(**connection_args)
    except Error as exc:
        print(
            "Database connection failed. Configure authentication through "
            "your MySQL client configuration/environment.",
            file=sys.stderr,
        )
        print(f"Connector error: {exc}", file=sys.stderr)
        return 1

    try:
        cursor = connection.cursor(dictionary=True)

        tables = fetch_all(
            cursor,
            """
            SELECT TABLE_NAME, TABLE_TYPE, ENGINE, TABLE_COLLATION, TABLE_COMMENT
            FROM INFORMATION_SCHEMA.TABLES
            WHERE TABLE_SCHEMA = %s
              AND TABLE_TYPE IN ('BASE TABLE', 'VIEW')
            ORDER BY TABLE_NAME
            """,
            (database,),
        )

        columns = fetch_all(
            cursor,
            """
            SELECT
                TABLE_NAME,
                COLUMN_NAME,
                ORDINAL_POSITION,
                COLUMN_DEFAULT,
                IS_NULLABLE,
                COLUMN_TYPE,
                EXTRA,
                COLUMN_COMMENT
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = %s
            ORDER BY TABLE_NAME, ORDINAL_POSITION
            """,
            (database,),
        )

        constraints = fetch_all(
            cursor,
            """
            SELECT TABLE_NAME, CONSTRAINT_NAME, CONSTRAINT_TYPE
            FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
            WHERE CONSTRAINT_SCHEMA = %s
            ORDER BY TABLE_NAME, CONSTRAINT_NAME
            """,
            (database,),
        )

        key_columns = fetch_all(
            cursor,
            """
            SELECT
                TABLE_NAME,
                CONSTRAINT_NAME,
                COLUMN_NAME,
                ORDINAL_POSITION,
                REFERENCED_TABLE_NAME,
                REFERENCED_COLUMN_NAME
            FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
            WHERE CONSTRAINT_SCHEMA = %s
            ORDER BY TABLE_NAME, CONSTRAINT_NAME, ORDINAL_POSITION
            """,
            (database,),
        )

        indexes = fetch_all(
            cursor,
            """
            SELECT
                TABLE_NAME,
                INDEX_NAME,
                NON_UNIQUE,
                SEQ_IN_INDEX,
                COLUMN_NAME,
                INDEX_TYPE
            FROM INFORMATION_SCHEMA.STATISTICS
            WHERE TABLE_SCHEMA = %s
            ORDER BY TABLE_NAME, INDEX_NAME, SEQ_IN_INDEX
            """,
            (database,),
        )
    finally:
        cursor.close()
        connection.close()

    columns_by_table: dict[str, list[dict[str, Any]]] = {}
    for row in columns:
        columns_by_table.setdefault(row["TABLE_NAME"], []).append(row)

    constraints_by_table: dict[str, list[dict[str, Any]]] = {}
    for row in constraints:
        constraints_by_table.setdefault(row["TABLE_NAME"], []).append(row)

    key_columns_by_constraint: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for row in key_columns:
        key_columns_by_constraint.setdefault(
            (row["TABLE_NAME"], row["CONSTRAINT_NAME"]), []
        ).append(row)

    indexes_by_table: dict[str, list[dict[str, Any]]] = {}
    for row in indexes:
        indexes_by_table.setdefault(row["TABLE_NAME"], []).append(row)

    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    lines: list[str] = [
        "# Legacy Schema Snapshot",
        "",
        "> **Purpose:** machine-generated snapshot of the observed MySQL schema.",
        "> This document represents database structure only. It does not define",
        "> desired new-system behavior, business policy, migration requirements,",
        "> or implementation decisions.",
        "",
        "## Snapshot Metadata",
        "",
        "| Field | Value |",
        "|---|---|",
        "| Source | Live MySQL INFORMATION_SCHEMA |",
        f"| Database | {database} |",
        f"| Generated at (UTC) | {generated_at} |",
        "| Generator | generate-legacy-schema.py |",
        f"| Tables / Views | {len(tables)} |",
        "",
        "## Tables and Views",
        "",
    ]

    for table in tables:
        name = table["TABLE_NAME"]
        kind = "Table" if table["TABLE_TYPE"] == "BASE TABLE" else "View"

        lines += [
            f"## {kind}: {name}",
            "",
            "| Property | Value |",
            "|---|---|",
            f"| Type | {md_cell(table['TABLE_TYPE'])} |",
            f"| Engine | {md_cell(table['ENGINE'])} |",
            f"| Collation | {md_cell(table['TABLE_COLLATION'])} |",
            f"| Comment | {md_cell(table['TABLE_COMMENT'])} |",
            "",
            "### Columns",
            "",
            "| # | Column | Type | Nullable | Default | Extra | Comment |",
            "|---:|---|---|---|---|---|---|",
        ]

        for column in columns_by_table.get(name, []):
            lines.append(
                "| "
                + " | ".join(
                    [
                        md_cell(column["ORDINAL_POSITION"]),
                        md_cell(column["COLUMN_NAME"]),
                        md_cell(column["COLUMN_TYPE"]),
                        md_cell(column["IS_NULLABLE"]),
                        md_cell(column["COLUMN_DEFAULT"]),
                        md_cell(column["EXTRA"]),
                        md_cell(column["COLUMN_COMMENT"]),
                    ]
                )
                + " |"
            )

        if not columns_by_table.get(name):
            lines.append("| — | No column metadata returned. | — | — | — | — | — |")

        lines += ["", "### Constraints", ""]
        table_constraints = constraints_by_table.get(name, [])

        if table_constraints:
            for constraint in table_constraints:
                constraint_name = constraint["CONSTRAINT_NAME"]
                constraint_type = constraint["CONSTRAINT_TYPE"]
                parts = key_columns_by_constraint.get((name, constraint_name), [])
                local_columns = ", ".join(
                    md_cell(part["COLUMN_NAME"]) for part in parts
                )

                if constraint_type == "FOREIGN KEY":
                    refs = ", ".join(
                        f"{part['REFERENCED_TABLE_NAME']}."
                        f"{part['REFERENCED_COLUMN_NAME']}"
                        for part in parts
                        if part["REFERENCED_TABLE_NAME"]
                    )
                    description = (
                        f"{constraint_type} {constraint_name}: "
                        f"{local_columns} -> {refs or '—'}"
                    )
                else:
                    description = (
                        f"{constraint_type} {constraint_name}: "
                        f"{local_columns or '—'}"
                    )
                lines.append(f"- {description}")
        else:
            lines.append("_No table constraints returned._")

        lines += ["", "### Indexes", ""]
        table_indexes = indexes_by_table.get(name, [])

        if table_indexes:
            grouped: dict[str, list[dict[str, Any]]] = {}
            for index in table_indexes:
                grouped.setdefault(index["INDEX_NAME"], []).append(index)

            for index_name, entries in grouped.items():
                first = entries[0]
                columns_text = ", ".join(
                    md_cell(entry["COLUMN_NAME"]) for entry in entries
                )
                uniqueness = "UNIQUE" if first["NON_UNIQUE"] == 0 else "NON-UNIQUE"
                lines.append(
                    f"- {index_name} — {uniqueness}; "
                    f"type: {first['INDEX_TYPE']}; columns: {columns_text}"
                )
        else:
            lines.append("_No indexes returned._")

        lines += ["", "### Relationships", ""]
        foreign_keys = [
            c for c in table_constraints if c["CONSTRAINT_TYPE"] == "FOREIGN KEY"
        ]

        if foreign_keys:
            for constraint in foreign_keys:
                parts = key_columns_by_constraint.get(
                    (name, constraint["CONSTRAINT_NAME"]), []
                )
                for part in parts:
                    if part["REFERENCED_TABLE_NAME"]:
                        lines.append(
                            f"- {name}.{part['COLUMN_NAME']} -> "
                            f"{part['REFERENCED_TABLE_NAME']}."
                            f"{part['REFERENCED_COLUMN_NAME']}"
                        )
        else:
            lines.append("_No foreign-key relationships returned._")

        lines += ["", "---", ""]

    if not tables:
        lines += ["_No tables or views were found._", ""]

    lines += [
        "## Interpretation Boundary",
        "",
        "The generator intentionally does not infer:",
        "",
        "- business meaning of tables or columns;",
        "- whether a legacy table or column belongs in the new system;",
        "- whether legacy data must be migrated;",
        "- desired business rules or lifecycle policy;",
        "- application behavior not represented by database metadata;",
        "- technical implementation choices for the new system.",
        "",
        "Use this snapshot as legacy database evidence. The Database Architect",
        "must reconcile it with approved requirements, business rules, PRDs,",
        "human decisions, and other authoritative project artifacts before",
        "designing the new database.",
        "",
    ]

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")

    print(f"Generated: {output}")
    print(f"Database: {database}")
    print(f"Tables / Views: {len(tables)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
