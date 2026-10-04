# Legacy Schema Snapshot

> **Purpose:** machine-generated snapshot of the observed MySQL schema.
> This document represents database structure only. It does not define
> desired new-system behavior, business policy, migration requirements,
> or implementation decisions.

## Snapshot Metadata

| Field | Value |
|---|---|
| Source | Live MySQL INFORMATION_SCHEMA |
| Database | project_insmart |
| Generated at (UTC) | 2026-10-04T11:37:25+00:00 |
| Generator | generate-legacy-schema.py |
| Tables / Views | 175 |

## Tables and Views

## Table: abouts

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | one_enable | int | NO | — |  |  |
| 3 | one_heading | varchar(191) | NO | — |  |  |
| 4 | one_image | varchar(191) | NO | — |  |  |
| 5 | one_text | text | NO | — |  |  |
| 6 | two_enable | int | NO | — |  |  |
| 7 | two_heading | varchar(191) | NO | — |  |  |
| 8 | two_text | text | NO | — |  |  |
| 9 | two_imageone | varchar(191) | NO | — |  |  |
| 10 | two_imagetwo | varchar(191) | NO | — |  |  |
| 11 | two_imagethree | varchar(191) | NO | — |  |  |
| 12 | two_imagefour | varchar(191) | NO | — |  |  |
| 13 | two_txtone | varchar(191) | NO | — |  |  |
| 14 | two_txttwo | varchar(191) | NO | — |  |  |
| 15 | two_txtthree | varchar(191) | NO | — |  |  |
| 16 | two_txtfour | varchar(191) | NO | — |  |  |
| 17 | two_imagetext | text | NO | — |  |  |
| 18 | three_enable | int | NO | — |  |  |
| 19 | three_heading | varchar(191) | NO | — |  |  |
| 20 | three_text | text | NO | — |  |  |
| 21 | three_countone | varchar(191) | NO | — |  |  |
| 22 | three_counttwo | varchar(191) | NO | — |  |  |
| 23 | three_countthree | varchar(191) | NO | — |  |  |
| 24 | three_countfour | varchar(191) | NO | — |  |  |
| 25 | three_countfive | varchar(191) | NO | — |  |  |
| 26 | three_countsix | varchar(191) | NO | — |  |  |
| 27 | three_txtone | varchar(191) | NO | — |  |  |
| 28 | three_txttwo | varchar(191) | NO | — |  |  |
| 29 | three_txtthree | varchar(191) | NO | — |  |  |
| 30 | three_txtfour | varchar(191) | NO | — |  |  |
| 31 | three_txtfive | varchar(191) | NO | — |  |  |
| 32 | three_txtsix | varchar(191) | NO | — |  |  |
| 33 | four_enable | int | NO | — |  |  |
| 34 | four_heading | varchar(191) | NO | — |  |  |
| 35 | four_text | text | NO | — |  |  |
| 36 | four_btntext | varchar(191) | NO | — |  |  |
| 37 | four_imageone | varchar(191) | NO | — |  |  |
| 38 | four_imagetwo | varchar(191) | NO | — |  |  |
| 39 | four_txtone | varchar(191) | NO | — |  |  |
| 40 | four_txttwo | varchar(191) | NO | — |  |  |
| 41 | four_icon | varchar(191) | NO | — |  |  |
| 42 | five_enable | int | NO | — |  |  |
| 43 | five_heading | varchar(191) | NO | — |  |  |
| 44 | five_text | text | NO | — |  |  |
| 45 | five_btntext | varchar(191) | NO | — |  |  |
| 46 | five_imageone | varchar(191) | NO | — |  |  |
| 47 | five_imagetwo | varchar(191) | NO | — |  |  |
| 48 | five_imagethree | varchar(191) | NO | — |  |  |
| 49 | six_enable | int | NO | — |  |  |
| 50 | six_heading | varchar(191) | NO | — |  |  |
| 51 | six_txtone | varchar(191) | NO | — |  |  |
| 52 | six_txttwo | varchar(191) | NO | — |  |  |
| 53 | six_txtthree | varchar(191) | NO | — |  |  |
| 54 | six_deatilone | text | NO | — |  |  |
| 55 | six_deatiltwo | text | NO | — |  |  |
| 56 | six_deatilthree | text | NO | — |  |  |
| 57 | text_one | longtext | YES | — |  |  |
| 58 | text_two | longtext | YES | — |  |  |
| 59 | text_three | longtext | YES | — |  |  |
| 60 | link_one | varchar(191) | YES | — |  |  |
| 61 | link_two | varchar(191) | YES | — |  |  |
| 62 | link_three | varchar(191) | YES | — |  |  |
| 63 | link_four | varchar(191) | YES | — |  |  |
| 64 | created_at | timestamp | YES | — |  |  |
| 65 | updated_at | timestamp | YES | — |  |  |
| 66 | linkedin | varchar(191) | YES | — |  |  |
| 67 | twitter | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: acedemics

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | course | varchar(191) | NO | — |  |  |
| 4 | school | varchar(191) | YES | — |  |  |
| 5 | marks | int | YES | — |  |  |
| 6 | yearofpassing | varchar(191) | YES | — |  |  |
| 7 | created_at | timestamp | YES | — |  |  |
| 8 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: activity_log

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | log_name | varchar(191) | YES | — |  |  |
| 3 | description | text | NO | — |  |  |
| 4 | subject_type | varchar(191) | YES | — |  |  |
| 5 | subject_id | bigint unsigned | YES | — |  |  |
| 6 | causer_type | varchar(191) | YES | — |  |  |
| 7 | causer_id | bigint unsigned | YES | — |  |  |
| 8 | properties | text | YES | — |  |  |
| 9 | created_at | timestamp | YES | — |  |  |
| 10 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- activity_log_log_name_index — NON-UNIQUE; type: BTREE; columns: log_name
- causer — NON-UNIQUE; type: BTREE; columns: causer_type, causer_id
- PRIMARY — UNIQUE; type: BTREE; columns: id
- subject — NON-UNIQUE; type: BTREE; columns: subject_type, subject_id

### Relationships

_No foreign-key relationships returned._

---

## Table: admin_supports

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int unsigned | NO | — |  |  |
| 3 | category | text | YES | — |  |  |
| 4 | priority | text | YES | — |  |  |
| 5 | subject | text | YES | — |  |  |
| 6 | message | text | YES | — |  |  |
| 7 | ticket_id | text | YES | — |  |  |
| 8 | status | tinyint(1) | NO | 0 |  |  |
| 9 | image | varchar(191) | YES | — |  |  |
| 10 | reply | varchar(191) | YES | — |  |  |
| 11 | reply_to | varchar(191) | YES | — |  |  |
| 12 | created_at | timestamp | YES | — |  |  |
| 13 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: admincustomisations

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | created_at | timestamp | YES | — |  |  |
| 3 | updated_at | timestamp | YES | — |  |  |
| 4 | bg_grey_color | varchar(191) | YES | — |  |  |
| 5 | bg_white_color | varchar(191) | YES | — |  |  |
| 6 | text-grey-color | varchar(191) | YES | — |  |  |
| 7 | text_dark_color | varchar(191) | YES | — |  |  |
| 8 | text_white_color | varchar(191) | YES | — |  |  |
| 9 | text_blue_color | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: ads

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | ad_type | varchar(191) | NO | — |  |  |
| 3 | ad_image | varchar(191) | NO | — |  |  |
| 4 | ad_video | varchar(191) | NO | — |  |  |
| 5 | ad_url | varchar(191) | YES | — |  |  |
| 6 | ad_location | varchar(191) | NO | — |  |  |
| 7 | ad_target | varchar(191) | YES | — |  |  |
| 8 | ad_hold | varchar(191) | YES | — |  |  |
| 9 | time | varchar(191) | YES | — |  |  |
| 10 | endtime | varchar(191) | YES | — |  |  |
| 11 | created_at | timestamp | YES | — |  |  |
| 12 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: adsenses

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | code | longtext | NO | — |  |  |
| 3 | status | tinyint(1) | NO | 0 |  |  |
| 4 | ishome | tinyint(1) | NO | 0 |  |  |
| 5 | iscart | tinyint(1) | NO | 0 |  |  |
| 6 | isdetail | tinyint(1) | NO | 0 |  |  |
| 7 | iswishlist | tinyint(1) | NO | 0 |  |  |
| 8 | isviewall | tinyint(1) | NO | 0 |  |  |
| 9 | created_at | timestamp | YES | — |  |  |
| 10 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: advertisements

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | image1 | varchar(191) | YES | — |  |  |
| 3 | image2 | varchar(191) | YES | — |  |  |
| 4 | link_by1 | varchar(191) | YES | — |  |  |
| 5 | link_by2 | varchar(191) | YES | — |  |  |
| 6 | course_id1 | int | YES | — |  |  |
| 7 | course_id2 | int | YES | — |  |  |
| 8 | url1 | text | YES | — |  |  |
| 9 | url2 | text | YES | — |  |  |
| 10 | type | varchar(191) | YES | — |  |  |
| 11 | status | tinyint(1) | NO | 0 |  |  |
| 12 | position | varchar(191) | YES | — |  |  |
| 13 | created_at | timestamp | YES | — |  |  |
| 14 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: affiliate

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | ref_length | varchar(191) | YES | — |  |  |
| 3 | point_per_referral | varchar(191) | YES | — |  |  |
| 4 | points_to_reffered | varchar(191) | YES | — |  |  |
| 5 | image | varchar(191) | YES | — |  |  |
| 6 | text | longtext | YES | — |  |  |
| 7 | status | int unsigned | NO | 0 |  |  |
| 8 | created_at | timestamp | YES | — |  |  |
| 9 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: allcities

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int | NO | — | auto_increment |  |
| 2 | name | varchar(30) | NO | — |  |  |
| 3 | state_id | int | NO | — |  |  |
| 4 | pincode | int | YES | — |  |  |
| 5 | updated_at | datetime | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: allcountry

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int | NO | — | auto_increment |  |
| 2 | iso | char(2) | NO | — |  |  |
| 3 | name | varchar(80) | NO | — |  |  |
| 4 | nicename | varchar(80) | NO | — |  |  |
| 5 | iso3 | char(3) | YES | — |  |  |
| 6 | numcode | smallint | YES | — |  |  |
| 7 | phonecode | int | NO | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: allstates

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int | NO | — | auto_increment |  |
| 2 | name | varchar(30) | NO | — |  |  |
| 3 | country_id | int | NO | 1 |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: aluminis

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | created_at | timestamp | YES | — |  |  |
| 3 | updated_at | timestamp | YES | — |  |  |
| 4 | status | tinyint(1) | NO | 0 |  |  |
| 5 | url | varchar(191) | YES | — |  |  |
| 6 | user_id | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: announcements

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | user_id | varchar(191) | NO | — |  |  |
| 3 | course_id | varchar(191) | NO | — |  |  |
| 4 | announsment | text | NO | — |  |  |
| 5 | status | enum('1','0') | YES | — |  |  |
| 6 | created_at | timestamp | YES | — |  |  |
| 7 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: answers

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | instructor_id | int | YES | — |  |  |
| 3 | ans_user_id | int | NO | — |  |  |
| 4 | ques_user_id | int | NO | — |  |  |
| 5 | course_id | int | NO | — |  |  |
| 6 | question_id | int | NO | — |  |  |
| 7 | answer | varchar(191) | NO | — |  |  |
| 8 | status | tinyint(1) | NO | — |  |  |
| 9 | created_at | timestamp | YES | — |  |  |
| 10 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: api_keys

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | secret_key | longtext | NO | — |  |  |
| 3 | user_id | int unsigned | NO | — |  |  |
| 4 | created_at | timestamp | YES | — |  |  |
| 5 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: applyjobs

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | job_id | int | NO | — |  |  |
| 4 | experiense | varchar(191) | NO | — |  |  |
| 5 | years | varchar(191) | NO | — |  |  |
| 6 | skills | varchar(191) | NO | — |  |  |
| 7 | pdf | varchar(191) | NO | — |  |  |
| 8 | created_at | timestamp | YES | — |  |  |
| 9 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: appointments

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | instructor_id | int | YES | — |  |  |
| 4 | course_id | int | NO | — |  |  |
| 5 | title | varchar(191) | YES | — |  |  |
| 6 | detail | text | YES | — |  |  |
| 7 | start_time | datetime | YES | — |  |  |
| 8 | request | varchar(191) | YES | — |  |  |
| 9 | accept | tinyint(1) | NO | 0 |  |  |
| 10 | files | varchar(191) | YES | — |  |  |
| 11 | reply | text | YES | — |  |  |
| 12 | created_at | timestamp | YES | — |  |  |
| 13 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: assignments

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | instructor_id | int | YES | — |  |  |
| 4 | course_id | int | NO | — |  |  |
| 5 | chapter_id | int | YES | — |  |  |
| 6 | title | varchar(191) | NO | — |  |  |
| 7 | detail | varchar(191) | YES | — |  |  |
| 8 | url | varchar(191) | YES | — |  |  |
| 9 | assignment | varchar(191) | YES | — |  |  |
| 10 | type | tinyint(1) | NO | 1 |  |  |
| 11 | rating | int | YES | — |  |  |
| 12 | created_at | timestamp | YES | — |  |  |
| 13 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: attandance

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | course_id | varchar(191) | YES | — |  |  |
| 4 | instructor_id | int | NO | — |  |  |
| 5 | order_id | varchar(191) | YES | — |  |  |
| 6 | date | date | YES | — |  |  |
| 7 | end_date | datetime | YES | — |  |  |
| 8 | status | tinyint(1) | NO | 1 |  |  |
| 9 | created_at | timestamp | YES | — |  |  |
| 10 | updated_at | timestamp | YES | — |  |  |
| 11 | zoom_id | int | YES | — |  |  |
| 12 | bbl_id | int | YES | — |  |  |
| 13 | googlemeet_id | int | YES | — |  |  |
| 14 | jitsi_id | int | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: authentication_log

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | authenticatable_type | varchar(191) | NO | — |  |  |
| 3 | authenticatable_id | bigint unsigned | NO | — |  |  |
| 4 | ip_address | varchar(45) | YES | — |  |  |
| 5 | platform | text | YES | — |  |  |
| 6 | browser | text | YES | — |  |  |
| 7 | login_at | timestamp | YES | — |  |  |
| 8 | logout_at | timestamp | YES | — |  |  |
| 9 | user_agent | int | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- auth_log_authenticatable_type_authenticatable_id_index — NON-UNIQUE; type: BTREE; columns: authenticatable_type, authenticatable_id
- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: bank_transfers

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | bank_name | varchar(191) | NO | — |  |  |
| 3 | ifcs_code | varchar(191) | YES | — |  |  |
| 4 | account_number | varchar(191) | NO | — |  |  |
| 5 | account_holder_name | varchar(191) | NO | — |  |  |
| 6 | swift_code | varchar(191) | YES | — |  |  |
| 7 | bank_enable | tinyint(1) | NO | 0 |  |  |
| 8 | created_at | timestamp | YES | — |  |  |
| 9 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: batch

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | varchar(191) | NO | — |  |  |
| 3 | title | varchar(191) | YES | — |  |  |
| 4 | detail | longtext | YES | — |  |  |
| 5 | price | double | YES | — |  |  |
| 6 | type | tinyint(1) | NO | 0 |  |  |
| 7 | slug | varchar(191) | YES | — |  |  |
| 8 | status | tinyint(1) | NO | 0 |  |  |
| 9 | featured | tinyint(1) | NO | 1 |  |  |
| 10 | preview_image | varchar(191) | YES | — |  |  |
| 11 | allowed_users | longtext | YES | — |  |  |
| 12 | allowed_courses | longtext | YES | — |  |  |
| 13 | allowed_bundles | longtext | YES | — |  |  |
| 14 | created_at | timestamp | YES | — |  |  |
| 15 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: bigbluemeetings

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | presen_name | varchar(191) | NO | — |  |  |
| 3 | instructor_id | int unsigned | NO | — |  |  |
| 4 | meetingid | varchar(191) | NO | — |  |  |
| 5 | detail | text | YES | — |  |  |
| 6 | start_time | varchar(200) | NO | — |  |  |
| 7 | meetingname | varchar(191) | NO | — |  |  |
| 8 | modpw | varchar(191) | YES | — |  |  |
| 9 | attendeepw | varchar(191) | NO | — |  |  |
| 10 | welcomemsg | varchar(191) | YES | — |  |  |
| 11 | duration | varchar(191) | NO | — |  |  |
| 12 | setMaxParticipants | varchar(191) | NO | -1 |  |  |
| 13 | setMuteOnStart | varchar(191) | NO | false |  |  |
| 14 | allow_record | tinyint(1) | NO | — |  |  |
| 15 | is_ended | int | NO | 0 |  |  |
| 16 | course_id | int | YES | — |  |  |
| 17 | link_by | varchar(191) | YES | — |  |  |
| 18 | created_at | timestamp | YES | — |  |  |
| 19 | updated_at | timestamp | YES | — |  |  |
| 20 | paid_meeting_toggle | tinyint(1) | NO | 0 |  |  |
| 21 | paid_meeting_price | varchar(255) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: blogs

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | date | date | NO | — |  |  |
| 4 | image | varchar(191) | NO | — |  |  |
| 5 | heading | varchar(191) | NO | — |  |  |
| 6 | detail | text | NO | — |  |  |
| 7 | text | varchar(191) | NO | — |  |  |
| 8 | approved | tinyint(1) | NO | — |  |  |
| 9 | status | tinyint(1) | NO | — |  |  |
| 10 | created_at | timestamp | YES | — |  |  |
| 11 | updated_at | timestamp | YES | — |  |  |
| 12 | slug | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: breadcums

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | created_at | timestamp | YES | — |  |  |
| 3 | updated_at | timestamp | YES | — |  |  |
| 4 | img | varchar(191) | NO | — |  |  |
| 5 | text | varchar(191) | NO | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: bundle_courses

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | varchar(191) | NO | — |  |  |
| 3 | course_id | varchar(191) | NO | — |  |  |
| 4 | title | varchar(191) | YES | — |  |  |
| 5 | detail | longtext | YES | — |  |  |
| 6 | price | int | YES | — |  |  |
| 7 | discount_price | int | YES | — |  |  |
| 8 | type | enum('1','0') | YES | — |  |  |
| 9 | slug | varchar(191) | YES | — |  |  |
| 10 | status | tinyint(1) | YES | — |  |  |
| 11 | featured | tinyint(1) | NO | 1 |  |  |
| 12 | preview_image | varchar(191) | YES | — |  |  |
| 13 | created_at | timestamp | YES | — |  |  |
| 14 | updated_at | timestamp | YES | — |  |  |
| 15 | billing_interval | enum('day','week','month','year') | YES | — |  |  |
| 16 | price_id | varchar(50) | YES | — |  |  |
| 17 | product_id | varchar(50) | YES | — |  |  |
| 18 | subscription_mode | varchar(50) | YES | stripe |  |  |
| 19 | is_subscription_enabled | tinyint(1) | NO | 0 |  |  |
| 20 | duration | int | YES | — |  |  |
| 21 | duration_type | varchar(191) | NO | m |  |  |
| 22 | short_detail | longtext | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: careers

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | one_enable | int | NO | — |  |  |
| 3 | one_heading | varchar(191) | YES | — |  |  |
| 4 | one_text | text | YES | — |  |  |
| 5 | one_btntxt | varchar(191) | YES | — |  |  |
| 6 | one_video | varchar(191) | YES | — |  |  |
| 7 | two_enable | int | NO | — |  |  |
| 8 | three_enable | int | NO | — |  |  |
| 9 | three_bg_image | varchar(191) | YES | — |  |  |
| 10 | three_video | varchar(191) | YES | — |  |  |
| 11 | three_heading | varchar(191) | YES | — |  |  |
| 12 | three_btntxt | varchar(191) | YES | — |  |  |
| 13 | four_enable | int | NO | — |  |  |
| 14 | four_img_one | varchar(191) | YES | — |  |  |
| 15 | four_img_two | varchar(191) | YES | — |  |  |
| 16 | four_img_three | varchar(191) | YES | — |  |  |
| 17 | four_img_four | varchar(191) | YES | — |  |  |
| 18 | four_img_five | varchar(191) | YES | — |  |  |
| 19 | four_img_six | varchar(191) | YES | — |  |  |
| 20 | four_img_seven | varchar(191) | YES | — |  |  |
| 21 | four_img_eight | varchar(191) | YES | — |  |  |
| 22 | four_img_nine | varchar(191) | YES | — |  |  |
| 23 | five_enable | int | NO | — |  |  |
| 24 | five_heading | varchar(191) | YES | — |  |  |
| 25 | five_text | text | YES | — |  |  |
| 26 | five_icon | varchar(191) | YES | — |  |  |
| 27 | five_detail | varchar(191) | YES | — |  |  |
| 28 | five_textone | varchar(191) | YES | — |  |  |
| 29 | five_texttwo | varchar(191) | YES | — |  |  |
| 30 | five_textthree | varchar(191) | YES | — |  |  |
| 31 | five_textfour | varchar(191) | YES | — |  |  |
| 32 | five_textfive | varchar(191) | YES | — |  |  |
| 33 | five_textsix | varchar(191) | YES | — |  |  |
| 34 | five_textseven | varchar(191) | YES | — |  |  |
| 35 | five_texteight | varchar(191) | YES | — |  |  |
| 36 | five_textnine | varchar(191) | YES | — |  |  |
| 37 | five_textten | varchar(191) | YES | — |  |  |
| 38 | five_dtlone | text | YES | — |  |  |
| 39 | five_dtltwo | text | YES | — |  |  |
| 40 | five_dtlthree | text | YES | — |  |  |
| 41 | five_dtlfour | text | YES | — |  |  |
| 42 | five_dtlfive | text | YES | — |  |  |
| 43 | five_dtlsix | text | YES | — |  |  |
| 44 | five_dtlseven | text | YES | — |  |  |
| 45 | five_dtleight | text | YES | — |  |  |
| 46 | five_dtlnine | text | YES | — |  |  |
| 47 | five_dtlten | text | YES | — |  |  |
| 48 | six_enable | int | NO | — |  |  |
| 49 | six_heading | varchar(191) | YES | — |  |  |
| 50 | six_text | varchar(191) | YES | — |  |  |
| 51 | six_topic_one | varchar(191) | YES | — |  |  |
| 52 | six_topic_two | varchar(191) | YES | — |  |  |
| 53 | six_topic_three | varchar(191) | YES | — |  |  |
| 54 | six_topic_four | varchar(191) | YES | — |  |  |
| 55 | six_topic_five | varchar(191) | YES | — |  |  |
| 56 | six_topic_six | varchar(191) | YES | — |  |  |
| 57 | created_at | timestamp | YES | — |  |  |
| 58 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: carts

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | course_id | int | YES | — |  |  |
| 4 | category_id | int | YES | — |  |  |
| 5 | price | varchar(191) | YES | — |  |  |
| 6 | offer_price | varchar(191) | YES | — |  |  |
| 7 | disamount | varchar(191) | YES | — |  |  |
| 8 | distype | varchar(191) | YES | — |  |  |
| 9 | bundle_id | int | YES | — |  |  |
| 10 | type | tinyint(1) | NO | 0 |  |  |
| 11 | created_at | timestamp | YES | — |  |  |
| 12 | updated_at | timestamp | YES | — |  |  |
| 13 | coupon_id | varchar(50) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: categories

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | title | varchar(191) | YES | — |  |  |
| 3 | icon | varchar(191) | YES | — |  |  |
| 4 | slug | varchar(191) | YES | — |  |  |
| 5 | featured | enum('1','0') | NO | — |  |  |
| 6 | status | enum('1','0') | NO | — |  |  |
| 7 | position | int | YES | — |  |  |
| 8 | created_at | timestamp | YES | — |  |  |
| 9 | updated_at | timestamp | YES | — |  |  |
| 10 | cat_image | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: category_blogs

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | category_id | varchar(191) | NO | — |  |  |
| 3 | category_to_show | varchar(191) | NO | — |  |  |
| 4 | created_at | timestamp | YES | — |  |  |
| 5 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: category_sliders

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | category_id | varchar(191) | NO | — |  |  |
| 3 | category_to_show | varchar(191) | NO | — |  |  |
| 4 | created_at | timestamp | YES | — |  |  |
| 5 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: certificate_design

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | background_image | varchar(191) | YES | — |  |  |
| 3 | background_image_enable | varchar(191) | YES | — |  |  |
| 4 | background_color | varchar(191) | YES | — |  |  |
| 5 | logo_image | varchar(191) | YES | — |  |  |
| 6 | logo_enable | varchar(191) | YES | — |  |  |
| 7 | logo_position | varchar(191) | NO | center |  |  |
| 8 | logo_width | int | NO | 150 |  |  |
| 9 | logo_height | int | NO | 100 |  |  |
| 10 | border_one | varchar(191) | NO | 15 |  |  |
| 11 | border_one_color | varchar(191) | YES | — |  |  |
| 12 | border_one_enable | varchar(191) | YES | — |  |  |
| 13 | border_two | varchar(191) | NO | 15 |  |  |
| 14 | border_two_color | varchar(191) | YES | — |  |  |
| 15 | border_two_enable | varchar(191) | YES | — |  |  |
| 16 | width | varchar(191) | YES | — |  |  |
| 17 | height | varchar(191) | YES | — |  |  |
| 18 | title | varchar(191) | YES | — |  |  |
| 19 | title_position | varchar(191) | NO | center |  |  |
| 20 | title_font_size | int | NO | 30 |  |  |
| 21 | title_font_color | varchar(191) | YES | — |  |  |
| 22 | body | text | YES | — |  |  |
| 23 | body_position | varchar(191) | NO | center |  |  |
| 24 | body_font_size | int | NO | 10 |  |  |
| 25 | body_font_color | varchar(191) | YES | — |  |  |
| 26 | body_max_len | varchar(191) | YES | — |  |  |
| 27 | date_enable | tinyint | NO | 1 |  |  |
| 28 | date_position | varchar(191) | NO | center |  |  |
| 29 | date_font_size | int | NO | 30 |  |  |
| 30 | date_font_color | varchar(191) | YES | — |  |  |
| 31 | date_format | int | NO | 1 |  |  |
| 32 | signature_image | varchar(191) | YES | — |  |  |
| 33 | signature_position | varchar(191) | NO | center |  |  |
| 34 | signature_height | int | NO | 100 |  |  |
| 35 | signature_width | int | NO | 150 |  |  |
| 36 | name | varchar(191) | YES | — |  |  |
| 37 | name_position | varchar(191) | NO | center |  |  |
| 38 | name_font_size | int | NO | 50 |  |  |
| 39 | name_font_color | varchar(191) | YES | — |  |  |
| 40 | for_course | tinyint | NO | 0 |  |  |
| 41 | for_quiz | tinyint | NO | 0 |  |  |
| 42 | default | tinyint | NO | 0 |  |  |
| 43 | created_at | timestamp | YES | — |  |  |
| 44 | updated_at | timestamp | YES | — |  |  |
| 45 | percentage | varchar(255) | NO | 00 |  |  |
| 46 | widget1_enable | varchar(255) | YES | — |  |  |
| 47 | widget2_enable | varchar(255) | YES | — |  |  |
| 48 | widget3_enable | varchar(255) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: chats

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | conv_id | bigint unsigned | NO | — |  |  |
| 3 | user_id | bigint unsigned | NO | — |  |  |
| 4 | message | longtext | YES | — |  |  |
| 5 | type | varchar(100) | NO | text |  |  |
| 6 | media | varchar(191) | YES | — |  |  |
| 7 | status | enum('Not Seen','Seen') | NO | — |  |  |
| 8 | created_at | timestamp | YES | — |  |  |
| 9 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: child_categories

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | category_id | int | YES | — |  |  |
| 3 | subcategory_id | varchar(191) | NO | — |  |  |
| 4 | title | varchar(191) | YES | — |  |  |
| 5 | icon | varchar(191) | YES | — |  |  |
| 6 | slug | varchar(191) | YES | — |  |  |
| 7 | status | enum('1','0') | NO | — |  |  |
| 8 | created_at | timestamp | YES | — |  |  |
| 9 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: cities

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | name | varchar(30) | NO | — |  |  |
| 3 | country_id | int | NO | — |  |  |
| 4 | state_id | int | NO | — |  |  |
| 5 | pincode | int | YES | — |  |  |
| 6 | created_at | timestamp | YES | — |  |  |
| 7 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: color_options

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | blue_bg | varchar(191) | YES | — |  |  |
| 3 | red_bg | varchar(191) | YES | — |  |  |
| 4 | grey_bg | varchar(191) | YES | — |  |  |
| 5 | light_grey_bg | varchar(191) | YES | — |  |  |
| 6 | black_bg | varchar(191) | YES | — |  |  |
| 7 | white_bg | varchar(191) | YES | — |  |  |
| 8 | dark_red_bg | varchar(191) | YES | — |  |  |
| 9 | black_text | varchar(191) | YES | — |  |  |
| 10 | light_grey_text | varchar(191) | YES | — |  |  |
| 11 | dark_grey_text | varchar(191) | YES | — |  |  |
| 12 | red_text | varchar(191) | YES | — |  |  |
| 13 | blue_text | varchar(191) | YES | — |  |  |
| 14 | dark_blue_text | varchar(191) | YES | — |  |  |
| 15 | white_text | varchar(191) | YES | — |  |  |
| 16 | linear_bg_one | varchar(191) | YES | — |  |  |
| 17 | linear_bg_two | varchar(191) | YES | — |  |  |
| 18 | linear_reverse_bg_one | varchar(191) | YES | — |  |  |
| 19 | linear_reverse_bg_two | varchar(191) | YES | — |  |  |
| 20 | linear_about_bg_one | varchar(191) | YES | — |  |  |
| 21 | linear_about_bg_two | varchar(191) | YES | — |  |  |
| 22 | linear_about_bluebg_one | varchar(191) | YES | — |  |  |
| 23 | linear_about_bluebg_two | varchar(191) | YES | — |  |  |
| 24 | linear_career_bg_one | varchar(191) | YES | — |  |  |
| 25 | linear_career_bg_two | varchar(191) | YES | — |  |  |
| 26 | created_at | timestamp | YES | — |  |  |
| 27 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: coming_soons

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | bg_image | varchar(191) | NO | — |  |  |
| 3 | heading | varchar(191) | NO | — |  |  |
| 4 | count_one | varchar(191) | NO | — |  |  |
| 5 | count_two | varchar(191) | NO | — |  |  |
| 6 | count_three | varchar(191) | NO | — |  |  |
| 7 | count_four | varchar(191) | NO | — |  |  |
| 8 | text_one | varchar(191) | NO | — |  |  |
| 9 | text_two | varchar(191) | NO | — |  |  |
| 10 | text_three | varchar(191) | NO | — |  |  |
| 11 | text_four | varchar(191) | NO | — |  |  |
| 12 | btn_text | varchar(191) | NO | — |  |  |
| 13 | created_at | timestamp | YES | — |  |  |
| 14 | updated_at | timestamp | YES | — |  |  |
| 15 | allowed_ip | longtext | YES | — |  |  |
| 16 | enable | int | NO | 0 |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: compares

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | varchar(191) | NO | — |  |  |
| 3 | course_id | varchar(191) | NO | — |  |  |
| 4 | created_at | timestamp | YES | — |  |  |
| 5 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: completed_payouts

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | payer_id | int | NO | — |  |  |
| 4 | pay_total | int | NO | — |  |  |
| 5 | order_id | varchar(191) | NO | — |  |  |
| 6 | payment_method | varchar(191) | YES | — |  |  |
| 7 | currency | varchar(191) | NO | — |  |  |
| 8 | currency_icon | varchar(191) | NO | — |  |  |
| 9 | pay_status | tinyint(1) | NO | 0 |  |  |
| 10 | created_at | timestamp | YES | — |  |  |
| 11 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: contactreasons

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | reason | varchar(191) | NO | — |  |  |
| 3 | status | tinyint(1) | NO | — |  |  |
| 4 | created_at | timestamp | YES | — |  |  |
| 5 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: contacts

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | fname | varchar(191) | NO | — |  |  |
| 4 | lname | varchar(191) | NO | — |  |  |
| 5 | email | varchar(191) | NO | — |  |  |
| 6 | mobile | varchar(191) | NO | — |  |  |
| 7 | message | longtext | NO | — |  |  |
| 8 | created_at | timestamp | YES | — |  |  |
| 9 | updated_at | timestamp | YES | — |  |  |
| 10 | contacts | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: conversations

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | conv_id | char(36) | NO | — |  |  |
| 3 | receiver_id | bigint unsigned | NO | — |  |  |
| 4 | sender_id | bigint unsigned | NO | — |  |  |
| 5 | created_at | timestamp | YES | — |  |  |
| 6 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: countries

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | country_id | int | YES | — |  |  |
| 3 | iso | char(2) | NO | — |  |  |
| 4 | name | varchar(80) | NO | — |  |  |
| 5 | nicename | varchar(80) | NO | — |  |  |
| 6 | iso3 | char(3) | YES | — |  |  |
| 7 | numcode | smallint | YES | — |  |  |
| 8 | created_at | timestamp | YES | — |  |  |
| 9 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: coupons

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | code | varchar(191) | NO | — |  |  |
| 3 | distype | varchar(100) | NO | — |  |  |
| 4 | amount | varchar(191) | NO | — |  |  |
| 5 | link_by | varchar(100) | NO | — |  |  |
| 6 | course_id | int unsigned | YES | — |  |  |
| 7 | category_id | int | YES | — |  |  |
| 8 | maxusage | int unsigned | YES | — |  |  |
| 9 | minamount | double | YES | — |  |  |
| 10 | expirydate | datetime | NO | — |  |  |
| 11 | created_at | timestamp | YES | — |  |  |
| 12 | updated_at | timestamp | YES | — |  |  |
| 13 | bundle_id | varchar(50) | YES | — |  |  |
| 14 | stripe_coupon_id | varchar(50) | YES | — |  |  |
| 15 | show_to_users | tinyint(1) | NO | 1 |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: course_backups

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | course_id | varchar(191) | NO | — |  |  |
| 3 | user_id | varchar(191) | NO | — |  |  |
| 4 | category_id | varchar(191) | NO | — |  |  |
| 5 | subcategory_id | varchar(191) | NO | — |  |  |
| 6 | childcategory_id | varchar(191) | NO | — |  |  |
| 7 | language_id | varchar(191) | NO | — |  |  |
| 8 | title | varchar(191) | YES | — |  |  |
| 9 | short_detail | text | YES | — |  |  |
| 10 | detail | text | YES | — |  |  |
| 11 | requirement | text | YES | — |  |  |
| 12 | price | varchar(191) | YES | — |  |  |
| 13 | discount_price | varchar(191) | YES | — |  |  |
| 14 | day | varchar(191) | YES | — |  |  |
| 15 | video | varchar(191) | YES | — |  |  |
| 16 | url | varchar(191) | YES | — |  |  |
| 17 | featured | enum('1','0') | YES | — |  |  |
| 18 | slug | varchar(191) | YES | — |  |  |
| 19 | status | enum('1','0') | YES | — |  |  |
| 20 | preview_image | varchar(191) | YES | — |  |  |
| 21 | video_url | varchar(191) | YES | — |  |  |
| 22 | preview_type | varchar(191) | YES | — |  |  |
| 23 | type | enum('1','0') | YES | — |  |  |
| 24 | duration | int | YES | — |  |  |
| 25 | duration_type | varchar(191) | YES | — |  |  |
| 26 | assignment_enable | int | NO | 1 |  |  |
| 27 | appointment_enable | int | NO | 1 |  |  |
| 28 | certificate_enable | int | NO | 1 |  |  |
| 29 | course_tags | text | YES | — |  |  |
| 30 | reject_txt | text | YES | — |  |  |
| 31 | drip_enable | int | NO | 1 |  |  |
| 32 | institude_id | int | NO | 1 |  |  |
| 33 | involvement_request | int | NO | 1 |  |  |
| 34 | country | varchar(191) | YES | — |  |  |
| 35 | other_cats | varchar(191) | YES | — |  |  |
| 36 | refund_policy_id | varchar(255) | YES | — |  |  |
| 37 | created_at | timestamp | YES | — |  |  |
| 38 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: course_chapters

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | course_id | varchar(191) | NO | — |  |  |
| 3 | chapter_name | varchar(191) | YES | — |  |  |
| 4 | short_number | varchar(191) | YES | — |  |  |
| 5 | status | enum('1','0') | NO | — |  |  |
| 6 | file | varchar(191) | YES | — |  |  |
| 7 | created_at | timestamp | YES | — |  |  |
| 8 | updated_at | timestamp | YES | — |  |  |
| 9 | user_id | int | YES | — |  |  |
| 10 | position | int | YES | — |  |  |
| 11 | drip_type | varchar(191) | YES | — |  |  |
| 12 | drip_date | date | YES | — |  |  |
| 13 | drip_days | varchar(191) | YES | — |  |  |
| 14 | goal_date | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: course_classes

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | course_id | varchar(191) | YES | — |  |  |
| 3 | coursechapter_id | varchar(191) | YES | — |  |  |
| 4 | title | varchar(191) | YES | — |  |  |
| 5 | image | varchar(191) | YES | — |  |  |
| 6 | zip | varchar(191) | YES | — |  |  |
| 7 | pdf | varchar(191) | YES | — |  |  |
| 8 | audio | varchar(191) | YES | — |  |  |
| 9 | size | varchar(191) | YES | — |  |  |
| 10 | url | varchar(191) | YES | — |  |  |
| 11 | iframe_url | text | YES | — |  |  |
| 12 | video | varchar(191) | YES | — |  |  |
| 13 | duration | varchar(191) | YES | — |  |  |
| 14 | status | enum('1','0') | YES | — |  |  |
| 15 | featured | enum('1','0') | YES | — |  |  |
| 16 | type | varchar(191) | YES | — |  |  |
| 17 | preview_video | varchar(191) | YES | — |  |  |
| 18 | preview_url | varchar(191) | YES | — |  |  |
| 19 | preview_type | varchar(191) | YES | — |  |  |
| 20 | date_time | datetime | YES | — |  |  |
| 21 | detail | text | YES | — |  |  |
| 22 | position | int | YES | — |  |  |
| 23 | aws_upload | varchar(191) | YES | — |  |  |
| 24 | created_at | timestamp | YES | — |  |  |
| 25 | updated_at | timestamp | YES | — |  |  |
| 26 | user_id | int | YES | — |  |  |
| 27 | file | varchar(191) | YES | — |  |  |
| 28 | drip_type | varchar(191) | YES | — |  |  |
| 29 | drip_date | date | YES | — |  |  |
| 30 | drip_days | int | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: course_includes

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | course_id | varchar(191) | NO | — |  |  |
| 3 | item | varchar(191) | YES | — |  |  |
| 4 | icon | varchar(191) | YES | — |  |  |
| 5 | detail | text | YES | — |  |  |
| 6 | status | enum('1','0') | NO | — |  |  |
| 7 | created_at | timestamp | YES | — |  |  |
| 8 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: course_languages

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | name | varchar(191) | NO | — |  |  |
| 3 | status | enum('1','0') | NO | — |  |  |
| 4 | created_at | timestamp | YES | — |  |  |
| 5 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: course_progress

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | course_id | int | NO | — |  |  |
| 4 | mark_chapter_id | varchar(191) | YES | — |  |  |
| 5 | all_chapter_id | varchar(191) | YES | — |  |  |
| 6 | created_at | timestamp | YES | — |  |  |
| 7 | updated_at | timestamp | YES | — |  |  |
| 8 | mark_class_id | varchar(191) | YES | — |  |  |
| 9 | all_class_id | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: course_reports

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | course_id | int | NO | — |  |  |
| 3 | user_id | int | NO | — |  |  |
| 4 | title | varchar(191) | NO | — |  |  |
| 5 | email | varchar(191) | NO | — |  |  |
| 6 | detail | longtext | NO | — |  |  |
| 7 | created_at | timestamp | YES | — |  |  |
| 8 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: course_texts

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | heading | varchar(191) | NO | — |  |  |
| 3 | sub_heading | varchar(191) | NO | — |  |  |
| 4 | created_at | timestamp | YES | — |  |  |
| 5 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: courserejects

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | created_at | timestamp | YES | — |  |  |
| 3 | updated_at | timestamp | YES | — |  |  |
| 4 | course_id | varchar(191) | YES | — |  |  |
| 5 | reason | text | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: courses

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | user_id | varchar(191) | NO | — |  |  |
| 3 | category_id | varchar(191) | NO | — |  |  |
| 4 | subcategory_id | varchar(191) | NO | — |  |  |
| 5 | childcategory_id | varchar(191) | NO | — |  |  |
| 6 | language_id | varchar(191) | NO | — |  |  |
| 7 | title | varchar(191) | YES | — |  |  |
| 8 | short_detail | text | YES | — |  |  |
| 9 | detail | text | YES | — |  |  |
| 10 | requirement | text | YES | — |  |  |
| 11 | discussion_group_link | varchar(191) | YES | — |  |  |
| 12 | price | varchar(191) | YES | — |  |  |
| 13 | discount_price | varchar(191) | YES | — |  |  |
| 14 | day | varchar(191) | YES | — |  |  |
| 15 | video | varchar(191) | YES | — |  |  |
| 16 | url | varchar(191) | YES | — |  |  |
| 17 | featured | enum('1','0') | YES | — |  |  |
| 18 | slug | varchar(191) | YES | — |  |  |
| 19 | status | enum('1','0') | YES | — |  |  |
| 20 | preview_image | varchar(191) | YES | — |  |  |
| 21 | video_url | varchar(191) | YES | — |  |  |
| 22 | preview_type | varchar(191) | YES | — |  |  |
| 23 | type | enum('1','0') | YES | — |  |  |
| 24 | duration | int | YES | — |  |  |
| 25 | created_at | timestamp | YES | — |  |  |
| 26 | updated_at | timestamp | YES | — |  |  |
| 27 | duration_type | varchar(191) | NO | m |  |  |
| 28 | instructor_revenue | int | YES | — |  |  |
| 29 | involvement_request | tinyint(1) | NO | 0 |  |  |
| 30 | refund_policy_id | int | YES | — |  |  |
| 31 | level_tags | longtext | YES | — |  |  |
| 32 | assignment_enable | tinyint(1) | NO | 1 |  |  |
| 33 | appointment_enable | tinyint(1) | NO | 1 |  |  |
| 34 | certificate_enable | tinyint(1) | NO | 1 |  |  |
| 35 | course_tags | longtext | YES | — |  |  |
| 36 | reject_txt | longtext | YES | — |  |  |
| 37 | drip_enable | tinyint(1) | NO | 0 |  |  |
| 38 | institude_id | varchar(191) | YES | — |  |  |
| 39 | country | longtext | YES | — |  |  |
| 40 | other_cats | varchar(255) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: currencies

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | icon | varchar(191) | NO | — |  |  |
| 3 | currency | varchar(191) | NO | — |  |  |
| 4 | default | int | NO | — |  |  |
| 5 | created_at | timestamp | YES | — |  |  |
| 6 | updated_at | timestamp | YES | — |  |  |
| 7 | name | varchar(191) | YES | — |  |  |
| 8 | code | varchar(10) | NO | — |  |  |
| 9 | symbol | varchar(25) | YES | — |  |  |
| 10 | format | varchar(10) | YES | — |  |  |
| 11 | exchange_rate | varchar(191) | YES | — |  |  |
| 12 | active | tinyint(1) | NO | 0 |  |  |
| 13 | position | varchar(191) | NO | r |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- currencies_code_index — NON-UNIQUE; type: BTREE; columns: code
- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: downloadqrs

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | created_at | timestamp | YES | — |  |  |
| 3 | updated_at | timestamp | YES | — |  |  |
| 4 | image | varchar(191) | YES | — |  |  |
| 5 | image2 | varchar(191) | YES | — |  |  |
| 6 | demo_image | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: dropdowns

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | created_at | timestamp | YES | — |  |  |
| 3 | updated_at | timestamp | YES | — |  |  |
| 4 | my_courses | tinyint(1) | NO | 1 |  |  |
| 5 | my_wishlist | tinyint(1) | NO | 1 |  |  |
| 6 | purchased_history | tinyint(1) | NO | 1 |  |  |
| 7 | my_profile | tinyint(1) | NO | 1 |  |  |
| 8 | flash_deal | tinyint(1) | NO | 1 |  |  |
| 9 | donation | tinyint(1) | NO | 1 |  |  |
| 10 | my_wallet | tinyint(1) | NO | 1 |  |  |
| 11 | affilate | tinyint(1) | NO | 1 |  |  |
| 12 | compare | tinyint(1) | NO | 1 |  |  |
| 13 | search_job | tinyint(1) | NO | 1 |  |  |
| 14 | job_portal | tinyint(1) | NO | 1 |  |  |
| 15 | form_enable | tinyint(1) | NO | 1 |  |  |
| 16 | my_leadership | tinyint(1) | NO | 1 |  |  |
| 17 | affilate_dashboard | tinyint(1) | NO | 1 |  |  |
| 18 | role_id | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: ebook_carts

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | ebook_id | int | NO | — |  |  |
| 4 | coupon | varchar(191) | YES | — |  |  |
| 5 | coupon_amount | int | NO | — |  |  |
| 6 | created_at | timestamp | YES | — |  |  |
| 7 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: ebook_categories

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | title | varchar(191) | NO | — |  |  |
| 3 | image | varchar(191) | NO | — |  |  |
| 4 | status | tinyint(1) | NO | 1 |  |  |
| 5 | created_at | timestamp | YES | — |  |  |
| 6 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: ebook_order_details

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | order_id | int | NO | — |  |  |
| 3 | ebook_id | int | NO | — |  |  |
| 4 | created_at | timestamp | YES | — |  |  |
| 5 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: ebook_orders

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | order_id | varchar(191) | YES | — |  |  |
| 4 | ebook_id | int | NO | — |  |  |
| 5 | transaction_id | varchar(191) | YES | — |  |  |
| 6 | orignal_price | varchar(191) | YES | — |  |  |
| 7 | payment_method | varchar(191) | YES | — |  |  |
| 8 | total_amount | varchar(191) | YES | — |  |  |
| 9 | coupon | varchar(191) | YES | — |  |  |
| 10 | coupon_amount | varchar(191) | YES | — |  |  |
| 11 | currency | varchar(191) | YES | — |  |  |
| 12 | status | varchar(191) | NO | 1 |  |  |
| 13 | created_at | timestamp | YES | — |  |  |
| 14 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: ebook_reviews

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | ebook_id | int | NO | — |  |  |
| 4 | comment | text | YES | — |  |  |
| 5 | rating | text | YES | — |  |  |
| 6 | created_at | timestamp | YES | — |  |  |
| 7 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: ebooks

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | author_id | bigint unsigned | YES | — |  |  |
| 3 | user_id | int | NO | — |  |  |
| 4 | title | varchar(191) | NO | — |  |  |
| 5 | slug | varchar(191) | YES | — |  |  |
| 6 | category_id | varchar(191) | NO | — |  |  |
| 7 | detail | longtext | YES | — |  |  |
| 8 | publication | varchar(191) | YES | — |  |  |
| 9 | edition | varchar(191) | YES | — |  |  |
| 10 | banner | varchar(191) | YES | — |  |  |
| 11 | thumbnali | varchar(191) | YES | — |  |  |
| 12 | price | varchar(191) | YES | — |  |  |
| 13 | pages | int unsigned | NO | 0 |  |  |
| 14 | format | varchar(191) | NO | PDF Ebook |  |  |
| 15 | description | text | YES | — |  |  |
| 16 | image | varchar(191) | YES | — |  |  |
| 17 | free | varchar(191) | NO | No |  |  |
| 18 | discount_check | varchar(191) | NO | No |  |  |
| 19 | discount_price | varchar(191) | YES | — |  |  |
| 20 | files | varchar(191) | YES | — |  |  |
| 21 | all_file | varchar(191) | YES | — |  |  |
| 22 | status | tinyint(1) | NO | 1 |  |  |
| 23 | created_at | timestamp | YES | — |  |  |
| 24 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: email_templates

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | subject | varchar(191) | NO | — |  |  |
| 3 | title | varchar(191) | NO | — |  |  |
| 4 | action | varchar(191) | YES | — |  |  |
| 5 | message | text | YES | — |  |  |
| 6 | type | varchar(191) | NO | — |  |  |
| 7 | created_at | timestamp | YES | — |  |  |
| 8 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: facts

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | created_at | timestamp | YES | — |  |  |
| 3 | updated_at | timestamp | YES | — |  |  |
| 4 | title | varchar(191) | NO | — |  |  |
| 5 | image | varchar(191) | NO | — |  |  |
| 6 | description | varchar(191) | NO | — |  |  |
| 7 | number | varchar(191) | NO | — |  |  |
| 8 | status | tinyint(1) | NO | 1 |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: faq_instructors

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | category_id | int | NO | — |  |  |
| 3 | title | varchar(191) | NO | — |  |  |
| 4 | details | text | NO | — |  |  |
| 5 | status | tinyint(1) | NO | — |  |  |
| 6 | created_at | timestamp | YES | — |  |  |
| 7 | updated_at | timestamp | YES | — |  |  |
| 8 | position | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: faq_students

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | category_id | int | NO | — |  |  |
| 3 | title | varchar(191) | NO | — |  |  |
| 4 | details | text | NO | — |  |  |
| 5 | status | tinyint(1) | NO | — |  |  |
| 6 | created_at | timestamp | YES | — |  |  |
| 7 | updated_at | timestamp | YES | — |  |  |
| 8 | position | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: feature_courses

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | user_id | varchar(191) | NO | — |  |  |
| 3 | course_id | varchar(191) | NO | — |  |  |
| 4 | total_amount | varchar(191) | YES | — |  |  |
| 5 | created_at | timestamp | YES | — |  |  |
| 6 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: feature_payments

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | user_id | varchar(191) | NO | — |  |  |
| 3 | course_id | varchar(191) | NO | — |  |  |
| 4 | transaction_id | text | YES | — |  |  |
| 5 | payment_method | varchar(191) | YES | — |  |  |
| 6 | total_amount | varchar(191) | YES | — |  |  |
| 7 | currency | varchar(191) | YES | — |  |  |
| 8 | currency_icon | varchar(191) | YES | — |  |  |
| 9 | featured | tinyint(1) | NO | 1 |  |  |
| 10 | created_at | timestamp | YES | — |  |  |
| 11 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: features

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | created_at | timestamp | YES | — |  |  |
| 3 | updated_at | timestamp | YES | — |  |  |
| 4 | title | varchar(191) | YES | — |  |  |
| 5 | detail | varchar(191) | YES | — |  |  |
| 6 | image | varchar(191) | YES | — |  |  |
| 7 | status | tinyint(1) | NO | 1 |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: featuresettings

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | created_at | timestamp | YES | — |  |  |
| 3 | updated_at | timestamp | YES | — |  |  |
| 4 | title | varchar(191) | YES | — |  |  |
| 5 | detail | varchar(191) | YES | — |  |  |
| 6 | image | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: file_uploads

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | name | varchar(191) | NO | — |  |  |
| 3 | created_at | timestamp | YES | — |  |  |
| 4 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: flash_sale_items

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | sale_id | int unsigned | NO | — |  |  |
| 3 | course_id | int unsigned | NO | — |  |  |
| 4 | discount | double | NO | — |  |  |
| 5 | discount_type | varchar(191) | NO | — |  |  |
| 6 | created_at | timestamp | YES | — |  |  |
| 7 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: flashsales

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | title | varchar(191) | NO | — |  |  |
| 3 | start_date | timestamp | NO | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |  |
| 4 | end_date | timestamp | NO | 0000-00-00 00:00:00 |  |  |
| 5 | background_image | varchar(191) | NO | — |  |  |
| 6 | detail | longtext | YES | — |  |  |
| 7 | status | int unsigned | NO | 1 |  |  |
| 8 | created_at | timestamp | YES | — |  |  |
| 9 | updated_at | timestamp | YES | — |  |  |
| 10 | position | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: flights

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | created_at | timestamp | YES | — |  |  |
| 3 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: followers

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | follower_id | int | NO | — |  |  |
| 4 | created_at | timestamp | YES | — |  |  |
| 5 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: forum_comments

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | topic_id | bigint unsigned | NO | — |  |  |
| 3 | parent_comment_id | int | NO | — |  |  |
| 4 | description | text | NO | — |  |  |
| 5 | posted_by_user_id | bigint unsigned | NO | — |  |  |
| 6 | created_at | timestamp | YES | — |  |  |
| 7 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: forum_topics

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | topic_title | varchar(191) | NO | — |  |  |
| 3 | description | text | NO | — |  |  |
| 4 | photo | text | YES | — |  |  |
| 5 | created_by_user_id | bigint unsigned | NO | — |  |  |
| 6 | category_id | bigint unsigned | NO | — |  |  |
| 7 | display_order | varchar(191) | NO | — |  |  |
| 8 | display_in_listing | tinyint | NO | — |  |  |
| 9 | slug | varchar(191) | NO | — |  |  |
| 10 | status | enum('1','0') | NO | — |  | 1:active, 0:In-Active |
| 11 | created_at | timestamp | YES | — |  |  |
| 12 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: forums_categories

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | category_name | varchar(191) | YES | — |  |  |
| 3 | slug | varchar(191) | NO | — |  |  |
| 4 | status | enum('1','0') | NO | — |  | 1:active, 0:In-Active |
| 5 | created_at | timestamp | YES | — |  |  |
| 6 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: get_starteds

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | heading | varchar(191) | YES | — |  |  |
| 3 | sub_heading | varchar(1916) | YES | — |  |  |
| 4 | button_txt | varchar(191) | YES | — |  |  |
| 5 | image | varchar(191) | YES | — |  |  |
| 6 | created_at | timestamp | YES | — |  |  |
| 7 | updated_at | timestamp | YES | — |  |  |
| 8 | link | text | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: googleclassrooms

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | YES | — |  |  |
| 3 | owner_id | varchar(191) | NO | — |  |  |
| 4 | course_id | int | YES | — |  |  |
| 5 | classroom_cource_id | varchar(191) | NO | — |  |  |
| 6 | cource_title | varchar(191) | YES | — |  |  |
| 7 | cource_description | varchar(191) | YES | — |  |  |
| 8 | cource_url | varchar(191) | NO | — |  |  |
| 9 | drive_url | varchar(191) | NO | — |  |  |
| 10 | link_by | varchar(191) | YES | — |  |  |
| 11 | classroom_cource_enrollment_code | varchar(191) | YES | — |  |  |
| 12 | image | varchar(191) | YES | — |  |  |
| 13 | cource_state | varchar(191) | YES | — |  |  |
| 14 | start_time | varchar(191) | YES | — |  |  |
| 15 | end_time | varchar(191) | YES | — |  |  |
| 16 | duration | varchar(191) | YES | — |  |  |
| 17 | timezone | varchar(191) | YES | — |  |  |
| 18 | status | tinyint(1) | NO | — |  |  |
| 19 | join_url | varchar(191) | NO | — |  |  |
| 20 | created_at | timestamp | YES | — |  |  |
| 21 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: googlemeets

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | meeting_id | varchar(191) | YES | — |  |  |
| 3 | user_id | int | YES | — |  |  |
| 4 | owner_id | varchar(191) | YES | — |  |  |
| 5 | meeting_title | varchar(191) | YES | — |  |  |
| 6 | start_time | datetime | YES | — |  |  |
| 7 | end_time | datetime | YES | — |  |  |
| 8 | duration | varchar(191) | YES | — |  |  |
| 9 | meet_url | varchar(191) | YES | — |  |  |
| 10 | link_by | varchar(191) | YES | — |  |  |
| 11 | course_id | int | YES | — |  |  |
| 12 | type | varchar(191) | YES | — |  |  |
| 13 | agenda | longtext | YES | — |  |  |
| 14 | image | varchar(191) | YES | — |  |  |
| 15 | timezone | varchar(191) | YES | — |  |  |
| 16 | created_at | timestamp | YES | — |  |  |
| 17 | updated_at | timestamp | YES | — |  |  |
| 18 | paid_meeting_toggle | tinyint(1) | NO | 0 |  |  |
| 19 | paid_meeting_price | varchar(255) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: homesettings

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | created_at | timestamp | YES | — |  |  |
| 3 | updated_at | timestamp | YES | — |  |  |
| 4 | fact_enable | tinyint(1) | NO | 1 |  |  |
| 5 | discount_enable | tinyint(1) | NO | 1 |  |  |
| 6 | purchase_enable | tinyint(1) | NO | 1 |  |  |
| 7 | recentcourse_enable | tinyint(1) | NO | 1 |  |  |
| 8 | featured_enable | tinyint(1) | NO | 1 |  |  |
| 9 | bundle_enable | tinyint(1) | NO | 1 |  |  |
| 10 | bestselling_enable | tinyint(1) | NO | 1 |  |  |
| 11 | batch_enable | tinyint(1) | NO | 1 |  |  |
| 12 | livemeetings_enable | tinyint(1) | NO | 1 |  |  |
| 13 | blog_enable | tinyint(1) | NO | 1 |  |  |
| 14 | became_enable | tinyint(1) | NO | 1 |  |  |
| 15 | featuredcategories_enable | tinyint(1) | NO | 1 |  |  |
| 16 | testimonial_enable | tinyint(1) | NO | 1 |  |  |
| 17 | video_enable | tinyint(1) | NO | 1 |  |  |
| 18 | instructor_enable | tinyint(1) | NO | 1 |  |  |
| 19 | trusted_enable | varchar(191) | YES | — |  |  |
| 20 | newsletter_enable | varchar(191) | YES | — |  |  |
| 21 | discount_badget_enable | tinyint(1) | NO | 1 |  |  |
| 22 | institute_enable | tinyint(1) | NO | 1 |  |  |
| 23 | get_enable | tinyint(1) | NO | 1 |  |  |
| 24 | service_enable | tinyint(1) | NO | 1 |  |  |
| 25 | feature_enable | tinyint(1) | NO | 1 |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: homework

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | title | varchar(191) | NO | — |  |  |
| 3 | description | varchar(191) | NO | — |  |  |
| 4 | pdf | varchar(191) | NO | — |  |  |
| 5 | status | int | NO | — |  |  |
| 6 | marks | int | YES | — |  |  |
| 7 | user_id | int | NO | — |  |  |
| 8 | course_id | int | NO | — |  |  |
| 9 | compulsory | int | NO | — |  |  |
| 10 | endtime | datetime | NO | — |  |  |
| 11 | created_at | timestamp | YES | — |  |  |
| 12 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: institute

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | title | varchar(191) | NO | — |  |  |
| 3 | detail | varchar(191) | NO | — |  |  |
| 4 | user_id | varchar(191) | NO | — |  |  |
| 5 | image | varchar(191) | NO | — |  |  |
| 6 | status | varchar(191) | NO | 1 |  |  |
| 7 | verified | varchar(191) | NO | 0 |  |  |
| 8 | skill | varchar(191) | NO | — |  |  |
| 9 | created_at | timestamp | YES | — |  |  |
| 10 | updated_at | timestamp | YES | — |  |  |
| 11 | email | varchar(191) | YES | — |  |  |
| 12 | mobile | varchar(191) | YES | — |  |  |
| 13 | affilated_by | varchar(191) | YES | — |  |  |
| 14 | address | varchar(191) | YES | — |  |  |
| 15 | slug | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: instructor_plan

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | title | varchar(191) | YES | — |  |  |
| 3 | detail | longtext | YES | — |  |  |
| 4 | price | varchar(191) | YES | — |  |  |
| 5 | discount_price | varchar(191) | YES | — |  |  |
| 6 | type | varchar(191) | YES | — |  |  |
| 7 | duration | varchar(191) | YES | — |  |  |
| 8 | duration_type | varchar(191) | YES | — |  |  |
| 9 | courses_allowed | int | YES | — |  |  |
| 10 | status | tinyint(1) | NO | 0 |  |  |
| 11 | created_at | timestamp | YES | — |  |  |
| 12 | updated_at | timestamp | YES | — |  |  |
| 13 | preview_image | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: instructor_settings

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | instructor_enable | tinyint(1) | NO | 1 |  |  |
| 3 | instructor_revenue | int | NO | 10 |  |  |
| 4 | admin_revenue | int | YES | — |  |  |
| 5 | paypal_enable | tinyint(1) | NO | 1 |  |  |
| 6 | paytm_enable | tinyint(1) | NO | 1 |  |  |
| 7 | bank_enable | tinyint(1) | NO | 1 |  |  |
| 8 | created_at | timestamp | YES | — |  |  |
| 9 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: instructors

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | user_id | varchar(191) | NO | — |  |  |
| 3 | fname | varchar(191) | NO | — |  |  |
| 4 | lname | varchar(191) | NO | — |  |  |
| 5 | dob | date | NO | — |  |  |
| 6 | email | varchar(191) | NO | — |  |  |
| 7 | mobile | varchar(191) | NO | — |  |  |
| 8 | gender | varchar(191) | NO | — |  |  |
| 9 | detail | text | NO | — |  |  |
| 10 | file | varchar(191) | NO | — |  |  |
| 11 | image | varchar(191) | NO | — |  |  |
| 12 | role | varchar(191) | NO | instructor |  |  |
| 13 | status | tinyint(1) | NO | — |  |  |
| 14 | created_at | timestamp | YES | — |  |  |
| 15 | updated_at | timestamp | YES | — |  |  |

### Constraints

- UNIQUE instructors_email_unique: email
- PRIMARY KEY PRIMARY: id

### Indexes

- instructors_email_unique — UNIQUE; type: BTREE; columns: email
- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: instructorskills

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | created_at | timestamp | YES | — |  |  |
| 3 | updated_at | timestamp | YES | — |  |  |
| 4 | instructor_id | varchar(191) | YES | — |  |  |
| 5 | skills | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: invoice_design

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | logo_enable | tinyint(1) | NO | 1 |  |  |
| 3 | print_type | varchar(191) | YES | — |  |  |
| 4 | border_enable | tinyint(1) | NO | 1 |  |  |
| 5 | border_radius | varchar(191) | YES | — |  |  |
| 6 | border_color | varchar(191) | YES | — |  |  |
| 7 | border_style | varchar(191) | YES | — |  |  |
| 8 | date_format | varchar(191) | YES | — |  |  |
| 9 | created_at | timestamp | YES | — |  |  |
| 10 | updated_at | timestamp | YES | — |  |  |
| 11 | signature | longtext | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: involvements

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | course_id | int | NO | — |  |  |
| 4 | reason | varchar(191) | YES | — |  |  |
| 5 | status | int | NO | 0 |  |  |
| 6 | created_at | timestamp | YES | — |  |  |
| 7 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: jitsimeetings

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | meeting_id | varchar(191) | YES | — |  |  |
| 3 | owner_id | varchar(191) | YES | — |  |  |
| 4 | user_id | int | YES | — |  |  |
| 5 | meeting_title | varchar(191) | YES | — |  |  |
| 6 | start_time | datetime | YES | — |  |  |
| 7 | end_time | datetime | YES | — |  |  |
| 8 | duration | varchar(191) | YES | — |  |  |
| 9 | jitsi_url | varchar(191) | YES | — |  |  |
| 10 | link_by | varchar(191) | YES | — |  |  |
| 11 | course_id | int | YES | — |  |  |
| 12 | time_zone | varchar(191) | YES | — |  |  |
| 13 | type | int | YES | — |  |  |
| 14 | agenda | longtext | YES | — |  |  |
| 15 | image | varchar(191) | YES | — |  |  |
| 16 | created_at | timestamp | YES | — |  |  |
| 17 | updated_at | timestamp | YES | — |  |  |
| 18 | paid_meeting_toggle | tinyint(1) | NO | 0 |  |  |
| 19 | paid_meeting_price | varchar(255) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: jobs

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | queue | varchar(191) | NO | — |  |  |
| 3 | payload | longtext | NO | — |  |  |
| 4 | attempts | tinyint unsigned | NO | — |  |  |
| 5 | reserved_at | int unsigned | YES | — |  |  |
| 6 | available_at | int unsigned | NO | — |  |  |
| 7 | created_at | int unsigned | NO | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- jobs_queue_index — NON-UNIQUE; type: BTREE; columns: queue
- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: jobsettings

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | job_enable | tinyint(1) | NO | 1 |  |  |
| 3 | created_at | timestamp | YES | — |  |  |
| 4 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: join_instructors

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | created_at | timestamp | YES | — |  |  |
| 3 | updated_at | timestamp | YES | — |  |  |
| 4 | img | varchar(191) | NO | — |  |  |
| 5 | text | varchar(191) | NO | — |  |  |
| 6 | detail | varchar(191) | NO | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: languages

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — |  |  |
| 2 | local | varchar(191) | NO | — |  |  |
| 3 | name | varchar(191) | NO | — |  |  |
| 4 | def | tinyint | YES | — |  |  |
| 5 | created_at | timestamp | YES | — |  |  |
| 6 | updated_at | timestamp | YES | — |  |  |
| 7 | language | varchar(191) | YES | — |  |  |

### Constraints

_No table constraints returned._

### Indexes

_No indexes returned._

### Relationships

_No foreign-key relationships returned._

---

## Table: m_pesas

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | checkoutid | varchar(191) | NO | — |  |  |
| 3 | rcode | varchar(191) | NO | — |  |  |
| 4 | rdesc | varchar(191) | NO | — |  |  |
| 5 | txnid | varchar(191) | YES | — |  |  |
| 6 | created_at | timestamp | YES | — |  |  |
| 7 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: mailchimpsettings

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | created_at | timestamp | YES | — |  |  |
| 3 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: manual_payment

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | name | varchar(191) | NO | — |  |  |
| 3 | detail | longtext | YES | — |  |  |
| 4 | image | varchar(191) | YES | — |  |  |
| 5 | status | int unsigned | NO | 0 |  |  |
| 6 | created_at | timestamp | YES | — |  |  |
| 7 | updated_at | timestamp | YES | — |  |  |

### Constraints

- UNIQUE manual_payment_name_unique: name
- PRIMARY KEY PRIMARY: id

### Indexes

- manual_payment_name_unique — UNIQUE; type: BTREE; columns: name
- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: meeting_recordings

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | title | varchar(191) | YES | — |  |  |
| 3 | url | varchar(191) | YES | — |  |  |
| 4 | created_at | timestamp | YES | — |  |  |
| 5 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: meetings

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | meeting_id | varchar(191) | NO | — |  |  |
| 3 | user_id | int | YES | — |  |  |
| 4 | owner_id | varchar(191) | NO | — |  |  |
| 5 | meeting_title | varchar(191) | YES | — |  |  |
| 6 | start_time | datetime | NO | — |  |  |
| 7 | zoom_url | varchar(191) | NO | — |  |  |
| 8 | link_by | varchar(191) | YES | — |  |  |
| 9 | course_id | int | YES | — |  |  |
| 10 | created_at | timestamp | YES | — |  |  |
| 11 | updated_at | timestamp | YES | — |  |  |
| 12 | type | int | YES | — |  |  |
| 13 | agenda | longtext | YES | — |  |  |
| 14 | image | varchar(191) | YES | — |  |  |
| 15 | paid_meeting_toggle | tinyint(1) | NO | 0 |  |  |
| 16 | paid_meeting_price | varchar(255) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: menus

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | created_at | timestamp | YES | — |  |  |
| 3 | updated_at | timestamp | YES | — |  |  |
| 4 | title | varchar(191) | NO | — |  |  |
| 5 | link_by | varchar(191) | NO | — |  |  |
| 6 | position | varchar(191) | YES | — |  |  |
| 7 | page_id | int unsigned | YES | — |  |  |
| 8 | url | varchar(191) | YES | — |  |  |
| 9 | status | int unsigned | NO | 1 |  |  |
| 10 | position_menu | varchar(191) | YES | — |  |  |
| 11 | top | varchar(191) | YES | — |  |  |
| 12 | footer | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: migrations

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | migration | varchar(191) | NO | — |  |  |
| 3 | batch | int | NO | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: mobile_settings

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | created_at | timestamp | YES | — |  |  |
| 3 | updated_at | timestamp | YES | — |  |  |
| 4 | setting_enable | tinyint(1) | NO | 1 |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: model_has_permissions

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | permission_id | bigint unsigned | NO | — |  |  |
| 2 | model_type | varchar(191) | NO | — |  |  |
| 3 | model_id | bigint unsigned | NO | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: permission_id, model_id, model_type

### Indexes

- model_has_permissions_model_id_model_type_index — NON-UNIQUE; type: BTREE; columns: model_id, model_type
- PRIMARY — UNIQUE; type: BTREE; columns: permission_id, model_id, model_type

### Relationships

_No foreign-key relationships returned._

---

## Table: model_has_roles

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | role_id | bigint unsigned | NO | — |  |  |
| 2 | model_type | varchar(191) | NO | — |  |  |
| 3 | model_id | bigint unsigned | NO | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: role_id, model_id, model_type

### Indexes

- model_has_roles_model_id_model_type_index — NON-UNIQUE; type: BTREE; columns: model_id, model_type
- PRIMARY — UNIQUE; type: BTREE; columns: role_id, model_id, model_type

### Relationships

_No foreign-key relationships returned._

---

## Table: notice_boards

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | course_id | varchar(191) | NO | — |  |  |
| 3 | title | varchar(191) | NO | — |  |  |
| 4 | content | text | NO | — |  |  |
| 5 | status | tinyint(1) | NO | 0 |  |  |
| 6 | created_at | timestamp | YES | — |  |  |
| 7 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: notifications

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | char(36) | NO | — |  |  |
| 2 | type | varchar(191) | NO | — |  |  |
| 3 | notifiable_type | varchar(191) | NO | — |  |  |
| 4 | notifiable_id | bigint unsigned | NO | — |  |  |
| 5 | data | text | NO | — |  |  |
| 6 | read_at | timestamp | YES | — |  |  |
| 7 | created_at | timestamp | YES | — |  |  |
| 8 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- notifications_notifiable_type_notifiable_id_index — NON-UNIQUE; type: BTREE; columns: notifiable_type, notifiable_id
- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: oauth_access_tokens

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | varchar(100) | NO | — |  |  |
| 2 | user_id | bigint unsigned | YES | — |  |  |
| 3 | client_id | bigint unsigned | NO | — |  |  |
| 4 | name | varchar(191) | YES | — |  |  |
| 5 | scopes | text | YES | — |  |  |
| 6 | revoked | tinyint(1) | NO | — |  |  |
| 7 | created_at | timestamp | YES | — |  |  |
| 8 | updated_at | timestamp | YES | — |  |  |
| 9 | expires_at | datetime | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- oauth_access_tokens_user_id_index — NON-UNIQUE; type: BTREE; columns: user_id
- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: oauth_auth_codes

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | varchar(100) | NO | — |  |  |
| 2 | user_id | bigint unsigned | NO | — |  |  |
| 3 | client_id | bigint unsigned | NO | — |  |  |
| 4 | scopes | text | YES | — |  |  |
| 5 | revoked | tinyint(1) | NO | — |  |  |
| 6 | expires_at | datetime | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- oauth_auth_codes_user_id_index — NON-UNIQUE; type: BTREE; columns: user_id
- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: oauth_clients

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | bigint unsigned | YES | — |  |  |
| 3 | name | varchar(191) | NO | — |  |  |
| 4 | secret | varchar(100) | YES | — |  |  |
| 5 | provider | varchar(191) | YES | — |  |  |
| 6 | redirect | text | NO | — |  |  |
| 7 | personal_access_client | tinyint(1) | NO | — |  |  |
| 8 | password_client | tinyint(1) | NO | — |  |  |
| 9 | revoked | tinyint(1) | NO | — |  |  |
| 10 | created_at | timestamp | YES | — |  |  |
| 11 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- oauth_clients_user_id_index — NON-UNIQUE; type: BTREE; columns: user_id
- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: oauth_personal_access_clients

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | client_id | bigint unsigned | NO | — |  |  |
| 3 | created_at | timestamp | YES | — |  |  |
| 4 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: oauth_refresh_tokens

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | varchar(100) | NO | — |  |  |
| 2 | access_token_id | varchar(100) | NO | — |  |  |
| 3 | revoked | tinyint(1) | NO | — |  |  |
| 4 | expires_at | datetime | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- oauth_refresh_tokens_access_token_id_index — NON-UNIQUE; type: BTREE; columns: access_token_id
- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: openais

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | generate | varchar(191) | NO | — |  |  |
| 3 | user_id | varchar(191) | NO | — |  |  |
| 4 | prompt | varchar(191) | NO | — |  |  |
| 5 | response | varchar(1000) | NO | — |  |  |
| 6 | created_at | timestamp | YES | — |  |  |
| 7 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: orders

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | course_id | int | YES | — |  |  |
| 3 | user_id | int | NO | — |  |  |
| 4 | instructor_id | int | YES | — |  |  |
| 5 | order_id | varchar(191) | YES | — |  |  |
| 6 | transaction_id | text | NO | — |  |  |
| 7 | payment_method | varchar(191) | NO | — |  |  |
| 8 | total_amount | varchar(191) | NO | — |  |  |
| 9 | coupon_discount | int | YES | — |  |  |
| 10 | currency | varchar(191) | NO | — |  |  |
| 11 | currency_icon | varchar(191) | NO | — |  |  |
| 12 | status | tinyint(1) | NO | 1 |  |  |
| 13 | duration | int | YES | — |  |  |
| 14 | enroll_start | date | YES | — |  |  |
| 15 | enroll_expire | date | YES | — |  |  |
| 16 | instructor_revenue | int | YES | — |  |  |
| 17 | bundle_id | int | YES | — |  |  |
| 18 | bundle_course_id | bigint | YES | — |  |  |
| 19 | proof | varchar(191) | YES | — |  |  |
| 20 | created_at | timestamp | YES | — |  |  |
| 21 | updated_at | timestamp | YES | — |  |  |
| 22 | sale_id | varchar(191) | YES | — |  |  |
| 23 | price_id | varchar(50) | YES | — |  |  |
| 24 | subscription_id | varchar(50) | YES | — |  |  |
| 25 | customer_id | varchar(50) | YES | — |  |  |
| 26 | subscription_status | varchar(50) | YES | — |  |  |
| 27 | refunded | tinyint(1) | NO | 0 |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: pages

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | title | varchar(191) | NO | — |  |  |
| 3 | slug | varchar(191) | NO | — |  |  |
| 4 | details | text | NO | — |  |  |
| 5 | status | tinyint(1) | NO | — |  |  |
| 6 | created_at | timestamp | YES | — |  |  |
| 7 | updated_at | timestamp | YES | — |  |  |
| 8 | page_type | varchar(255) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: paid_mettings

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | transaction_id | varchar(191) | NO | — |  |  |
| 3 | type | varchar(255) | YES | — |  |  |
| 4 | meeting_id | varchar(191) | NO | — |  |  |
| 5 | user_id | varchar(191) | NO | — |  |  |
| 6 | course_id | varchar(191) | YES | — |  |  |
| 7 | amount | varchar(191) | NO | — |  |  |
| 8 | currency | varchar(191) | NO | — |  |  |
| 9 | currency_symbol | varchar(191) | NO | — |  |  |
| 10 | payment_method | varchar(191) | NO | — |  |  |
| 11 | status | tinyint(1) | NO | 0 |  |  |
| 12 | created_at | timestamp | YES | — |  |  |
| 13 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: password_resets

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | email | varchar(191) | NO | — |  |  |
| 2 | token | varchar(191) | NO | — |  |  |
| 3 | created_at | timestamp | YES | — |  |  |

### Constraints

_No table constraints returned._

### Indexes

- password_resets_email_index — NON-UNIQUE; type: BTREE; columns: email

### Relationships

_No foreign-key relationships returned._

---

## Table: payu_transactions

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | paid_for_id | bigint unsigned | YES | — |  |  |
| 3 | paid_for_type | varchar(191) | YES | — |  |  |
| 4 | transaction_id | varchar(191) | NO | — |  |  |
| 5 | gateway | text | NO | — |  |  |
| 6 | body | text | NO | — |  |  |
| 7 | destination | varchar(191) | NO | — |  |  |
| 8 | hash | text | NO | — |  |  |
| 9 | response | text | YES | — |  |  |
| 10 | status | enum('pending','failed','successful','invalid') | NO | pending |  |  |
| 11 | verified_at | timestamp | YES | — |  |  |
| 12 | deleted_at | timestamp | YES | — |  |  |
| 13 | created_at | timestamp | YES | — |  |  |
| 14 | updated_at | timestamp | YES | — |  |  |

### Constraints

- UNIQUE payu_transactions_transaction_id_unique: transaction_id
- PRIMARY KEY PRIMARY: id

### Indexes

- payu_transactions_status_index — NON-UNIQUE; type: BTREE; columns: status
- payu_transactions_transaction_id_unique — UNIQUE; type: BTREE; columns: transaction_id
- payu_transactions_verified_at_index — NON-UNIQUE; type: BTREE; columns: verified_at
- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: pending_payouts

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | course_id | int | NO | — |  |  |
| 4 | order_id | varchar(191) | YES | — |  |  |
| 5 | transaction_id | varchar(191) | NO | — |  |  |
| 6 | total_amount | int | NO | — |  |  |
| 7 | instructor_revenue | int | NO | — |  |  |
| 8 | currency | varchar(191) | NO | — |  |  |
| 9 | currency_icon | varchar(191) | NO | — |  |  |
| 10 | status | tinyint(1) | NO | 0 |  |  |
| 11 | created_at | timestamp | YES | — |  |  |
| 12 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: permissions

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | name | varchar(191) | NO | — |  |  |
| 3 | guard_name | varchar(191) | NO | — |  |  |
| 4 | created_at | timestamp | YES | — |  |  |
| 5 | updated_at | timestamp | YES | — |  |  |

### Constraints

- UNIQUE permissions_name_guard_name_unique: name, guard_name
- PRIMARY KEY PRIMARY: id

### Indexes

- permissions_name_guard_name_unique — UNIQUE; type: BTREE; columns: name, guard_name
- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: personalinfos

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | fname | varchar(191) | NO | — |  |  |
| 4 | lname | varchar(191) | NO | — |  |  |
| 5 | profession | varchar(191) | NO | — |  |  |
| 6 | country | varchar(191) | NO | — |  |  |
| 7 | state | varchar(191) | NO | — |  |  |
| 8 | city | varchar(191) | NO | — |  |  |
| 9 | image | varchar(191) | NO | — |  |  |
| 10 | address | varchar(191) | NO | — |  |  |
| 11 | phone | varchar(191) | NO | — |  |  |
| 12 | email | varchar(191) | NO | — |  |  |
| 13 | skill | varchar(191) | NO | — |  |  |
| 14 | strength | varchar(2000) | NO | — |  |  |
| 15 | interest | varchar(2000) | NO | — |  |  |
| 16 | objective | varchar(2000) | NO | — |  |  |
| 17 | language | varchar(191) | NO | — |  |  |
| 18 | status | varchar(191) | NO | 0 |  |  |
| 19 | verified | varchar(191) | NO | 0 |  |  |
| 20 | message | varchar(191) | YES | — |  |  |
| 21 | created_at | timestamp | YES | — |  |  |
| 22 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: plan_subscription

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | YES | — |  |  |
| 3 | plan_id | int | YES | — |  |  |
| 4 | order_id | varchar(191) | YES | — |  |  |
| 5 | transaction_id | varchar(191) | YES | — |  |  |
| 6 | payment_method | varchar(191) | YES | — |  |  |
| 7 | total_amount | varchar(191) | YES | — |  |  |
| 8 | currency | varchar(191) | YES | — |  |  |
| 9 | currency_icon | varchar(191) | YES | — |  |  |
| 10 | duration | varchar(191) | YES | — |  |  |
| 11 | duration_type | varchar(191) | YES | — |  |  |
| 12 | enroll_start | date | YES | — |  |  |
| 13 | enroll_expire | date | YES | — |  |  |
| 14 | created_at | timestamp | YES | — |  |  |
| 15 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: player_settings

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | logo | varchar(191) | NO | — |  |  |
| 3 | logo_enable | tinyint(1) | NO | 1 |  |  |
| 4 | cpy_text | varchar(191) | NO | — |  |  |
| 5 | share_enable | tinyint(1) | NO | 1 |  |  |
| 6 | autoplay | tinyint(1) | NO | 1 |  |  |
| 7 | download | int | NO | 0 |  |  |
| 8 | created_at | timestamp | YES | — |  |  |
| 9 | updated_at | timestamp | YES | — |  |  |
| 10 | subtitle_font_size | int | YES | — |  |  |
| 11 | subtitle_color | varchar(191) | YES | — |  |  |
| 12 | embedded_enable | tinyint(1) | NO | 0 |  |  |
| 13 | skin | varchar(255) | YES | — |  |  |
| 14 | loop_video | tinyint(1) | NO | 0 |  |  |
| 15 | player_google_analytics_id | varchar(255) | YES | — |  |  |
| 16 | chrome_cast | tinyint(1) | NO | 0 |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: postjobs

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | companyname | varchar(191) | NO | — |  |  |
| 4 | title | varchar(191) | NO | — |  |  |
| 5 | description | varchar(10000) | NO | — |  |  |
| 6 | min_experience | varchar(191) | NO | — |  |  |
| 7 | max_experience | varchar(191) | NO | — |  |  |
| 8 | experience | varchar(191) | NO | — |  |  |
| 9 | years | varchar(191) | NO | — |  |  |
| 10 | location | varchar(191) | NO | — |  |  |
| 11 | requirement | varchar(191) | NO | — |  |  |
| 12 | role | varchar(191) | NO | — |  |  |
| 13 | industry_type | varchar(191) | NO | — |  |  |
| 14 | employment_type | varchar(191) | NO | — |  |  |
| 15 | image | varchar(191) | NO | — |  |  |
| 16 | min_salary | varchar(191) | NO | — |  |  |
| 17 | max_salary | varchar(191) | NO | — |  |  |
| 18 | salary | varchar(191) | NO | — |  |  |
| 19 | skills | varchar(191) | NO | — |  |  |
| 20 | pdf | varchar(191) | NO | — |  |  |
| 21 | message | varchar(191) | NO | — |  |  |
| 22 | varified | varchar(191) | NO | 0 |  |  |
| 23 | status | varchar(191) | NO | 0 |  |  |
| 24 | approved | varchar(191) | YES | — |  |  |
| 25 | created_at | timestamp | YES | — |  |  |
| 26 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: previous_paper

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | course_id | int | NO | — |  |  |
| 3 | title | varchar(191) | YES | — |  |  |
| 4 | file | varchar(191) | YES | — |  |  |
| 5 | detail | longtext | YES | — |  |  |
| 6 | status | tinyint(1) | NO | 0 |  |  |
| 7 | created_at | timestamp | YES | — |  |  |
| 8 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: private_course

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | longtext | NO | — |  |  |
| 3 | course_id | int | NO | — |  |  |
| 4 | status | tinyint(1) | YES | — |  |  |
| 5 | created_at | timestamp | YES | — |  |  |
| 6 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: projects

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | projecttitle | varchar(191) | NO | — |  |  |
| 4 | role | varchar(191) | NO | — |  |  |
| 5 | description | varchar(191) | NO | — |  |  |
| 6 | created_at | timestamp | YES | — |  |  |
| 7 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: question_book_pdfs

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | course_id | varchar(191) | NO | — |  |  |
| 3 | file_name | varchar(191) | NO | — |  |  |
| 4 | created_at | timestamp | YES | — |  |  |
| 5 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: question_books

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | course_id | varchar(191) | NO | — |  |  |
| 3 | type | varchar(191) | NO | — |  |  |
| 4 | question | text | NO | — |  |  |
| 5 | answer | text | NO | — |  |  |
| 6 | option_one | varchar(191) | NO | — |  |  |
| 7 | option_two | varchar(191) | NO | — |  |  |
| 8 | option_three | varchar(191) | NO | — |  |  |
| 9 | option_four | varchar(191) | NO | — |  |  |
| 10 | correct_option | varchar(191) | NO | — |  |  |
| 11 | created_at | timestamp | YES | — |  |  |
| 12 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: question_reports

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | course_id | int | NO | — |  |  |
| 3 | user_id | int | NO | — |  |  |
| 4 | question_id | int | NO | — |  |  |
| 5 | title | varchar(191) | YES | — |  |  |
| 6 | email | varchar(191) | YES | — |  |  |
| 7 | detail | longtext | YES | — |  |  |
| 8 | created_at | timestamp | YES | — |  |  |
| 9 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: questions

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | user_id | varchar(191) | NO | — |  |  |
| 3 | instructor_id | int | YES | — |  |  |
| 4 | course_id | varchar(191) | NO | — |  |  |
| 5 | question | varchar(191) | NO | — |  |  |
| 6 | answer | varchar(191) | NO | — |  |  |
| 7 | status | enum('1','0') | YES | — |  |  |
| 8 | created_at | timestamp | YES | — |  |  |
| 9 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: quiz_answers

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | course_id | int unsigned | NO | — |  |  |
| 3 | topic_id | int unsigned | NO | — |  |  |
| 4 | user_id | int | NO | — |  |  |
| 5 | question_id | int | NO | — |  |  |
| 6 | user_answer | char(191) | YES | — |  |  |
| 7 | answer | char(191) | YES | — |  |  |
| 8 | created_at | timestamp | YES | — |  |  |
| 9 | updated_at | timestamp | YES | — |  |  |
| 10 | type | varchar(191) | YES | — |  |  |
| 11 | txt_answer | longtext | YES | — |  |  |
| 12 | txt_approved | tinyint(1) | NO | 0 |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: quiz_questions

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | course_id | int | NO | — |  |  |
| 3 | topic_id | int | NO | — |  |  |
| 4 | question | longtext | NO | — |  |  |
| 5 | a | varchar(191) | YES | — |  |  |
| 6 | b | varchar(191) | YES | — |  |  |
| 7 | c | varchar(191) | YES | — |  |  |
| 8 | d | varchar(191) | YES | — |  |  |
| 9 | answer | varchar(191) | YES | — |  |  |
| 10 | created_at | timestamp | YES | — |  |  |
| 11 | updated_at | timestamp | YES | — |  |  |
| 12 | question_video_link | varchar(191) | YES | — |  |  |
| 13 | question_img | varchar(191) | YES | — |  |  |
| 14 | type | varchar(191) | YES | — |  |  |
| 15 | position | varchar(191) | YES | — |  |  |
| 16 | data_type | varchar(191) | NO | Objective |  |  |
| 17 | first_option_ans | varchar(191) | YES | — |  |  |
| 18 | second_option_ans | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: quiz_topics

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | course_id | int | NO | — |  |  |
| 3 | title | varchar(191) | NO | — |  |  |
| 4 | description | text | YES | — |  |  |
| 5 | per_q_mark | int | NO | — |  |  |
| 6 | timer | int | YES | — |  |  |
| 7 | status | tinyint(1) | NO | 1 |  |  |
| 8 | show_ans | int | NO | 0 |  |  |
| 9 | quiz_again | tinyint(1) | NO | 1 |  |  |
| 10 | due_days | int | YES | — |  |  |
| 11 | created_at | timestamp | YES | — |  |  |
| 12 | updated_at | timestamp | YES | — |  |  |
| 13 | type | varchar(191) | YES | — |  |  |
| 14 | position | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: refund_courses

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int unsigned | NO | — |  |  |
| 3 | order_id | int unsigned | NO | — |  |  |
| 4 | course_id | int unsigned | NO | — |  |  |
| 5 | instructor_id | int unsigned | NO | — |  |  |
| 6 | ref_id | varchar(191) | YES | — |  |  |
| 7 | refund_transaction_id | varchar(191) | YES | — |  |  |
| 8 | txn_fee | varchar(191) | YES | — |  |  |
| 9 | payment_method | varchar(100) | NO | — |  |  |
| 10 | total_amount | double unsigned | NO | — |  |  |
| 11 | reason | text | YES | — |  |  |
| 12 | detail | text | YES | — |  |  |
| 13 | bank_id | int unsigned | YES | — |  |  |
| 14 | currency | varchar(191) | YES | — |  |  |
| 15 | currency_icon | varchar(191) | YES | — |  |  |
| 16 | status | tinyint(1) | NO | 0 |  |  |
| 17 | approved | tinyint(1) | NO | 0 |  |  |
| 18 | created_at | timestamp | YES | — |  |  |
| 19 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: refund_policies

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | name | varchar(191) | YES | — |  |  |
| 3 | amount | varchar(191) | YES | — |  |  |
| 4 | days | varchar(191) | YES | — |  |  |
| 5 | detail | text | YES | — |  |  |
| 6 | status | tinyint(1) | NO | 1 |  |  |
| 7 | created_at | timestamp | YES | — |  |  |
| 8 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: related_courses

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | course_id | varchar(191) | YES | — |  |  |
| 3 | main_course_id | varchar(191) | YES | — |  |  |
| 4 | user_id | varchar(191) | YES | — |  |  |
| 5 | status | enum('1','0') | YES | — |  |  |
| 6 | created_at | timestamp | YES | — |  |  |
| 7 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: report_reviews

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | course_id | int | NO | — |  |  |
| 3 | user_id | int | NO | — |  |  |
| 4 | review_id | int | NO | — |  |  |
| 5 | title | varchar(191) | NO | — |  |  |
| 6 | email | varchar(191) | NO | — |  |  |
| 7 | detail | longtext | NO | — |  |  |
| 8 | created_at | timestamp | YES | — |  |  |
| 9 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: review_helpfuls

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | course_id | varchar(191) | NO | — |  |  |
| 3 | user_id | varchar(191) | NO | — |  |  |
| 4 | review_id | varchar(191) | NO | — |  |  |
| 5 | helpful | varchar(191) | NO | — |  |  |
| 6 | created_at | timestamp | YES | — |  |  |
| 7 | updated_at | timestamp | YES | — |  |  |
| 8 | review_like | tinyint(1) | NO | 0 |  |  |
| 9 | review_dislike | tinyint(1) | NO | 0 |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: review_ratings

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | course_id | varchar(191) | NO | — |  |  |
| 3 | user_id | varchar(191) | NO | — |  |  |
| 4 | learn | int | NO | — |  |  |
| 5 | price | int | NO | — |  |  |
| 6 | value | int | NO | — |  |  |
| 7 | review | longtext | NO | — |  |  |
| 8 | status | tinyint(1) | NO | 1 |  |  |
| 9 | approved | tinyint(1) | NO | 1 |  |  |
| 10 | featured | tinyint(1) | YES | — |  |  |
| 11 | created_at | timestamp | YES | — |  |  |
| 12 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: role_has_permissions

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | permission_id | bigint unsigned | NO | — |  |  |
| 2 | role_id | bigint unsigned | NO | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: permission_id, role_id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: permission_id, role_id

### Relationships

_No foreign-key relationships returned._

---

## Table: roles

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | name | varchar(191) | NO | — |  |  |
| 3 | guard_name | varchar(191) | NO | — |  |  |
| 4 | created_at | timestamp | YES | — |  |  |
| 5 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id
- UNIQUE roles_name_guard_name_unique: name, guard_name

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id
- roles_name_guard_name_unique — UNIQUE; type: BTREE; columns: name, guard_name

### Relationships

_No foreign-key relationships returned._

---

## Table: seo_directory

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | city | varchar(191) | YES | — |  |  |
| 3 | state | varchar(191) | YES | — |  |  |
| 4 | country | varchar(191) | YES | — |  |  |
| 5 | detail | longtext | YES | — |  |  |
| 6 | status | tinyint(1) | NO | 0 |  |  |
| 7 | created_at | timestamp | YES | — |  |  |
| 8 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: services

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | created_at | timestamp | YES | — |  |  |
| 3 | updated_at | timestamp | YES | — |  |  |
| 4 | title | varchar(191) | YES | — |  |  |
| 5 | detail | varchar(191) | YES | — |  |  |
| 6 | image | varchar(191) | YES | — |  |  |
| 7 | status | tinyint(1) | NO | 1 |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: servicesettings

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | created_at | timestamp | YES | — |  |  |
| 3 | updated_at | timestamp | YES | — |  |  |
| 4 | title | varchar(191) | YES | — |  |  |
| 5 | detail | varchar(191) | YES | — |  |  |
| 6 | image | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: servicess

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | name | varchar(191) | YES | — |  |  |
| 3 | status | tinyint(1) | NO | 1 |  |  |
| 4 | created_at | timestamp | YES | — |  |  |
| 5 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: sessions

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | varchar(191) | NO | — |  |  |
| 2 | user_id | bigint unsigned | YES | — |  |  |
| 3 | ip_address | varchar(45) | YES | — |  |  |
| 4 | user_agent | text | YES | — |  |  |
| 5 | payload | text | NO | — |  |  |
| 6 | last_activity | int | NO | — |  |  |

### Constraints

- UNIQUE sessions_id_unique: id

### Indexes

- sessions_id_unique — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: settings

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | currency_symbol | varchar(255) | YES | — |  |  |
| 3 | currency | varchar(255) | YES | — |  |  |
| 4 | project_title | varchar(191) | YES | — |  |  |
| 5 | logo | varchar(191) | YES | — |  |  |
| 6 | favicon | varchar(191) | YES | — |  |  |
| 7 | cpy_txt | varchar(191) | YES | — |  |  |
| 8 | logo_type | varchar(191) | YES | — |  |  |
| 9 | rightclick | tinyint(1) | NO | 1 |  |  |
| 10 | inspect | tinyint(1) | NO | 1 |  |  |
| 11 | meta_data_desc | varchar(191) | YES | — |  |  |
| 12 | meta_data_keyword | varchar(191) | YES | — |  |  |
| 13 | google_ana | varchar(191) | YES | — |  |  |
| 14 | fb_pixel | varchar(191) | YES | — |  |  |
| 15 | google_search_console | varchar(255) | YES | — |  |  |
| 16 | fb_login_enable | tinyint(1) | YES | — |  |  |
| 17 | google_login_enable | tinyint(1) | YES | — |  |  |
| 18 | gitlab_login_enable | tinyint(1) | YES | — |  |  |
| 19 | stripe_enable | tinyint(1) | YES | — |  |  |
| 20 | instamojo_enable | tinyint(1) | YES | — |  |  |
| 21 | paypal_enable | tinyint(1) | YES | — |  |  |
| 22 | paytm_enable | tinyint(1) | YES | — |  |  |
| 23 | braintree_enable | tinyint(1) | YES | — |  |  |
| 24 | razorpay_enable | tinyint(1) | YES | — |  |  |
| 25 | paystack_enable | tinyint(1) | YES | — |  |  |
| 26 | w_email_enable | tinyint(1) | YES | — |  |  |
| 27 | verify_enable | tinyint(1) | NO | 0 |  |  |
| 28 | wel_email | varchar(191) | YES | — |  |  |
| 29 | default_address | text | YES | — |  |  |
| 30 | default_phone | varchar(191) | YES | — |  |  |
| 31 | instructor_enable | tinyint(1) | YES | — |  |  |
| 32 | debug_enable | tinyint(1) | NO | 1 |  |  |
| 33 | cat_enable | int | NO | 0 |  |  |
| 34 | feature_amount | int | YES | — |  |  |
| 35 | preloader_enable | tinyint(1) | YES | 1 |  |  |
| 36 | zoom_enable | int | YES | 0 |  |  |
| 37 | amazon_enable | tinyint(1) | YES | 0 |  |  |
| 38 | captcha_enable | tinyint(1) | YES | 0 |  |  |
| 39 | bbl_enable | tinyint(1) | NO | 0 |  |  |
| 40 | map_lat | varchar(191) | YES | — |  |  |
| 41 | map_long | varchar(191) | YES | — |  |  |
| 42 | map_enable | varchar(191) | NO | map |  |  |
| 43 | contact_image | varchar(191) | YES | — |  |  |
| 44 | mobile_enable | tinyint(1) | NO | 0 |  |  |
| 45 | promo_enable | tinyint(1) | NO | 0 |  |  |
| 46 | promo_text | text | YES | — |  |  |
| 47 | promo_link | varchar(191) | YES | — |  |  |
| 48 | linkedin_enable | tinyint(1) | NO | 0 |  |  |
| 49 | map_api | varchar(191) | YES | — |  |  |
| 50 | twitter_enable | tinyint(1) | NO | 0 |  |  |
| 51 | aws_enable | tinyint(1) | YES | 0 |  |  |
| 52 | certificate_enable | tinyint(1) | NO | 1 |  |  |
| 53 | device_control | tinyint(1) | NO | 0 |  |  |
| 54 | ipblock_enable | tinyint(1) | NO | 0 |  |  |
| 55 | ipblock | text | YES | — |  |  |
| 56 | assignment_enable | tinyint(1) | YES | 0 |  |  |
| 57 | appointment_enable | tinyint(1) | YES | 0 |  |  |
| 58 | created_at | timestamp | YES | — |  |  |
| 59 | updated_at | timestamp | YES | — |  |  |
| 60 | hide_identity | tinyint(1) | NO | 0 |  |  |
| 61 | footer_logo | varchar(191) | YES | — |  |  |
| 62 | enable_omise | int | NO | 0 |  |  |
| 63 | enable_payu | int | NO | 0 |  |  |
| 64 | enable_moli | int | NO | 0 |  |  |
| 65 | enable_cashfree | int | NO | 0 |  |  |
| 66 | enable_skrill | int | NO | 0 |  |  |
| 67 | enable_rave | int | NO | 0 |  |  |
| 68 | preloader_logo | varchar(191) | YES | — |  |  |
| 69 | chat_bubble | text | YES | — |  |  |
| 70 | wapp_phone | varchar(191) | YES | — |  |  |
| 71 | wapp_popup_msg | text | YES | — |  |  |
| 72 | wapp_title | text | YES | — |  |  |
| 73 | wapp_position | varchar(191) | YES | — |  |  |
| 74 | wapp_color | varchar(191) | YES | — |  |  |
| 75 | wapp_enable | tinyint(1) | NO | 0 |  |  |
| 76 | enable_payhere | tinyint(1) | NO | 0 |  |  |
| 77 | app_download | tinyint(1) | NO | 0 |  |  |
| 78 | app_link | varchar(191) | YES | — |  |  |
| 79 | play_download | tinyint(1) | NO | 0 |  |  |
| 80 | play_link | varchar(191) | YES | — |  |  |
| 81 | iyzico_enable | tinyint(1) | NO | 0 |  |  |
| 82 | course_hover | tinyint(1) | NO | 1 |  |  |
| 83 | ssl_enable | tinyint(1) | NO | 0 |  |  |
| 84 | currency_swipe | tinyint(1) | NO | 1 |  |  |
| 85 | attandance_enable | tinyint(1) | NO | 0 |  |  |
| 86 | youtube_enable | tinyint(1) | NO | 0 |  |  |
| 87 | vimeo_enable | tinyint(1) | NO | 0 |  |  |
| 88 | aamarpay_enable | tinyint(1) | NO | 0 |  |  |
| 89 | activity_enable | tinyint(1) | NO | 0 |  |  |
| 90 | twilio_enable | tinyint(1) | NO | 0 |  |  |
| 91 | plan_enable | tinyint(1) | NO | 0 |  |  |
| 92 | googlemeet_enable | tinyint(1) | NO | 0 |  |  |
| 93 | cookie_enable | tinyint(1) | NO | 1 |  |  |
| 94 | jitsimeet_enable | tinyint(1) | NO | 1 |  |  |
| 95 | payflexi_enable | tinyint(1) | NO | 0 |  |  |
| 96 | donation_enable | tinyint(1) | NO | 0 |  |  |
| 97 | donation_link | varchar(191) | YES | — |  |  |
| 98 | googlepay_enable | tinyint(1) | NO | 0 |  |  |
| 99 | guest_enable | tinyint(1) | NO | 0 |  |  |
| 100 | notifiy_enable | tinyint(1) | NO | 0 |  |  |
| 101 | text | varchar(191) | YES | — |  |  |
| 102 | category_enable | tinyint(1) | YES | 0 |  |  |
| 103 | img | varchar(191) | YES | — |  |  |
| 104 | watch_enable | tinyint(1) | NO | 0 |  |  |
| 105 | watch_time | varchar(191) | YES | — |  |  |
| 106 | sidebar_enable | tinyint(1) | NO | 1 |  |  |
| 107 | instructor_sidebar | tinyint(1) | NO | 1 |  |  |
| 108 | map_url | varchar(255) | YES | — |  |  |
| 109 | verify_status | enum('0','1') | YES | 0 |  |  |
| 110 | verify_message | varchar(255) | NO | — |  |  |
| 111 | esewa_enable | tinyint(1) | NO | 0 |  |  |
| 112 | smanager_enable | tinyint(1) | NO | 0 |  |  |
| 113 | forum_enable | varchar(191) | YES | — |  |  |
| 114 | theme | tinyint(1) | NO | 1 |  |  |
| 115 | api_enable | tinyint | NO | 1 |  |  |
| 116 | api_key | varchar(255) | YES | — |  |  |
| 117 | wasabi_enable | tinyint | NO | 0 |  |  |
| 118 | bunny_enable | tinyint | NO | 0 |  |  |
| 119 | otp_enable | tinyint(1) | NO | 0 |  |  |
| 120 | screenshot_enable | tinyint(1) | NO | 0 |  |  |
| 121 | instagram_url | varchar(255) | YES | — |  |  |
| 122 | facebook_url | varchar(255) | YES | — |  |  |
| 123 | youtube_url | varchar(255) | YES | — |  |  |
| 124 | twitter_url | varchar(255) | YES | — |  |  |
| 125 | cookie_message | longtext | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: slider_facts

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | icon | varchar(191) | NO | — |  |  |
| 3 | heading | varchar(191) | NO | — |  |  |
| 4 | sub_heading | varchar(191) | NO | — |  |  |
| 5 | created_at | timestamp | YES | — |  |  |
| 6 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: sliders

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | heading | varchar(191) | NO | — |  |  |
| 3 | sub_heading | varchar(191) | YES | — |  |  |
| 4 | detail | text | NO | — |  |  |
| 5 | button_primary | varchar(191) | YES | — |  |  |
| 6 | button_primary_url | varchar(255) | YES | — |  |  |
| 7 | button_outline | varchar(191) | YES | — |  |  |
| 8 | button_outline_url | varchar(255) | YES | — |  |  |
| 9 | status | enum('1','0') | NO | — |  |  |
| 10 | image | varchar(191) | NO | — |  |  |
| 11 | position | int | YES | — |  |  |
| 12 | created_at | timestamp | YES | — |  |  |
| 13 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: states

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | state_id | int | YES | — |  |  |
| 3 | name | varchar(30) | NO | — |  |  |
| 4 | country_id | int | NO | 1 |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: sub_categories

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | category_id | varchar(191) | NO | — |  |  |
| 3 | title | varchar(191) | YES | — |  |  |
| 4 | icon | varchar(191) | YES | — |  |  |
| 5 | slug | varchar(191) | YES | — |  |  |
| 6 | status | enum('1','0') | NO | — |  |  |
| 7 | created_at | timestamp | YES | — |  |  |
| 8 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: submit_homework

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — |  |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | homework_id | int | NO | — |  |  |
| 4 | instructor_id | int | YES | — |  |  |
| 5 | course_id | int | NO | — |  |  |
| 6 | detail | varchar(191) | YES | — |  |  |
| 7 | homework | varchar(191) | YES | — |  |  |
| 8 | remark | varchar(191) | YES | — |  |  |
| 9 | marks | int | YES | — |  |  |
| 10 | created_at | timestamp | YES | — |  |  |
| 11 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: subscription_items

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | subscription_id | bigint unsigned | NO | — |  |  |
| 3 | stripe_id | varchar(191) | NO | — |  |  |
| 4 | stripe_product | varchar(191) | NO | — |  |  |
| 5 | stripe_price | varchar(191) | NO | — |  |  |
| 6 | quantity | int | YES | — |  |  |
| 7 | created_at | timestamp | YES | — |  |  |
| 8 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id
- UNIQUE subscription_items_stripe_id_unique: stripe_id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id
- subscription_items_stripe_id_unique — UNIQUE; type: BTREE; columns: stripe_id
- subscription_items_subscription_id_stripe_price_index — NON-UNIQUE; type: BTREE; columns: subscription_id, stripe_price

### Relationships

_No foreign-key relationships returned._

---

## Table: subscriptions

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | bigint unsigned | NO | — |  |  |
| 3 | name | varchar(191) | NO | — |  |  |
| 4 | stripe_id | varchar(191) | NO | — |  |  |
| 5 | stripe_status | varchar(191) | NO | — |  |  |
| 6 | stripe_price | varchar(191) | YES | — |  |  |
| 7 | quantity | int | YES | — |  |  |
| 8 | trial_ends_at | timestamp | YES | — |  |  |
| 9 | ends_at | timestamp | YES | — |  |  |
| 10 | created_at | timestamp | YES | — |  |  |
| 11 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id
- UNIQUE subscriptions_stripe_id_unique: stripe_id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id
- subscriptions_stripe_id_unique — UNIQUE; type: BTREE; columns: stripe_id
- subscriptions_user_id_stripe_status_index — NON-UNIQUE; type: BTREE; columns: user_id, stripe_status

### Relationships

_No foreign-key relationships returned._

---

## Table: subtitles

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | sub_lang | varchar(191) | YES | — |  |  |
| 3 | sub_t | varchar(191) | YES | — |  |  |
| 4 | c_id | varchar(191) | YES | — |  |  |
| 5 | created_at | timestamp | YES | — |  |  |
| 6 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: support_types

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | name | varchar(191) | YES | — |  |  |
| 3 | created_at | timestamp | YES | — |  |  |
| 4 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: terms

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | terms | longtext | NO | — |  |  |
| 3 | policy | longtext | NO | — |  |  |
| 4 | created_at | timestamp | YES | — |  |  |
| 5 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: testimonials

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | client_name | varchar(191) | NO | — |  |  |
| 3 | details | text | NO | — |  |  |
| 4 | status | tinyint(1) | NO | — |  |  |
| 5 | image | varchar(191) | NO | — |  |  |
| 6 | created_at | timestamp | YES | — |  |  |
| 7 | updated_at | timestamp | YES | — |  |  |
| 8 | rating | varchar(191) | YES | — |  |  |
| 9 | designation | longtext | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: trusteds

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | url | varchar(191) | NO | — |  |  |
| 3 | image | varchar(191) | NO | — |  |  |
| 4 | status | enum('1','0') | NO | — |  |  |
| 5 | created_at | timestamp | YES | — |  |  |
| 6 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: upis

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | created_at | timestamp | YES | — |  |  |
| 3 | updated_at | timestamp | YES | — |  |  |
| 4 | name | varchar(191) | YES | — |  |  |
| 5 | upiid | varchar(191) | YES | — |  |  |
| 6 | status | tinyint(1) | NO | 1 |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: user_bank

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | bank_name | varchar(191) | NO | — |  |  |
| 4 | ifcs_code | varchar(191) | YES | — |  |  |
| 5 | account_number | varchar(191) | NO | — |  |  |
| 6 | account_holder_name | varchar(191) | NO | — |  |  |
| 7 | swift_code | varchar(191) | YES | — |  |  |
| 8 | bank_enable | tinyint(1) | NO | 1 |  |  |
| 9 | created_at | timestamp | YES | — |  |  |
| 10 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: user_currencies

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_0900_ai_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | bigint unsigned | NO | — |  |  |
| 3 | code | varchar(10) | NO | — |  |  |
| 4 | name | varchar(255) | NO | — |  |  |
| 5 | symbol | varchar(10) | NO | — |  |  |
| 6 | format | varchar(255) | NO | — |  |  |
| 7 | exchange_rate | float(8,2) | NO | — |  |  |
| 8 | default | tinyint(1) | YES | 0 |  |  |
| 9 | created_at | timestamp | YES | — |  |  |
| 10 | updated_at | timestamp | YES | — |  |  |
| 11 | deleted_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: users

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | fname | varchar(191) | NO | — |  |  |
| 3 | lname | varchar(191) | NO | — |  |  |
| 4 | dob | date | YES | — |  |  |
| 5 | doa | date | YES | — |  |  |
| 6 | mobile | varchar(191) | YES | — |  |  |
| 7 | email | varchar(191) | NO | — |  |  |
| 8 | password | varchar(191) | NO | — |  |  |
| 9 | address | varchar(191) | YES | — |  |  |
| 10 | married_status | varchar(191) | YES | — |  |  |
| 11 | city_id | int unsigned | YES | — |  |  |
| 12 | state_id | int unsigned | YES | — |  |  |
| 13 | country_id | int unsigned | YES | — |  |  |
| 14 | gender | varchar(191) | YES | — |  |  |
| 15 | pin_code | varchar(191) | YES | — |  |  |
| 16 | status | tinyint(1) | NO | 1 |  |  |
| 17 | verified | tinyint(1) | NO | — |  |  |
| 18 | user_img | varchar(191) | YES | — |  |  |
| 19 | role | varchar(191) | NO | user |  |  |
| 20 | email_verified_at | datetime | YES | — |  |  |
| 21 | detail | text | YES | — |  |  |
| 22 | short_detail | text | YES | — |  |  |
| 23 | profesi | varchar(191) | YES | — |  |  |
| 24 | braintree_id | int | NO | — |  |  |
| 25 | fb_url | varchar(191) | YES | — |  |  |
| 26 | twitter_url | varchar(191) | YES | — |  |  |
| 27 | youtube_url | varchar(191) | YES | — |  |  |
| 28 | linkedin_url | varchar(191) | YES | — |  |  |
| 29 | instagram_url | varchar(191) | YES | — |  |  |
| 30 | remember_token | varchar(100) | YES | — |  |  |
| 31 | prefer_pay_method | varchar(191) | YES | — |  |  |
| 32 | paypal_email | varchar(191) | YES | — |  |  |
| 33 | paytm_mobile | varchar(191) | YES | — |  |  |
| 34 | bank_acc_name | varchar(191) | YES | — |  |  |
| 35 | bank_acc_no | varchar(191) | YES | — |  |  |
| 36 | ifsc_code | varchar(191) | YES | — |  |  |
| 37 | bank_name | varchar(191) | YES | — |  |  |
| 38 | facebook_id | varchar(191) | YES | — |  |  |
| 39 | google_id | varchar(191) | YES | — |  |  |
| 40 | amazon_id | varchar(191) | YES | — |  |  |
| 41 | created_at | timestamp | YES | — |  |  |
| 42 | updated_at | timestamp | YES | — |  |  |
| 43 | zoom_email | varchar(200) | YES | — |  |  |
| 44 | jwt_token | text | YES | — |  |  |
| 45 | gitlab_id | varchar(191) | YES | — |  |  |
| 46 | linkedin_id | varchar(191) | YES | — |  |  |
| 47 | twitter_id | varchar(191) | YES | — |  |  |
| 48 | code | varchar(191) | YES | — |  |  |
| 49 | google2fa_secret | text | YES | — |  |  |
| 50 | google2fa_enable | tinyint(1) | NO | 0 |  |  |
| 51 | vacation_start | date | YES | — |  |  |
| 52 | vacation_end | date | YES | — |  |  |
| 53 | affiliate_id | varchar(191) | YES | — |  |  |
| 54 | referred_by | varchar(191) | YES | — |  |  |
| 55 | age | varchar(191) | NO | — |  |  |
| 56 | is_verify | tinyint(1) | NO | 1 |  |  |
| 57 | is_blocked | tinyint(1) | NO | 1 |  |  |
| 58 | block_note | varchar(191) | YES | — |  |  |
| 59 | document_detail | varchar(191) | YES | — |  |  |
| 60 | document_file | varchar(191) | YES | — |  |  |
| 61 | exam_percentage | varchar(191) | YES | — |  |  |
| 62 | stripe_id | varchar(191) | YES | — |  |  |
| 63 | pm_type | varchar(191) | YES | — |  |  |
| 64 | pm_last_four | varchar(4) | YES | — |  |  |
| 65 | trial_ends_at | timestamp | YES | — |  |  |
| 66 | delete_request | varchar(255) | YES | — |  |  |
| 67 | delete_reason | varchar(255) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id
- UNIQUE users_email_unique: email

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id
- users_email_unique — UNIQUE; type: BTREE; columns: email
- users_stripe_id_index — NON-UNIQUE; type: BTREE; columns: stripe_id

### Relationships

_No foreign-key relationships returned._

---

## Table: videosettings

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | created_at | timestamp | YES | — |  |  |
| 3 | updated_at | timestamp | YES | — |  |  |
| 4 | url | varchar(191) | NO | — |  |  |
| 5 | tittle | varchar(191) | NO | — |  |  |
| 6 | description | varchar(191) | NO | — |  |  |
| 7 | image | varchar(191) | NO | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: wallet

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int unsigned | NO | — |  |  |
| 3 | balance | double | YES | 0 |  |  |
| 4 | status | int unsigned | NO | 1 |  |  |
| 5 | created_at | timestamp | YES | — |  |  |
| 6 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id
- wallet_user_id_index — NON-UNIQUE; type: BTREE; columns: user_id

### Relationships

_No foreign-key relationships returned._

---

## Table: wallet_settings

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | status | int unsigned | NO | 0 |  |  |
| 3 | paytm_enable | tinyint(1) | YES | 0 |  |  |
| 4 | paypal_enable | tinyint(1) | YES | 0 |  |  |
| 5 | razorpay_enable | tinyint(1) | YES | 0 |  |  |
| 6 | stripe_enable | tinyint(1) | YES | 0 |  |  |
| 7 | braintree_enable | tinyint(1) | YES | 0 |  |  |
| 8 | created_at | timestamp | YES | — |  |  |
| 9 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: wallet_transactions

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int unsigned | NO | — |  |  |
| 3 | wallet_id | int unsigned | NO | — |  |  |
| 4 | type | varchar(191) | NO | — |  |  |
| 5 | total_amount | double | YES | — |  |  |
| 6 | payment_method | varchar(191) | YES | — |  |  |
| 7 | transaction_id | varchar(191) | YES | — |  |  |
| 8 | currency | varchar(191) | YES | — |  |  |
| 9 | currency_icon | varchar(191) | YES | — |  |  |
| 10 | detail | text | YES | — |  |  |
| 11 | expire_at | timestamp | YES | — |  |  |
| 12 | created_at | timestamp | YES | — |  |  |
| 13 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: watch_courses

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | varchar(191) | NO | — |  |  |
| 3 | course_id | varchar(191) | NO | — |  |  |
| 4 | start_time | datetime | YES | — |  |  |
| 5 | active | tinyint(1) | NO | 0 |  |  |
| 6 | created_at | timestamp | YES | — |  |  |
| 7 | updated_at | timestamp | YES | — |  |  |
| 8 | count | varchar(191) | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: what_learns

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | course_id | varchar(191) | YES | — |  |  |
| 3 | detail | text | YES | — |  |  |
| 4 | status | enum('1','0') | YES | — |  |  |
| 5 | created_at | timestamp | YES | — |  |  |
| 6 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: widget_settings

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | widget_one | varchar(191) | NO | — |  |  |
| 3 | widget_two | varchar(191) | NO | — |  |  |
| 4 | widget_three | varchar(191) | NO | — |  |  |
| 5 | created_at | timestamp | YES | — |  |  |
| 6 | updated_at | timestamp | YES | — |  |  |
| 7 | widget_enable | tinyint(1) | NO | 1 |  |  |
| 8 | about_enable | tinyint(1) | NO | 1 |  |  |
| 9 | contact_enable | tinyint(1) | NO | 1 |  |  |
| 10 | career_enable | tinyint(1) | NO | 1 |  |  |
| 11 | blog_enable | tinyint(1) | NO | 1 |  |  |
| 12 | help_enable | tinyint(1) | NO | 1 |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: wishlists

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | int unsigned | NO | — | auto_increment |  |
| 2 | user_id | varchar(191) | NO | — |  |  |
| 3 | course_id | varchar(191) | NO | — |  |  |
| 4 | created_at | timestamp | YES | — |  |  |
| 5 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Table: workexps

| Property | Value |
|---|---|
| Type | BASE TABLE |
| Engine | InnoDB |
| Collation | utf8mb4_unicode_ci |
| Comment |  |

### Columns

| # | Column | Type | Nullable | Default | Extra | Comment |
|---:|---|---|---|---|---|---|
| 1 | id | bigint unsigned | NO | — | auto_increment |  |
| 2 | user_id | int | NO | — |  |  |
| 3 | jobtitle | varchar(191) | NO | — |  |  |
| 4 | employer | varchar(191) | NO | — |  |  |
| 5 | city | varchar(191) | NO | — |  |  |
| 6 | state | varchar(191) | NO | — |  |  |
| 7 | startdate | varchar(191) | NO | — |  |  |
| 8 | enddate | varchar(191) | YES | — |  |  |
| 9 | created_at | timestamp | YES | — |  |  |
| 10 | updated_at | timestamp | YES | — |  |  |

### Constraints

- PRIMARY KEY PRIMARY: id

### Indexes

- PRIMARY — UNIQUE; type: BTREE; columns: id

### Relationships

_No foreign-key relationships returned._

---

## Interpretation Boundary

The generator intentionally does not infer:

- business meaning of tables or columns;
- whether a legacy table or column belongs in the new system;
- whether legacy data must be migrated;
- desired business rules or lifecycle policy;
- application behavior not represented by database metadata;
- technical implementation choices for the new system.

Use this snapshot as legacy database evidence. The Database Architect
must reconcile it with approved requirements, business rules, PRDs,
human decisions, and other authoritative project artifacts before
designing the new database.
