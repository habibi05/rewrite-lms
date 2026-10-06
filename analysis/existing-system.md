---
document: ANALYSIS
artifact_id: ART-001
version: 1.1
status: APPROVED
owner: RE-RESEARCHER
prompt_id: PROMPT-REV-ART-001
sources:
  - legacy LMS repository (d:/laragon/www/insmart)
  - analysis/legacy-schema-snapshot.md
revision_basis:
  source_artifact: ART-001 v1.0
  review_artifact: ART-002
  review_version: 1.0
  findings_addressed:
    - REV-001
    - REV-002
    - REV-003
    - REV-004
    - REV-005
    - REV-006
    - REV-007
    - REV-008
    - REV-009
    - REV-010
    - REV-011
    - REV-012
---

# Existing System Analysis — Legacy LMS (InSmart / eClass)

## 1. Scope of Investigation

This artifact documents the **existing legacy LMS system** as observed from source code, configuration files, database schema, and repository structure. All findings and technical descriptions follow the evidence classification and traceability rules defined in governing contracts (`ARTIFACT-METADATA-CONVENTION-v1`, `ROLE-SPECIFIC-CONTRACT-REVERSE-ENGINEERING-RESEARCHER`, and `REVIEW-ARTIFACT-CONVENTION-v1`).

**Revision History:** This document is revision **v1.1**, updated from v1.0 in direct response to the independent forensic review in **ART-002 v1.0** (`reviews/REVIEW-ART-001-existing-system.md`). The revision systematically addresses findings `REV-001` through `REV-012` by tightening evidence classifications, establishing granular traceability down to source files, symbols, routes, and database tables, reconstructing core execution flows, resolving overbroad claims, clarifying existence versus reachability, and refining conflict and architectural classifications.

**Boundary Statement:** This document records **WHAT EXISTS** in the inspected repository. It does **not** prescribe requirements, target architecture, replacement data models, API/UI contracts, or implementation decisions for the future system. Legacy system behaviors and conventions are recorded strictly as evidence of existing behavior, not as blueprints or mandates for the rewrite.

### Evidence Classification Rules

Every substantive statement in this document is bound to one of the following evidence classifications:

- **`FACT`**: Directly observed and verified in source code, configuration files, database schema, or repository filesystem.
- **`DERIVED`**: Logically inferred from multiple corroborating facts; reasoning and basis are explicitly stated.
- **`UNKNOWN`**: Insufficient evidence exists in the repository or available artifacts to confirm existence, completeness, reachability, or runtime behavior.
- **`CONFLICT`**: Two or more verifiable evidence items directly contradict each other and cannot be reconciled without external resolution.

### Primary Evidence Sources

| Source | Description | Reference Path |
|---|---|---|
| Repository Filesystem | Legacy LMS application codebase | `d:/laragon/www/insmart` |
| Database Schema Snapshot | Forensically extracted MySQL metadata (175 tables, 0 foreign keys) | `analysis/legacy-schema-snapshot.md` |
| Composer Manifest | Backend packages, autoload configuration, scripts | `composer.json` |
| Application Configurations | Core settings, auth guards, module paths | `config/app.php`, `config/auth.php`, `config/modules.php` |
| Module Status Configuration | State flags for modular extensions | `modules_statuses.json` |
| Route Registries | Web and API route definitions | `routes/web.php`, `routes/api.php` |
| Controller & Model Code | Application logic, request handling, Eloquent entity definitions | `app/Http/Controllers/`, `app/*.php` |
| Review Basis | Forensic review findings and required resolutions | `reviews/REVIEW-ART-001-existing-system.md` (ART-002 v1.0) |

---

## 2. Repository & System Overview

| Property | Observed Value | Classification & Granular Evidence |
|---|---|---|
| Framework | Laravel 10.x | **FACT** — `composer.json` line 41: `"laravel/framework": "^10.34.0"` |
| PHP Version | ≥ 8.2 | **FACT** — `composer.json` line 11: `"php": "^8.2"` |
| Application Version | 6.7.0 | **FACT** — `config/app.php` line 32: `'version' => '6.7.0'` |
| Database Engine | MySQL (InnoDB, utf8mb4_unicode_ci) | **FACT** — `analysis/legacy-schema-snapshot.md` table headers |
| Database Name | `project_insmart` | **FACT** — `analysis/legacy-schema-snapshot.md` header |
| Total Tables / Views | 175 | **FACT** — `analysis/legacy-schema-snapshot.md` table index |
| Total Controllers | ~170+ PHP files | **FACT** — Filesystem inspection of `app/Http/Controllers/` |
| Total Models | ~130+ PHP files in `app/` root | **FACT** — Filesystem inspection: flat Eloquent models located directly at `app/*.php` |
| Total Migrations | 203 | **FACT** — Filesystem inspection of `database/migrations/` |
| Route Files | web.php (1,156 lines), api.php (505 lines) | **FACT** — `routes/web.php`, `routes/api.php` line counts |
| Automated Tests | Only default scaffold `ExampleTest` | **FACT** — `tests/Unit/ExampleTest.php`, `tests/Feature/ExampleTest.php`; no domain feature or unit tests exist |
| Frontend Stack | Blade templates (multi-theme) + Inertia.js bridge | **FACT** — `composer.json` line 29 (`inertiajs/inertia-laravel`); Blade views in `resources/views/` (`front/`, `theme_2/`, `fe/`) |
| Module Management Package | `nwidart/laravel-modules` 8.2.* | **FACT** — `composer.json` line 54; `config/modules.php` |
| Configured Modules | 19 entries marked `true` in `modules_statuses.json` | **FACT** (Configuration state) — `modules_statuses.json` lines 2–20. Note: `Modules/` directory is absent from the repository filesystem; runtime loadability is **UNKNOWN** (see Section 3 & 16). |
| API Authentication Guard | Laravel Passport (OAuth2 tokens) | **FACT** — `config/auth.php` line 45 (`'driver' => 'passport'`); `composer.json` line 43 |
| Web Authentication | Laravel session-based authentication | **FACT** — `config/auth.php` line 39 (`'driver' => 'session'`); `App\Http\Controllers\Auth\LoginController` |
| Authorization / RBAC | Spatie Laravel Permission (`HasRoles`) | **FACT** — `composer.json` line 77; `app/User.php` line 21 |
| Product Ancestry | Customized derivative of eClass LMS | **DERIVED** — `config/app.php` fallback `'APP_NAME' => 'Laravel'`; default setting strings reference "Eclass Learning Management"; database naming `project_insmart`. |

---

## 3. Technology & Runtime — Key Backend Dependencies

The presence of a package in `composer.json` or a class file in the repository establishes **structural presence**. It does **not** prove active runtime usage in production unless verified through execution tracing.

### Core Backend Packages

| Package | Inspected Purpose | Structural Presence | Observable Behavior / Reachability |
|---|---|---|---|
| `laravel/framework ^10.34.0` | Application runtime | **FACT** (`composer.json`:41) | **REACHABLE** — Core application framework. |
| `laravel/passport` | API OAuth2 authentication | **FACT** (`composer.json`:43) | **REACHABLE** — Configured as `api` guard in `config/auth.php:45`; consumed in `routes/api.php`. |
| `laravel/socialite ^5.11` | Social OAuth authentication | **FACT** (`composer.json`:44) | **REACHABLE** — Runtime qualifier: **PARTIAL DEAD CODE**. — Providers configured in `config/services.php`; routes in `routes/web.php:73-77`. `LoginController@handleProviderCallback` contains dead code (see Section 19). |
| `spatie/laravel-permission ^5.5` | Role-Based Access Control | **FACT** (`composer.json`:77) | **REACHABLE** — `User` model uses `HasRoles` (`app/User.php:21`); middleware registered in `app/Http/Kernel.php:67-69`. |
| `spatie/laravel-translatable ^6.5.5` | Model attribute translation | **FACT** (`composer.json`:79) | **REACHABLE** — Used in `Course`, `CourseChapter`, `Quiz`, `Blog` models via `$translatable` array. |
| `spatie/laravel-activitylog ^4.7.1` | User activity audit logging | **FACT** (`composer.json`:70) | **CONFIG-DEPENDENT** — Executed conditionally in `LoginController@authenticated` if `Setting.activity_enable == 1`. |
| `spatie/laravel-backup ^8.5.1` | Database backup management | **FACT** (`composer.json`:71) | **CONFIG-DEPENDENT** — Invoked via `app/Console/Commands/DatabaseBackUp.php` and `BackupController.php`. |
| `inertiajs/inertia-laravel ^0.6.6` | Inertia SSR / SPA bridge | **FACT** (`composer.json`:29) | **REFERENCE-ONLY / UNKNOWN** — Middleware `HandleInertiaRequests` in web group (`Kernel.php:38`), but controllers primarily return Blade views; extent of Vue page usage is **UNKNOWN**. |
| `intervention/image ^2.4` | Server-side image manipulation | **FACT** (`composer.json`:31) | **REACHABLE** — Direct calls in `CourseController.php`, `CategoryController.php`, `UserController.php`. |
| `nwidart/laravel-modules 8.2.*` | Modular feature architecture | **FACT** (`composer.json`:54) | **CONFIG-DEPENDENT / BROKEN DEPENDENCY** — Configured in `config/modules.php`; filesystem directory `Modules/` is missing (see Section 3.2). |
| `yajra/laravel-datatables-oracle 10.11.0` | Admin grid DataTables backend | **FACT** (`composer.json`:92) | **REACHABLE** — Used across admin index methods (`OrderController.php`, `UserController.php`). |
| `niklasravnsborg/laravel-pdf ^4.0` | PDF rendering (MPDF wrapper) | **FACT** (`composer.json`:53) | **REACHABLE** — Used in `CertificateController@pdfdownload` and `OrderController@pdfdownload`. |
| `pragmarx/google2fa-laravel ^2.0.2` | Two-factor authentication | **FACT** (`composer.json`:60) | **CONFIG-DEPENDENT** — `Google2FAAuthenticator` middleware in `Kernel.php:57`; `google2fa_secret` on `users` table. |
| `torann/currency ^1.1` | Multi-currency conversions | **FACT** (`composer.json`:84) | **REACHABLE** — Helper `currency()` invoked extensively in `OrderStoreController.php` and `EnrollmentController.php`. |
| `torann/geoip ^3.0` | GeoIP lookup | **FACT** (`composer.json`:85) | **CONFIG-DEPENDENT** — Called in `CourseController@show` and currency resolution. |
| `rap2hpoutre/fast-excel ^5.3.0` | Excel import/export | **FACT** (`composer.json`:62) | **REACHABLE** — Used in `OrderController@fileImportExport` and `QuizController@import`. |

### Cloud, Storage & Communication Dependencies

| Integration | Inspected Evidence | Classification & Status |
|---|---|---|
| AWS S3 | `aws/aws-sdk-php:^3.303`, `league/flysystem-aws-s3-v3` in `composer.json:15,48`; `CourseClass.aws_upload` column in schema. | **FACT** (Component presence) / **UNKNOWN** (Production usage) — Code supports uploading course media to S3; active bucket connectivity in production cannot be verified from repository alone. |
| Firebase Cloud Messaging | `kutia-software-company/larafirebase:^1.2` in `composer.json:38`; `NotificationController.php`. | **FACT** (Component presence) / **UNKNOWN** (Production activity) — Push dispatch code present; active runtime push depends on Google service account credentials. |
| OneSignal Push | `laravel-notification-channels/onesignal:^2.2` in `composer.json:39`. | **FACT** (Package presence) / **UNKNOWN** (Production activity) — Channel registered in `composer.json`; no active dispatch calls observed in core controllers. |
| Twilio SMS | `twilio/sdk:^6.17` in `composer.json:86`; `app/Helpers/TwilioMsg.php`. | **FACT** (Helper presence) / **CONFIG-DEPENDENT** — Invoked in `OrderStoreController:246` if `Setting.twilio_enable == '1'`. Swallows exceptions on delivery failure. |
| Video Providers (YouTube / Vimeo) | `alaouy/youtube:^2.2`, `vimeo/laravel:^5.6` in `composer.json:12,89`; `CourseClass.video_url`, `CourseClass.iframe_url`. | **FACT** (Presence) / **REACHABLE** — Rendered in player view (`WatchController.php`, `resources/views/watch.blade.php`). |
| Live Meetings (Zoom, BBB, Jitsi, Meet) | Controllers in `app/Http/Controllers/` (`ZoomController`, `BigBlueController`, `JitsiController`, `GoogleMeetController`); database tables `meetings`, `b_b_l_s`, `jitsi_meetings`, `googlemeets`. | **FACT** (Presence) / **CONFIG-DEPENDENT** — Each provider requires external API keys configured in settings tables (`setting.zoom_enable`, etc.). |

### Payment Gateway Integrations (REV-003 Analysis)

The codebase contains references, packages, or controller implementations for over 30 payment gateways:
- PayPal, Stripe, Razorpay, Braintree, Mollie, Paystack, Flutterwave (Rave), Paytm, Midtrans, PayU, Iyzico, Omise, Square, Skrill, AamarPay, M-Pesa, Worldpay, SslCommerz, CashFree, ChargilyPay, 2Checkout, DPOPayment, Esewa, Onepay, Paytab, Bkash, PayFlexi, ManualPayment, BankTransfer, WalletPayment, UPI.

**Evidence Classification:**
1. **Component & Package Presence: FACT.** Packages (e.g. `stripe/stripe-php`, `paypal/rest-api-sdk-php`, `razorpay/razorpay`) exist in `composer.json`, and dedicated payment callback controllers exist in `app/Http/Controllers/` (e.g., `StripePaymentController.php`, `PayPalController.php`, `RazorpayController.php`).
2. **Integration Pattern: DERIVED.** Inspected payment controllers follow a pattern where post-payment webhook/callback methods directly instantiate `OrderStoreController` and invoke `orderstore(...)` with transaction parameters.
3. **Operational Runtime Activity: UNKNOWN.** The repository code does not verify which gateways are actively credentialed, enabled in settings, or processing transactions in production. Each gateway is **CONFIG-DEPENDENT**.

### Modular System & `modules_statuses.json` (REV-004 Analysis)

The file `modules_statuses.json` contains 19 entries marked `true`:
`AuthorizeNet`, `Bkash`, `Certificate`, `Chatboard`, `DPOPayment`, `Ebook`, `Esewa`, `Forum`, `Googleclassroom`, `Homework`, `Onepay`, `Paytab`, `Resume`, `Smanager`, `Upi`, `SquarePay`, `Worldpay`, `Midtrains`, `MPesa`.

**Evidence Classification & Reachability:**
- **Configuration State: FACT.** `modules_statuses.json` marks these 19 entries enabled.
- **Filesystem Verification: FACT.** The canonical modules directory `base_path('Modules')` specified in `config/modules.php:73` and `composer.json:129` (`"Modules\\": "Modules/"`) is **completely absent from the repository filesystem**.
- **Source References: FACT.** Isolated controller and model references import from the `Modules\` namespace (e.g., `app/Http/Controllers/CategoryController.php` sets `namespace Modules\Ebook\Http\Controllers;`; `CourseController.php` imports `Modules\Certificate\Models\CertificateDesign;`; `OtherApiController.php` imports `Modules\Homework\Models\Homework` and `Modules\Resume\Models\...`).
- **Runtime Loadability: DERIVED / BROKEN DEPENDENCY.** Because the module class files do not exist under `Modules/`, any execution path attempting to autoload these classes in this repository will trigger a fatal runtime error (`Class "Modules\..." not found`), unless supplied by an external artifact outside this repository. Reachability is classified as **UNKNOWN**. Runtime qualifier: **BROKEN DEPENDENCY**.

### Autoloaded Helper Functions

`composer.json` lines 118–124 explicitly registers 5 helper files loaded on every request (**FACT**):
- `app/Helpers/Tracker.php` — Visitor/traffic tracking logic.
- `app/Helpers/TwilioMsg.php` — Twilio SMS wrapper method.
- `app/Helpers/Is_wishlist.php` — Wishlist existence check helper (`is_wishlist($course_id)`).
- `app/Helpers/currency.php` — Currency formatting and exchange arithmetic (`price_format()`, `currency()`).
- `app/Helpers/fe.php` — Front-end view and layout helper functions.

---

## 4. Architecture (REV-007 Revision)

### Architectural Pattern

The inspected legacy system predominantly exhibits a **monolithic MVC architecture** with the following structural characteristics:

1. **Controller-Centric Logic Delivery:**
   - Application business logic across examined features is implemented directly inside controller classes.
   - Controllers directly invoke Eloquent models, execute raw `DB::table(...)` facade queries, handle file uploads, calculate currency conversions, and trigger notifications.
2. **Service Layer Presence & Usage:**
   - A dedicated `app/Services/` directory exists containing two service classes: `OTPService.php` and `sManagerService.php` (**FACT**).
   - However, application logic across course management, orders, enrollments, quizzes, and certificates is **not consistently mediated through a service layer** (**DERIVED**).
3. **Repository Abstraction:**
   - No repository pattern or interface abstraction layer exists in the inspected codebase (**FACT**). Controllers directly couple to Eloquent queries.
4. **Direct Inter-Controller Coupling:**
   - Multiple payment controllers (e.g., `StripePaymentController.php`, `PayPalController.php`, `BankTransferController.php`, `EnrollmentController.php`) directly instantiate `OrderStoreController` via `new OrderStoreController` and invoke its `orderstore()` method rather than delegating to a shared domain service (**FACT**).
5. **Flat Eloquent Model Structure:**
   - All ~130+ Eloquent models are placed directly in the `app/*.php` root folder rather than inside a domain or `app/Models/` namespace (**FACT**).

### Observed Request-Response Pipeline

```
HTTP Client Request
  │
  ▼
Global Middleware Stack (Kernel.php)
  │ (TrimStrings, CheckForMaintenanceMode, CheckReferral, HandleInertiaRequests)
  ▼
Route-Level Middleware Group (web / api)
  │ (Auth check, IsActive, IsVerified, IsAdmin / AdminIntructor, Spatie RBAC)
  ▼
Controller Method (app/Http/Controllers/*.php)
  │ (Validation, Direct DB queries, Session/Auth inspection, Notification calls)
  ├──► Direct Controller Instantiation (e.g., new OrderStoreController->orderstore())
  ├──► Direct Model / DB Query (app/*.php or DB::table())
  │
  ▼
View Rendering (resources/views/*.blade.php) OR JSON Response (API)
```

---

## 5. Application Directory Structure

```
app/
├── Charts/                 — 6 chart classes (consoletvs/charts integration)
├── Console/Commands/       — 7 custom Artisan commands (DatabaseBackUp, ImportDemo, DemoReset, etc.)
├── Helpers/                — 5 autoloaded helper files (Tracker, TwilioMsg, Is_wishlist, currency, fe)
├── Http/
│   ├── Controllers/        — ~170+ controllers (root + Auth/, Api/, Roles/, landing/)
│   ├── Middleware/         — 19 custom middleware classes
│   └── Requests/           — 44 Form Request validation classes
├── Jobs/                   — 3 Queue Job classes (EnrollExpire, AffiliatesPoints, InstructorPlan)
├── Library/                — SslCommerz payment gateway SDK files (3 files)
├── Mail/                   — 10 Mailable classes (SendOrderMail, AdminMailOnOrder, WelcomeUser, etc.)
├── Notifications/          — 5 Notification classes (UserEnroll, ActivityLog, etc.)
├── Policies/               — 23 Policy classes for authorization
├── Providers/              — 6 Service Providers (AppServiceProvider, AuthServiceProvider, etc.)
├── Services/               — 2 Service classes (OTPService.php, sManagerService.php)
└── *.php                   — ~130+ Eloquent Model files directly in app/ root
```

**Classification: FACT** — Verified by filesystem enumeration of `app/`.

---

## 6. Routing & Middleware Architecture

### 6.1 Web Routing (`routes/web.php` — 1,156 lines)

Web routes are grouped into distinct functional and authorization segments (**FACT**):

1. **Unauthenticated Public Routes:**
   - Login, registration, password reset, OTP verification, initial installer setup (`/install`), system cache clearing.
2. **Admin-Only Protected Routes:**
   - Guarded by middleware `['auth', 'is_admin']` (~400+ routes). Covers administrative management of users, courses, categories, site settings, payment credentials, blog posts, coupon creation, reports, and backup.
3. **Shared Admin & Instructor Routes:**
   - Guarded by middleware `['admin_instructor', 'auth']`. Covers Zoom, BigBlueButton, Jitsi, Google Meet creation, course chapter/class authoring, assignment review, and student attendance tracking.
4. **Public & Enrolled Student Routes:**
   - Guarded by middleware `['is_verified', '2fa', 'maintanance_mode', 'switch_languages']`. Covers course browsing, search, shopping cart, checkout, student dashboard, video watching, progress tracking, and certificate downloads.
5. **Payment Gateway Callbacks:**
   - Named return routes for payment processing (`/payment/status`, `/stripe/post`, `/paypal/success`, etc.).
6. **Localized Prefix Routes:**
   - Indonesian localization routes prefixed with `/jelajahi/` (`kelas`, `tes`, `ebook`).

### 6.2 API Routing (`routes/api.php` — 505 lines)

API routes provide endpoints consumed primarily by mobile applications or decoupled clients (**FACT**):

1. **Unauthenticated API Routes:**
   - `POST api/login`, `POST api/register`, `GET api/home`, `GET api/course`, `GET api/faq`, `GET api/payment_gateway`.
2. **Passport Authenticated API Routes (`auth:api`):**
   - User profile management, wishlist manipulation, cart items, order history, course lecture watching, class progress updates, quiz submissions, wallet details, and affiliate links.
3. **Module API Endpoints:**
   - Endpoints defined for homework (`/homework`, `/submithomework`), resumes (`/create/resumes`), and forums (`/addforumscategory`) routed to `App\Http\Controllers\Api\OtherApiController`. (Reachability dependent on missing module classes; see Section 16).

### 6.3 Key Custom Middleware

| Middleware Class | File Path | Inspected Logic & Behavior | Classification |
|---|---|---|---|
| `IsAdmin` | `app/Http/Middleware/IsAdmin.php:20` | Checks if authenticated user has any role other than `'user'`: `Auth::user()->roles()->where('name', '!=', 'user')->exists()`. If only `'user'`, redirects to home with 401. | **FACT** |
| `AdminIntructor` | `app/Http/Middleware/AdminIntructor.php:21` | Checks if user possesses either `'admin'` or `'instructor'` role via Spatie `hasAnyRole(['admin', 'instructor'])`. | **FACT** |
| `IsVerified` | `app/Http/Middleware/IsVerified.php:22` | If `Setting.verify_enable == 1`, verifies user email is verified; redirects to verification prompt if unverified. | **FACT** |
| `IsActive` | `app/Http/Middleware/IsActive.php:20` | Reads plain-text file `public/config.txt`. If content is not `'1'`, aborts or redirects to installation/activation page. | **FACT** |
| `Google2FAAuthenticator` | `app/Http/Middleware/Google2FAAuthenticator.php:18` | Intercepts session; enforces Google Authenticator 2FA verification if configured for the user. | **FACT** |
| `CheckReferral` | `app/Http/Middleware/CheckReferral.php:20` | Web middleware group; checks query parameter `?ref=`; stores referral affiliate code in cookie `referral` for 30 days. | **FACT** |
| `MaintananceMode` | `app/Http/Middleware/MaintananceMode.php:20` | Checks `Setting.maintenance_mode == 1`; redirects non-admin users to maintenance screen. | **FACT** |
| `HandleInertiaRequests`| `app/Http/Middleware/HandleInertiaRequests.php` | Configured in web group; defines shared Inertia view props (`auth`, `flash`, `currency`). | **FACT** |

---

## 7. User Roles & Authorization

### 7.1 Authorization Model & Implementation Inconsistency (REV-009 Analysis)

The application incorporates **Spatie Laravel Permission** as its primary authorization library, but exhibits an **Implementation Inconsistency / Dual Tracking Pattern** (**DERIVED** from code inspection):

1. **Spatie Permission RBAC:**
   - Model `app/User.php:21` utilizes trait `Spatie\Permission\Traits\HasRoles`.
   - Core roles defined in seeders and migrations: `admin`, `instructor`, `user`.
   - Role checks using Spatie methods occur in `LoginController.php:136` (`$user->hasRole('admin')`), `AdminIntructor.php:21` (`hasAnyRole(...)`), and Blade directives (`@hasrole`).
2. **Database String Column `users.role`:**
   - The table `users` contains a varchar column `role` (`analysis/legacy-schema-snapshot.md:6630`).
   - Multiple legacy controllers check role directly against this string:
     - `app/Http/Controllers/AdminController.php:51`: `if(Auth::User()->role == "admin")`
     - `app/Http/Controllers/InstructorController.php:35`: `if(Auth::User()->role == "instructor")`
     - `app/Http/Controllers/WatchController.php:96`: `if(Auth::User()->role == "admin")`
     - `app/Http/Controllers/OrderStoreController.php:177`: `if($cart->courses->user->role == "instructor")`

**Classification: IMPLEMENTATION INCONSISTENCY (INC-001).** Both authorization mechanisms operate concurrently without database-enforced synchronization. While not a contradictory conflict of physical facts, it represents an architectural divergence that requires careful normalization in any target system.

### 7.2 Granular Permissions

Inspected permissions registered in database migrations and policies include:
- `courses.view`, `courses.create`, `courses.edit`, `courses.delete`
- `certificate.manage`, `dashboard.manage`, `report.progress-report.manage`, `ebooks-category.manage`

---

## 8. Authentication Mechanisms

### 8.1 Web Session Authentication

- **Primary Authentication:** Email and password authentication handled by `app/Http/Controllers/Auth/LoginController.php` using standard Laravel `AuthenticatesUsers` trait.
- **Login Credentials Validation:** Validates `email` (required, string, email) and `password` (required, string).
- **Post-Login Routing (`LoginController@authenticated`):**
  - If `user.status == 1`:
    - Admin (`hasRole('admin')`) → redirects to `admin.index`.
    - Instructor (`hasRole('instructor')`) → redirects to `instructor.index`.
    - Other custom roles → redirects to `admin.index`.
    - Student/Default → redirects to `/`.
  - If `user.status != 1`: Logs user out immediately and redirects with message "You are deactivated!".
- **Social Login:** Configured via `laravel/socialite` for Google, Facebook, Amazon, GitLab, LinkedIn, Twitter (`routes/web.php:73-77`).
  - *Dead Code Finding:* `LoginController@handleProviderCallback` lines 244–251 contain confirmed unreachable code following an unconditional return in the preceding `if/else` block (see Section 19, `DEAD-001`).
- **Two-Factor Authentication:** Google 2FA integrated via `pragmarx/google2fa-laravel`; enabled per-user via `users.google2fa_secret`.
- **OTP Authentication:** Routes defined in `routes/web.php:68-71` (`/otp/login`, `/otp/verify`); service `app/Services/OTPService.php` exists. View rendering in `LoginController@showLoginForm` is commented out; activation state is **UNKNOWN**.

### 8.2 API Authentication

- Handled via **Laravel Passport** OAuth2 bearer tokens.
- Guards defined in `config/auth.php:44-47`: guard `api` uses driver `passport` and provider `users`.
- Endpoints `POST api/login` and `POST api/register` issue Personal Access Tokens.

---

## 9. Major Modules & Features Inventory (REV-001, REV-002, REV-011)

To prevent overbroad claims, each module is documented with its verified structural components, observed behavior, granular file/schema references, and current reachability status.

### 9.1 Course Management

- **Structural Components (FACT):**
  - Models: `app/Course.php`, `app/CourseChapter.php`, `app/CourseClass.php`, `app/WhatLearn.php`, `app/CourseInclude.php`, `app/RelatedCourse.php`.
  - Controllers: `app/Http/Controllers/CourseController.php`, `app/Http/Controllers/CourseChapterController.php`, `app/Http/Controllers/CourseClassController.php`.
  - Database Tables: `courses`, `course_chapters`, `course_classes`, `what_learns`, `course_includes`, `related_courses`.
  - Routes: `routes/web.php:643-645` (`Route::resource('course', 'CourseController')`, etc.).
- **Observed Behavior (DERIVED):**
  - Supports Free and Paid courses (`courses.type`). Multi-lingual translatable fields (`title`, `short_detail`, `detail`, `requirement`) handled by Spatie Translatable.
  - Hierarchical structure: `Course` has many `CourseChapter` (with drip scheduling), which has many `CourseClass` (video, audio, PDF, zip, text).
  - Admin approval workflow implemented via `courses.status` flag and rejection logging in `courserejects` table.
- **Reachability: REACHABLE.** Fully active across web routes and admin dashboards.

### 9.2 Enrollment & Order Processing

- **Structural Components (FACT):**
  - Models: `app/Order.php`, `app/Cart.php`, `app/PendingPayout.php`, `app/InstructorSetting.php`.
  - Controllers: `app/Http/Controllers/EnrollmentController.php`, `app/Http/Controllers/OrderStoreController.php`, `app/Http/Controllers/OrderController.php`.
  - Database Tables: `orders`, `carts`, `pending_payouts`, `instructor_settings`.
  - Routes: `routes/web.php:838` (`GET enroll/show/{id}`), `routes/web.php:651` (`Route::resource('order', 'OrderController')`).
- **Observed Behavior (DERIVED):**
  - Free enrollment bypasses cart and executes raw insert into `orders` via `EnrollmentController@enroll`.
  - Paid orders process through `OrderStoreController@orderstore`, which calculates instructor revenue share, creates `Order` with generated serial number `#00000001`, clears cart and wishlist, logs `PendingPayout`, dispatches Twilio SMS, and sends order confirmation emails.
- **Data Model Inconsistency (INC-002):** `orders.total_amount` is defined as `varchar(191)` in schema, but code performs floating-point rounding and arithmetic (`Order::boot()` rounds value).
- **Reachability: REACHABLE.** Core revenue and enrollment pipeline.

### 9.3 Shopping Cart & Checkout

- **Structural Components (FACT):**
  - Models: `app/Cart.php`, `app/UserCurrency.php`, `app/Currency.php`.
  - Controllers: `app/Http/Controllers/CartController.php`.
  - Database Tables: `carts`, `user_currencies`, `currencies`.
  - Routes: `routes/web.php:842-848` (`GET cart`, `POST addtocart`, `POST removefromcart`).
- **Observed Behavior (DERIVED):**
  - Stores items for courses (`type=0`) and bundles (`type=1`). Supports guest sessions and multi-currency pricing conversion via `torann/currency`.
- **Reachability: REACHABLE.**

### 9.4 Quiz & Assessment

- **Structural Components (FACT):**
  - Models: `app/QuizTopic.php`, `app/Quiz.php`, `app/QuizAnswer.php`.
  - Controllers: `app/Http/Controllers/QuizTopicController.php`, `app/Http/Controllers/QuizController.php`, `app/Http/Controllers/QuizStartController.php`.
  - Database Tables: `quiz_topics`, `quiz_questions`, `quiz_answers`.
  - Routes: `routes/web.php:646-648` (Admin CRUD), `routes/web.php:908-910` (`start_quiz/{id}`, `finish/{id}`).
- **Observed Behavior (DERIVED):**
  - Quizzes belong to courses; support per-question marks, pass percentages, timers, and retry rules.
  - Evaluation in `QuizStartController@show` calculates student score by comparing `QuizAnswer.user_answer` to `QuizAnswer.answer`.
- **Reachability: REACHABLE.**

### 9.5 Assignments

- **Structural Components (FACT):**
  - Models: `app/Assignment.php`.
  - Controllers: `app/Http/Controllers/AssignmentController.php`.
  - Database Tables: `assignments`.
  - Routes: `routes/web.php:655` (`Route::resource('assignment', 'AssignmentController')`).
- **Observed Behavior (DERIVED):**
  - Instructors post assignments linked to course chapters; students submit files; instructors review and assign ratings.
- **Reachability: REACHABLE.**

### 9.6 Certificates

- **Structural Components (FACT):**
  - Models: `app/CourseProgress.php`, `app/Certificate.php`, `app/Setting.php`.
  - Controllers: `app/Http/Controllers/CertificateController.php`, `app/Http/Controllers/PdfController.php`.
  - Database Tables: `certificates`, `course_progress`.
  - Routes: `routes/web.php:918` (`GET certificate/{slug}`), `routes/web.php:920` (`GET certificate/download/{slug}`).
- **Observed Behavior (DERIVED):**
  - Certificates are derived directly from course completion. Serial format: `{progress_id}CR-{uniqid}`.
  - Renders HTML preview or triggers PDF download via `niklasravnsborg/laravel-pdf`.
- **Reachability: REACHABLE.**

### 9.7 Course Progress Tracking

- **Structural Components (FACT):**
  - Models: `app/CourseProgress.php`, `app/CourseChapter.php`, `app/CourseClass.php`.
  - Controllers: `app/Http/Controllers/CourseProgressController.php`.
  - Database Tables: `course_progress`.
  - Routes: `routes/web.php:925-927` (`GET course/checked/{course_id}/{class_id}`, `POST course/checked/{id}`).
- **Observed Behavior (DERIVED):**
  - Stores completed IDs as JSON arrays in `mark_chapter_id` and `mark_class_id`.
  - Enforces sequential progression: `checkedCourse` verifies the requested class matches the next incomplete class; otherwise returns 403 Forbidden ("Class is locked").
- **Reachability: REACHABLE.**

### 9.8 Reviews & Ratings

- **Structural Components (FACT):**
  - Models: `app/ReviewRating.php`, `app/ReviewHelpful.php`.
  - Controllers: `app/Http/Controllers/ReviewRatingController.php`.
  - Database Tables: `review_ratings`, `review_helpfuls`.
  - Routes: `routes/web.php:852` (`POST course/review/{id}`).
- **Observed Behavior (DERIVED):**
  - Captures 3 distinct rating dimensions: `learn`, `price`, `value` alongside text feedback. Requires admin moderation if configured.
- **Reachability: REACHABLE.**

### 9.9 Bundle Courses

- **Structural Components (FACT):**
  - Models: `app/BundleCourse.php`.
  - Controllers: `app/Http/Controllers/BundleCourseController.php`.
  - Database Tables: `bundle_courses`.
  - Routes: `routes/web.php:652` (`Route::resource('bundle', 'BundleCourseController')`).
- **Observed Behavior (DERIVED):**
  - Bundles package multiple course IDs stored as JSON arrays (`course_id` column); supports fixed subscription billing periods.
- **Reachability: REACHABLE.**

### 9.10 Live Meetings

- **Structural Components (FACT):**
  - Models: `app/Meeting.php` (Zoom), `app/BBL.php` (BigBlueButton), `app/JitsiMeeting.php`, `app/Googlemeet.php`, `app/PaidMettings.php`.
  - Controllers: `app/Http/Controllers/ZoomController.php`, `app/Http/Controllers/BigBlueController.php`, `app/Http/Controllers/JitsiController.php`, `app/Http/Controllers/GoogleMeetController.php`.
  - Database Tables: `meetings`, `b_b_l_s`, `jitsi_meetings`, `googlemeets`, `paid_mettings`.
  - Routes: `routes/web.php:657-659` (Zoom, BBB, Jitsi, Meet management).
- **Observed Behavior (DERIVED):**
  - Supports scheduling live classes and paid meeting sessions recorded in `paid_mettings`.
- **Reachability: CONFIG-DEPENDENT.** Each provider requires third-party API credentials.

### 9.11 Blog

- **Structural Components (FACT):**
  - Models: `app/Blog.php`.
  - Controllers: `app/Http/Controllers/BlogController.php`.
  - Database Tables: `blogs`.
  - Routes: `routes/web.php:650` (`Route::resource('blog', 'BlogController')`).
- **Reachability: REACHABLE.**

### 9.12 Wallet System

- **Structural Components (FACT):**
  - Models: `app/Wallet.php`, `app/WalletSettings.php`, `app/WalletTransactions.php`.
  - Controllers: `app/Http/Controllers/WalletController.php`, `app/Http/Controllers/WalletPaymentController.php`, `app/Http/Controllers/WalletSettingController.php`.
  - Database Tables: `wallet`, `wallet_settings`, `wallet_transactions`.
  - Routes: `routes/web.php:462-465` (Admin settings/transactions), `routes/web.php:1061-1071` (User wallet dashboard, checkout, PayPal/Paytm/Stripe deposit, payment); `routes/api.php:174-175, 361`.
- **Observed Behavior (DERIVED):**
  - Tracks user balances; allows topping up balance via PayPal, Paytm, or Stripe; allows students to pay for courses using wallet balance via `WalletPaymentController@walletpayment`.
- **Reachability: REACHABLE.**

### 9.13 Affiliate / Referral Program

- **Structural Components (FACT):**
  - Models: `app/Affiliate.php`.
  - Controllers: `app/Http/Controllers/AffiliateController.php`.
  - Middleware: `app/Http/Middleware/CheckReferral.php`.
  - Jobs: `app/Jobs/AffiliatesPoints.php`.
  - Database Tables: `affiliate`, `users.affiliate_id`, `users.referred_by`.
  - Routes: `routes/web.php:468-469` (Admin config), `routes/web.php:1074-1075` (Generate/get link); `routes/api.php:178`.
- **Observed Behavior (DERIVED):**
  - URL referrals tracked via cookies; new registrations record referrer; points credited to wallet balance.
- **Reachability: REACHABLE.** Runtime qualifier: **PARTIAL RUNTIME RISK**. Cookie and link tracking are reachable; background point crediting job has an authenticated session dependency (see Section 12).

### 9.14 Instructor Payout Management

- **Structural Components (FACT):**
  - Models: `app/PendingPayout.php`, `app/CompletedPayout.php`, `app/InstructorSetting.php`.
  - Controllers: `app/Http/Controllers/PayoutController.php`.
  - Database Tables: `pending_payouts`, `completed_payouts`, `instructor_settings`.
  - Routes: `routes/web.php:424-428` (`admin/payout/*`).
- **Observed Behavior (DERIVED):**
  - Orders automatically create `PendingPayout` records based on configured revenue split percentages. Admin reviews and marks payouts as completed via bank transfer, PayPal, or Paytm.
- **Reachability: REACHABLE.**

### 9.15 E-Book Module

- **Structural Components (FACT):**
  - Models: `app/Ebook.php`.
  - Controllers: `app/Http/Controllers/CategoryController.php` (contains `namespace Modules\Ebook\Http\Controllers;`).
  - Database Tables: `ebooks`.
  - Configuration: `"Ebook": true` in `modules_statuses.json`.
- **Reachability: UNKNOWN.** Runtime qualifier: **BROKEN DEPENDENCY**. Directory `Modules/Ebook` is missing; model `Modules\Ebook\Models\EbookCategory` is referenced but absent from repository.

### 9.16 Forum & Discussion Module

- **Structural Components (FACT):**
  - Database Tables: `forums_categories`, `forum_topics`, `forum_comments`.
  - Setting Columns: `setting.forum_enable`.
  - API Routes: `routes/api.php:214-217` (`/addforumscategory`, `/listforumscategory`, `/addforums`).
  - API Controller: `app/Http/Controllers/Api/OtherApiController.php:1050-1120`.
  - Configuration: `"Forum": true` in `modules_statuses.json`.
- **Reachability: UNKNOWN.** Runtime qualifier: **BROKEN DEPENDENCY**. Dedicated `Modules/Forum` directory is missing; web controllers not found in `app/Http/Controllers`.

### 9.17 Homework Module

- **Structural Components (FACT):**
  - Database Tables: `homework`, `submit_homework`.
  - API Routes: `routes/api.php:208-211` (`POST /homework`, `POST /submithomework`, `GET /gethomework/{id}`).
  - API Controller: `app/Http/Controllers/Api/OtherApiController.php:793-870`.
  - Configuration: `"Homework": true` in `modules_statuses.json`.
- **Reachability: UNKNOWN.** Runtime qualifier: **BROKEN DEPENDENCY**. `OtherApiController` imports `Modules\Homework\Models\Homework`. Because `Modules/` does not exist on disk, invoking this API fails at runtime with class not found.

### 9.18 Chatboard Module

- **Structural Components (FACT):**
  - Database Tables: `chats`.
  - Setting Columns: `setting.chat_bubble`.
  - Controller: `app/Http/Controllers/ChatgptController.php` (AI chat integration).
  - Configuration: `"Chatboard": true` in `modules_statuses.json`.
- **Reachability: UNKNOWN.** Runtime qualifier: **BROKEN DEPENDENCY**. Dedicated module folder `Modules/Chatboard` is missing.

### 9.19 Resume / Job Portal Module

- **Structural Components (FACT):**
  - Database Tables: `acedemics`, `applyjobs`, `jobsettings`, `personalinfos`, `postjobs`, `workexps`.
  - Models: `app/Jobcategory.php`.
  - Controllers: `app/Http/Controllers/JobcategoryController.php`, `app/Http/Controllers/Api/OtherApiController.php:910-1040`.
  - API Routes: `routes/api.php:183-186, 499` (`/create/resumes`, `/resume/download/{user_id}`).
  - Configuration: `"Resume": true` in `modules_statuses.json`.
- **Reachability: UNKNOWN.** Runtime qualifier: **BROKEN DEPENDENCY**. Schema and API routes exist; however, `OtherApiController` imports `Modules\Resume\Models\...`, which fails on execution due to missing `Modules/` directory.

### 9.20 Subscriptions & Instructor Plans

- **Structural Components (FACT):**
  - Models: `app/PlanSubscribe.php`, `app/InstructorPlan.php`.
  - Controllers: `app/Http/Controllers/StripeController.php`, `app/Http/Controllers/SubscribedOrdersController.php`.
  - Database Tables: `plan_subscribes`, `instructor_plans`.
  - Routes: `routes/web.php:436` (`orders/subscription`).
- **Reachability: REACHABLE.** Configuration qualifier: **CONFIG-DEPENDENT**.

### 9.21 Additional Utility Features (Granular Traceability)

| Feature | Model | Controller | Schema Table | Route Reference | Reachability |
|---|---|---|---|---|---|
| Coupons | `app/Coupon.php` | `CouponController.php` | `coupons` | `web.php:666` (`coupon`) | **REACHABLE** |
| Notifications | `app/Notifications/*.php` | `NotificationController.php` | `notifications` | `web.php:850` (`notifications`) | **REACHABLE** |
| Support Tickets | `app/AdminSupport.php`, `SupportType.php` | `AdminSupportController.php`, `SupportController.php` | `admin_supports`, `support_types` | `web.php:656` (`admin/support`) | **REACHABLE** |
| Pages / CMS | `app/Page.php` | `PageController.php` | `pages` | `web.php:661` (`page`) | **REACHABLE** |
| Flash Sales | `app/FlashSale.php` | `FlashSaleController.php` | `flash_sales` | `web.php:662` (`flash-sales`) | **REACHABLE** |
| Attendance | `app/Attandance.php` | `AttandanceController.php` | `attandance` | `web.php:413-416`, `api.php:481` | **REACHABLE** (Auto-logged during class playback; see Section 11.4) |
| Watch Course Device Limit | `app/WatchCourse.php` | `WatchCourseController.php`, `WatchController.php` | `watch_courses` | `web.php:944-947` | **REACHABLE** |
| Course Comparison | `app/Compare.php` | `CompareController.php` | `compares` | `web.php:856` (`compare`) | **REACHABLE** |
| Wishlist | `app/Wishlist.php` | `WishlistController.php` | `wishlists` | `web.php:849` (`wishlist`) | **REACHABLE** |

---

## 10. Data Architecture & Relational Snapshot

### 10.1 Key Conceptual Entity Relationships

```
User (users)
  ├── 1:N ──► Course (as instructor_id)
  ├── 1:N ──► Order (as student user_id)
  ├── 1:N ──► ReviewRating, Assignment, Blog, Wishlist, Cart
  ├── 1:N ──► PendingPayout, CompletedPayout
  ├── 1:1 ──► Wallet
  └── N:M ──► Roles & Permissions (via Spatie model_has_roles)

Course (courses)
  ├── N:1 ──► User (instructor), Categories, CourseLanguage
  ├── 1:N ──► CourseChapter (ordered sequence)
  │             └── 1:N ──► CourseClass (lectures / media / files)
  ├── 1:N ──► QuizTopic
  │             └── 1:N ──► Quiz (questions) ──► 1:N ──► QuizAnswer
  ├── 1:N ──► Order, ReviewRating, Assignment, WhatLearn, CourseInclude
  └── 1:N ──► CourseProgress ──► 1:1 ──► Certificate

Order (orders)
  ├── N:1 ──► User (student)
  ├── N:1 ──► Course (or BundleCourse)
  └── 1:N ──► PendingPayout (if instructor revenue share applicable)
```

### 10.2 Relational Integrity Deficit: Zero Foreign Keys

**Forensic Finding: FACT.** Analysis of `analysis/legacy-schema-snapshot.md` verifies that **none of the 175 tables possess database-level foreign key constraints (`FOREIGN KEY ... REFERENCES ...`)**.

- Referential integrity is managed exclusively within PHP application logic (Eloquent relationships or raw DB facade statements).
- Deleting parent records relies entirely on application-level cascades or leaves orphan rows in dependent tables (`course_chapters`, `course_classes`, `orders`, `quiz_answers`).

---

## 11. Core Execution Flow Reconstructions (REV-006 Revision)

The following core workflows have been forensically reconstructed across the 12 execution-flow dimensions mandated by governance contracts.

### 11.1 Web User Authentication & Session Establishment

1. **Trigger:** User submits web login credentials.
2. **Entry Point:** `App\Http\Controllers\Auth\LoginController@login`.
3. **Route / Caller:** `POST /login` (route `login.post`).
4. **Middleware / Auth Boundary:** Web middleware group (`EncryptCookies`, `StartSession`, `ShareErrorsFromSession`, `VerifyCsrfToken`). Publicly accessible.
5. **Controller / Component:** `LoginController` using `AuthenticatesUsers` trait.
6. **Validation:** `validateLogin($request)` validates `email` (required, string, email) and `password` (required, string).
7. **Decision / Branching:**
   - Invokes `Auth::attempt($credentials, $remember)`.
   - If invalid credentials, calls `sendFailedLoginResponse()` → redirects back with error bag `trans('auth.failed')`.
   - If valid credentials, invokes `authenticated($request, $user)`.
8. **Data Read / Write:**
   - Reads: `users` table via `Auth::attempt()`; reads `Setting::first()`.
   - Writes: Writes activity log to `activity_log` table if `Setting.activity_enable == 1`.
9. **Dependencies:** `Illuminate\Support\Facades\Auth`, `Spatie\Activitylog`, `App\Setting`.
10. **Side Effects:** Writes Laravel session cookie; records audit log entry.
11. **Success / Stop Condition:**
    - If `user.status == 1`: Evaluates Spatie roles. If `hasRole('admin')`, redirects to `route('admin.index')`; if `hasRole('instructor')`, redirects to `route('instructor.index')`; else redirects to `/`.
12. **Error / Failure Branch:**
    - If `user.status != 1`: Calls `Auth::logout()`, destroys session, and redirects to `login` with flash message `'You are deactivated!'`.

### 11.2 Free Course Enrollment Flow

1. **Trigger:** Student clicks "Enroll Now" on a free course.
2. **Entry Point:** `App\Http\Controllers\EnrollmentController@enroll`.
3. **Route / Caller:** `GET enroll/show/{id}` (route `show.enroll`).
4. **Middleware / Auth Boundary:** Protected by `auth` middleware group (`routes/web.php:838`).
5. **Controller / Component:** `EnrollmentController`.
6. **Validation:** Implicit course lookup: `$course = Course::where('id', $id)->first()`. No duplicate enrollment verification is performed before insert.
7. **Decision / Branching:** Direct execution path without conditional branches.
8. **Data Read / Write:**
   - Reads: `Course::where('id', $id)->first()`.
   - Writes: Direct insert via DB facade:
     ```php
     DB::table('orders')->insert([
         'user_id' => Auth::User()->id,
         'instructor_id' => $course->user_id,
         'course_id' => $id,
         'total_amount' => 'Free',
         'created_at'  => Carbon::now()->toDateTimeString(),
     ]);
     ```
9. **Dependencies:** `Illuminate\Support\Facades\DB`, `Illuminate\Support\Facades\Auth`, `Carbon\Carbon`, `App\Course`.
10. **Side Effects:** Inserts order record directly into `orders` table. Bypasses cart, payment gateways, invoice emails, and payout generation.
11. **Success / Stop Condition:** Redirects `back()->with('success', trans('flash.EnrolledSuccessfully'))`.
12. **Error / Failure Branch:** If course ID does not exist, `$course` evaluates to null, triggering an unhandled fatal null-property access on `$course->user_id`.

### 11.3 Paid Course Order & Checkout Processing

1. **Trigger:** Payment gateway callback / webhook triggers successful payment verification.
2. **Entry Point:** Gateway controller callback (e.g. `StripePaymentController@stripePost`, `PayPalController@getPaymentStatus`, `RazorpayController@payment`).
3. **Route / Caller:** Gateway return routes in `routes/web.php` (e.g. `POST /stripe/post`, `POST /order/payment`).
4. **Middleware / Auth Boundary:** Authenticated user session (`auth` middleware).
5. **Controller / Component:** Gateway controller creates an instance of `OrderStoreController` and invokes method `orderstore($txn_id, $payment_method, ...)`.
6. **Validation:** Validates existence of user cart items (`Cart::where('user_id', Auth::id())->get()`) or session meeting details (`meeting_id`, `meeting_type`).
7. **Decision / Branching:**
   - If session contains `one_order_course` and `one_order_user`, branches to `$this->oneorder(...)`.
   - If session contains `meeting_id` and `meeting_type`, processes paid live meeting entry in `paid_mettings` and forgets session keys.
   - Iterates through each cart item:
     - If `$cart->type == 1` (Bundle Course): resolves bundle duration and bundle courses.
     - If `$cart->type == 0` (Single Course): computes course duration, checks `InstructorSetting` or `courses.instructor_revenue`, and computes instructor payout percentage.
8. **Data Read / Write:**
   - Reads: `Setting::first()`, `UserCurrency`, `Currency::where('default', 1)`, `Cart`, `Order::orderBy('created_at', 'desc')->first()`.
   - Writes:
     - Inserts record into `orders` with auto-incremented string order ID formatted as `#' . sprintf("%08d", intval($number) + 1)`.
     - Deletes item from `wishlists` table: `Wishlist::where('user_id', ...)->where('course_id', ...)->delete()`.
     - Clears user shopping cart: `Cart::where('user_id', Auth::id())->delete()`.
     - If instructor payout > 0 and course instructor has role `'instructor'`, inserts record into `pending_payouts` table.
9. **Dependencies:** `App\Order`, `App\Cart`, `App\PendingPayout`, `App\InstructorSetting`, `App\Helpers\TwilioMsg`, `Illuminate\Support\Facades\Mail`.
10. **Side Effects:**
    - If `Setting.twilio_enable == '1'`, sends SMS notification via Twilio (catches and suppresses any thrown exceptions).
    - If `MAIL_USERNAME` is configured in environment, dispatches `SendOrderMail` to student and `AdminMailOnOrder` to instructor/admin (catches `Swift_TransportException`).
    - Dispatches in-app database notification to instructor (`Notification::send($user, new UserEnroll($course))`).
11. **Success / Stop Condition:** Redirects user to order confirmation page (`route('confirmation')` or purchase invoice).
12. **Error / Failure Branch:** If gateway transaction fails, gateway controller aborts or redirects back with error messages prior to calling `orderstore`. Swift transport and Twilio exceptions during order storage are caught and suppressed to prevent rolling back order creation.

### 11.4 Course Content Access & Automatic Attendance Recording

1. **Trigger:** Enrolled student accesses course playback page.
2. **Entry Point:** `App\Http\Controllers\WatchController@watchOld` (or `@watch`).
3. **Route / Caller:** `GET watch/course/{id}` (route `watchcourse`).
4. **Middleware / Auth Boundary:** Authenticated user check via `Auth::check()`.
5. **Controller / Component:** `WatchController`.
6. **Validation:** Checks if user is authenticated; retrieves order record:
   `Order::where('status', '1')->where('user_id', Auth::id())->where('course_id', $id)->first()`.
7. **Decision / Branching:**
   - If user is admin (`Auth::user()->role == "admin"`) or course instructor (`Auth::id() == $course->user_id`), access is granted immediately.
   - If student has an active order (`!empty($order)`), access is granted.
   - If no valid order exists, access is refused.
8. **Data Read / Write:**
   - Reads: `Course::findOrFail($id)`, `Order`, `Setting::first()`.
   - Writes (Automatic Attendance Side Effect):
     - If `Setting.attandance_enable == 1`, queries `Attandance::where('course_id', $id)->where('user_id', Auth::id())->where('date', today)->first()`.
     - If no attendance record exists for current date, automatically creates record in `attandance` table:
       ```php
       Attandance::create([
           'user_id' => Auth::id(),
           'course_id' => $id,
           'instructor_id' => $courses->user_id,
           'date' => Carbon::now()->toDateString(),
           'order_id' => $id,
       ]);
       ```
   - Writes (Device Limit Enforcement): If `Setting.device_control == 1`, creates a record in `watch_courses` tracking active viewing sessions.
9. **Dependencies:** `App\Course`, `App\Order`, `App\Attandance`, `App\WatchCourse`, `App\Setting`, `Carbon\Carbon`.
10. **Side Effects:** Daily attendance auto-inserted; active viewing device registered.
11. **Success / Stop Condition:** Traverses chapters and classes, identifies initial video/audio playback index, and renders Blade view `watch.blade.php`.
12. **Error / Failure Branch:** Unauthenticated or unauthorized users are redirected back with flash alert.

### 11.5 Course Class Progress Tracking & Sequential Locking

1. **Trigger:** Student completes watching a class lecture or clicks completion mark.
2. **Entry Point:** `App\Http\Controllers\CourseProgressController@checkedCourse`.
3. **Route / Caller:** `GET course/checked/{course_id}/{class_id}`.
4. **Middleware / Auth Boundary:** Custom check `is_logged_in()`; returns 401 JSON if unauthenticated.
5. **Controller / Component:** `CourseProgressController`.
6. **Validation:** Verifies course exists via `Course::with(['progress', 'chapter', 'courseclass'])->find($course_id)`. Returns 404 if not found.
7. **Decision / Branching (Sequential Enforcement):**
   - Retrieves list of all active class IDs in position order: `$allClassIds`.
   - Inspects existing user progress: `$markClassIds`.
   - Computes expected next class: `$nextClassId = $allClassIds->diff($markClassIds)->first()`.
   - If `$markClassIds->contains($class_id)`: returns 200 JSON (`{"success": true, "message": "Already completed"}`).
   - If `$class_id != $nextClassId`: returns 403 Forbidden JSON (`{"success": false, "message": "Class is locked"}`).
8. **Data Read / Write:**
   - Reads: `courses`, `course_chapters`, `course_classes`, `course_progress`.
   - Writes: Updates `course_progress` record: appends `$class_id` to array `$progress->mark_class_id`, saves chapter and class ID snapshot arrays (`all_chapter_id`, `all_class_id`).
9. **Dependencies:** `App\CourseProgress`, `App\Course`, `App\CourseClass`.
10. **Side Effects:** Updates progress record in database.
11. **Success / Stop Condition:** Returns 200 JSON (`{"success": true, "message": "Class completed"}`).
12. **Error / Failure Branch:** Database save failure returns 500 JSON.

### 11.6 Quiz Examination & Assessment Evaluation

1. **Trigger:** Student begins quiz on a course topic.
2. **Entry Point:** `App\Http\Controllers\QuizStartController@quizstart`.
3. **Route / Caller:** `GET start_quiz/{id}` (route `start_quiz`). Form submission enters `POST /start_quiz/store/{id}` (route `start.quiz.store`).
4. **Middleware / Auth Boundary:** Authenticated user session (`auth` group).
5. **Controller / Component:** `QuizStartController`.
6. **Validation:** Checks if student has already completed quiz topic:
   `QuizAnswer::where('user_id', Auth::id())->where('topic_id', $id)->first()`.
7. **Decision / Branching:**
   - In `store()`: If `$quiz_already != null`, duplicate submission is ignored and execution skips answer storage.
   - If not previously submitted, loops through submitted answers: verifies question hasn't already been answered, maps submitted `user_answer` and correct `answer`, and constructs `$answers[]` payload.
8. **Data Read / Write:**
   - Reads: `QuizTopic::findOrFail($id)`, `Quiz::where('topic_id', $id)->get()`.
   - Writes: Batch insert into database: `QuizAnswer::insert($answers)`.
9. **Dependencies:** `App\QuizTopic`, `App\Quiz`, `App\QuizAnswer`, `Carbon\Carbon`.
10. **Side Effects:** Stores user responses in `quiz_answers` table.
11. **Success / Stop Condition:** Redirects to `route('start.quiz.show', $id)`. Method `show($id)` fetches all student answers for topic, counts matching answers where `$answer->answer == $answer->user_answer`, calculates score against `per_q_mark`, and displays results view `front.quiz.finish`.
12. **Error / Failure Branch:** Missing topic throws 404 ModelNotFoundException.

### 11.7 Certificate Generation & Verification

1. **Trigger:** Student views or downloads completed course certificate, or public verifier checks certificate validity.
2. **Entry Point:** `App\Http\Controllers\CertificateController@show` (web view) or `@pdfdownload` (PDF generation).
3. **Route / Caller:** `GET certificate/{slug}` (route `certificate.show`) or `GET certificate/download/{slug}` (route `certificate.download`).
4. **Middleware / Auth Boundary:** Publicly reachable route (allows public certificate verification).
5. **Controller / Component:** `CertificateController`.
6. **Validation:** Extracts progress ID from slug using string tokenization:
   `$whatIWant = strtok($slug, 'CR-');`
   Retrieves progress record: `CourseProgress::where('id', $whatIWant)->firstOrFail()`.
7. **Decision / Branching:** Checks `Setting.theme`. If theme 1, renders `front.certificate.certificate`; otherwise renders `theme_2.front.certificate.certificate`.
8. **Data Read / Write:**
   - Reads: `CourseProgress`, `Course`, `Setting::first()`.
   - Writes: None (read-only document rendering).
9. **Dependencies:** `App\CourseProgress`, `App\Course`, `niklasravnsborg\LaravelPdf\Facades\Pdf`.
10. **Side Effects:** Renders HTML or compiles binary PDF document stream.
11. **Success / Stop Condition:**
    - Web view: Displays styled certificate with course name, completion date, student name, and serial number.
    - PDF download: Returns `$pdf->download('certificate.pdf')` with landscape orientation (`'orientation' => 'L'`).
12. **Error / Failure Branch:** Invalid certificate slug or missing progress record triggers 404 abort.

---

## 12. Background & Scheduled Processing (REV-008 Revision)

### 12.1 Custom Queue Jobs

The application defines 3 queue job classes under `app/Jobs/` (**FACT**):

| Job Class | Inspected Purpose | Code Observation & Runtime Analysis |
|---|---|---|
| `App\Jobs\EnrollExpire` | Deletes expired orders from `orders` table | **Code Observation (FACT):** Line 37 executes: `foreach (Auth::user()->orders as $order) { ... }`. Lines 43 executes: `DB::table('orders')->where('enroll_expire', '<', $todayDate)->delete();`.<br>**Derived Architectural Analysis (DERIVED):** The code creates a direct dependency on an authenticated session context (`Auth::user()`). When executed in a standard asynchronous background worker (`php artisan queue:work`), no HTTP session exists, causing `Auth::user()` to return `null` and triggering a fatal null-property access error.<br>**Production Operational Status (UNKNOWN):** No dispatch call was found in scheduled commands. Whether this job is dispatched synchronously from web requests or executed via worker is unknown without production runtime logs. |
| `App\Jobs\AffiliatesPoints` | Credits referral wallet balance | **Code Observation (FACT):** Line 37 executes: `if(Auth::user()->wallet->status == 1)`. Line 46 updates wallet balance using `Auth::user()->id`.<br>**Derived Architectural Analysis (DERIVED):** Exactly mirrors the authenticated session dependency observed in `EnrollExpire`.<br>**Production Operational Status (UNKNOWN):** Whether referrals trigger this job synchronously or asynchronously in production is unknown. |
| `App\Jobs\InstructorPlan` | Instructor subscription plan handling | **Code Observation (FACT):** Job class exists in filesystem.<br>**Production Operational Status (UNKNOWN):** Internal logic not fully mapped; dispatch triggers unverified. |

### 12.2 Custom Artisan Commands

The repository defines 7 custom console commands in `app/Console/Commands/` (**FACT**):
- `DatabaseBackUp.php` — Triggers Spatie database backup.
- `DemoReset.php` — Clears uploaded media and resets demo database state.
- `GenerateSitemap.php` — Generates XML sitemap using `spatie/laravel-sitemap`.
- `ImportDemo.php` — Imports demo fixtures and images.
- `PurchaseFile.php` — Inspects license/purchase status file.
- `RenameVideo.php` — Batch renames video lecture assets.
- `ReplaceFiles.php` — Utility file replacement script.

### 12.3 Scheduled Cron Tasks

**Forensic Finding: FACT.** Inspection of `app/Console/Kernel.php` lines 32–36 demonstrates that the `schedule(Schedule $schedule)` method is **completely empty**:
```php
protected function schedule(Schedule $schedule)
{
    //
}
```
**Conclusion:** The legacy application defines **no automated recurring background tasks, cron jobs, or scheduled queue cleanups** within Laravel's native scheduler.

---

## 13. Configuration, Environment & System Activation

### 13.1 Configuration Architecture

1. **Database-Driven Settings Store (`Setting::first()`):**
   - The primary application configuration is stored in the `settings` database table rather than `.env` files.
   - The global service provider `app/Providers/AppServiceProvider.php:67-90` loads `Setting::first()` during boot and shares global view variables (`$gsetting`, `$currency`, `$isetting`, `$zoom_enable`, `$terms`, `$hsetting`) across all Blade templates (**FACT**).
2. **Specialized Settings Tables:**
   - 10 additional configuration tables exist in schema: `homesettings` (25 toggle columns), `featuresettings`, `instructor_settings`, `mobile_settings`, `player_settings`, `videosettings`, `wallet_settings`, `servicesettings`, `color_options`, `widget_settings` (**FACT**).

### 13.2 System Activation & Licensing Gates

- **`IsActive` Middleware:** Intercepts incoming requests and verifies that `public/config.txt` contains `'1'` (**FACT** — `app/Http/Middleware/IsActive.php:20`).
- **Purchase Verification:** `public/code.txt` stores an encrypted purchase code checked during installer execution (**FACT**).
- **Environment Flag `IS_INSTALLED`:** Stored in `.env`; controls redirect to web installer when false (**FACT**).

---

## 14. File Storage & Media Delivery

- **Local Disk Storage:** Uploaded files, course thumbnails, certificates, and local video lectures are stored in `public/images/`, `public/files/`, `public/video/`, and `public/subtitles/` (**FACT**).
- **AWS S3 Cloud Storage:** Packages `aws/aws-sdk-php` and `league/flysystem-aws-s3-v3` are installed; `CourseClass` model contains column `aws_upload` (**FACT**). Actual production bucket usage remains **UNKNOWN**.
- **Media Management Package:** `itskodinger/midia` is installed for in-editor media selection (**FACT**).
- **Image Optimization:** `spatie/laravel-image-optimizer` optimizes uploaded images during controller store actions (**FACT**).

---

## 15. Automated Test Coverage

**Forensic Finding: FACT.** Inspection of the `tests/` directory reveals only the default framework scaffold tests:
- `tests/Unit/ExampleTest.php`
- `tests/Feature/ExampleTest.php`

**Conclusion:** The legacy repository possesses **zero domain unit tests, zero feature integration tests, and zero API test suites**. No automated verification suite exists to validate legacy behavior.

---

## 16. Reachability & Activity Matrix (REV-004, REV-010 Revision)

To avoid conflating existence with active runtime availability, the following matrix classifies inspected components according to verifiable reachability categories:
- **`REACHABLE`**: Routable, complete implementation exists, active controller and view/response verified.
- **`CONFIG-DEPENDENT`**: Code exists and is routable, but execution depends on specific external credentials, flags, or configuration keys.
- **`REFERENCE-ONLY`**: Code exists in codebase or packages, but has no active route caller or execution trigger.
- **`DEAD/ORPHAN`**: Code is proven unreachable due to control-flow logic, commented calls, or broken references.
- **`UNKNOWN`**: Reachability cannot be determined from repository inspection alone.

| Component / Subsystem | Reachability Status | Evidence & Basis |
|---|---|---|
| Core Web Routes (Courses, Auth, Cart, Checkout) | **REACHABLE** | Active route bindings in `routes/web.php`; complete controller methods and Blade templates verified. |
| Admin Panel Subsystem | **REACHABLE** | Mapped in `routes/web.php` with `is_admin` middleware; full controller and view hierarchy. |
| Core API Subsystem (Login, Register, Course list) | **REACHABLE** | Validated Passport guard and active controller endpoints in `routes/api.php`. |
| 19 nwidart Modules (`modules_statuses.json`) | **UNKNOWN** | Entries enabled in config, but `Modules/` directory does not exist on disk. Class loading fails without external module files. |
| Module API Endpoints (`/homework`, `/create/resumes`) | **DEAD** | Routes exist in `routes/api.php`, but controllers import `Modules\...` classes that are absent from filesystem. |
| Scheduled Cron Tasks | **DEAD** | `app/Console/Kernel.php:schedule()` is completely empty (**FACT**). No recurring cron tasks execute. |
| Queue Jobs (`EnrollExpire`, `AffiliatesPoints`) | **REFERENCE-ONLY / UNKNOWN DISPATCH** | Jobs defined in `app/Jobs/`, but no automated dispatch identified. Authenticated session dependency creates high runtime failure risk if queued. |
| Social Login Callback (lines 244–251) | **DEAD** | `LoginController@handleProviderCallback`: lines 244–251 are preceded by an unconditional `if/else` return block (**FACT**). |
| OTP Login Workflow | **CONFIG-DEPENDENT / UNKNOWN** | Routes and `OTPService` exist; view call in `showLoginForm` is commented out; activation state unverified. |
| Theme 1 Blade Views (`resources/views/front`) | **REACHABLE** | Active when `Setting.theme == '1'`. |
| Theme 2 Blade Views (`resources/views/theme_2`) | **CONFIG-DEPENDENT** | Active when `Setting.theme != '1'`. |
| Frontend `fe/` Views (`resources/views/fe`) | **REACHABLE** | Hardcoded return target in `LoginController@showLoginForm:52`. |
| Third-Party Meetings (Zoom, BBB, Jitsi, Meet) | **CONFIG-DEPENDENT** | Controllers and routes exist; operational activity depends on API credentials in settings tables. |
| Payment Gateways (Stripe, PayPal, etc.) | **CONFIG-DEPENDENT** | Controllers and callbacks exist; operational status depends on gateway credentials and environment keys. |

---

## 17. Systemic Constraints & Risks

The following structural constraints are established by repository evidence (**FACT**):

1. **Total Absence of Database Foreign Keys:** All 175 tables lack foreign key constraints; relational consistency depends entirely on application-level execution.
2. **Heavy Controller-Centric Business Logic:** Dominant proportion of business logic, database queries, and notifications reside directly in controller methods.
3. **Absence of Domain Automated Tests:** Zero test suites exist to validate regression behavior during re-engineering.
4. **Monolithic Route Definitions:** Single files `web.php` (1,156 lines) and `api.php` (505 lines) house all routing definitions without modular separation.
5. **Data Type / Representation Mismatches:** Currency and price fields stored as `varchar(191)` (e.g. `orders.total_amount`).
6. **Filesystem Dependency Disconnect:** 19 modules are marked enabled in configuration while the entire `Modules/` directory is missing from repository disk.

---

## 18. Unknowns Registry

The following uncertainty areas cannot be resolved from the inspected repository evidence and are formally recorded as **`UNKNOWN`**:

| ID | Domain Area | Description of Uncertainty |
|---|---|---|
| **UNK-001** | Missing Modules Filesystem | Location and implementation of the 19 enabled nwidart modules listed in `modules_statuses.json`; whether modules were deployed via Git submodules, build pipelines, or private packages. |
| **UNK-002** | OTP Authentication Activation | Whether phone OTP authentication is actively used in production, given commented view code in `LoginController`. |
| **UNK-003** | Inertia.js / Vue Integration Extent | Purpose and production usage of `HandleInertiaRequests` middleware given the dominance of Blade views. |
| **UNK-004** | InstructorPlan Job Dispatch | Mechanism, triggers, and frequency of `app/Jobs/InstructorPlan.php`. |
| **UNK-005** | Console Command `PurchaseFile` | Exact runtime purpose and operational triggering of `app/Console/Commands/PurchaseFile.php`. |
| **UNK-006** | Database Seeders Completeness | Whether database seeders in `database/seeders/` represent valid production baselines. |
| **UNK-007** | Exhaustive View Template Audit | Complete interaction mapping across all 179 view subdirectories in `resources/views/`. |
| **UNK-008** | Payment Gateway Production Reachability | Which of the 30+ payment gateway controllers are actively configured with live merchant keys in production. |
| **UNK-009** | Cloud S3 Media Utilization | Whether course media assets are actively uploaded to AWS S3 in production or stored locally on disk. |
| **UNK-010** | Google Classroom Integration Depth | Operational flow and API connectivity of Google Classroom module given missing module directory. |
| **UNK-011** | Push Notification Live Triggers | Which events trigger OneSignal or Firebase push notifications in the live deployment. |
| **UNK-012** | Subscription Lifecycle Webhook Handling | Full recurring billing lifecycle handling for Stripe subscriptions beyond initial order record insertion. |
| **UNK-013** | Queue Worker Execution Mode | Whether queue jobs in production are run via `sync` driver or async daemon workers (`php artisan queue:work`). |

---

## 19. Conflict & Anomaly Classification (REV-009 Revision)

In strict compliance with `OPEN-QUESTION-CONFLICT-CONVENTION-v1` and finding `REV-009`, this section separates genuine contradictory evidence (`CONFLICT`) from implementation inconsistencies, derived runtime risks, and confirmed dead code.

### 19.1 Genuine Contradictions (`CONFLICT`)

*No genuine contradictory evidence was identified where verified physical evidence directly conflicts on an immutable fact.*

### 19.2 Implementation Inconsistencies & Architectural Duplications (`INC`)

- **INC-001 — Dual Role Tracking Mechanism:**
  - *Observation:* User roles are tracked simultaneously via Spatie Permission tables (`roles`, `model_has_roles`) and a direct string column `users.role`.
  - *Evidence:* `LoginController.php:136` uses `$user->hasRole('admin')`, while `AdminController.php:51` uses `Auth::User()->role == "admin"`.
  - *Classification:* Implementation Inconsistency. Coexisting parallel patterns rather than contradictory evidence.
- **INC-002 — Numeric Financial Data Stored in String Column:**
  - *Observation:* Column `orders.total_amount` is defined as `varchar(191)` in database schema (`analysis/legacy-schema-snapshot.md:4689`), but application code treats it as numeric by calling `round()` in `Order::boot()` (`app/Order.php:17-31`) and performing arithmetic in `OrderStoreController`.
  - *Classification:* Data Model Inconsistency.

### 19.3 Derived Runtime Architectural Risks (`RISK`)

- **RISK-001 — Queue Job Dependency on Authenticated HTTP Session:**
  - *Observation:* Queue jobs `app/Jobs/EnrollExpire.php:37` and `app/Jobs/AffiliatesPoints.php:37` invoke `Auth::user()` inside their `handle()` methods.
  - *Evidence:* Code inspection of `EnrollExpire.php` and `AffiliatesPoints.php`.
  - *Classification:* Derived Runtime Risk. The code creates a strict dependency on session state; if dispatched asynchronously via CLI queue workers, `Auth::user()` evaluates to `null`. Production impact remains `UNKNOWN` without runtime worker logs.

### 19.4 Confirmed Dead / Unreachable Code (`DEAD`)

- **DEAD-001 — Unreachable Logic in Social Login Callback:**
  - *Observation:* In `app/Http/Controllers/Auth/LoginController.php` method `handleProviderCallback($social)`, lines 244–251 contain an `if ($user) { Auth::login($user); ... } else { return view('auth.register', ...); }` block.
  - *Evidence:* Control-flow inspection of lines 231–240 reveals an preceding `if (Auth::attempt(...)) { return ...; } else { return ...; }` construct where both branches unconditionally exit the method. Furthermore, parameter `$request` is accessed but not passed into the method signature.
  - *Classification:* Confirmed Dead / Unreachable Code.

---

## 20. Granular Evidence Traceability Matrix (REV-002, REV-011 Revision)

| Substantive Claim / Feature Area | Specific Source Files & Line / Symbol References | Schema / Configuration Evidence |
|---|---|---|
| Laravel Framework & Version | `composer.json:41` (`"laravel/framework": "^10.34.0"`) | `config/app.php:32` (`'version' => '6.7.0'`) |
| Passport API Authentication | `config/auth.php:44-47` (`'api' => ['driver' => 'passport']`) | `oauth_access_tokens`, `oauth_clients` tables |
| Spatie Permission RBAC | `composer.json:77`; `app/User.php:21` (`use HasRoles`) | `roles`, `permissions`, `model_has_roles` tables |
| Zero Foreign Keys | `analysis/legacy-schema-snapshot.md` (metadata across all 175 tables) | Information Schema query metadata |
| Empty Task Scheduler | `app/Console/Kernel.php:32-36` (`schedule()` method body empty) | Filesystem inspection |
| Course Management CRUD | `app/Course.php`, `app/CourseChapter.php`, `app/CourseClass.php`, `app/Http/Controllers/CourseController.php` | `courses`, `course_chapters`, `course_classes` tables |
| Free Enrollment Flow | `app/Http/Controllers/EnrollmentController.php:19-34` (`enroll()`) | `orders` table (direct insert via DB facade) |
| Paid Order Processing | `app/Http/Controllers/OrderStoreController.php:38-280` (`orderstore()`) | `orders`, `pending_payouts`, `carts` tables |
| Course Sequential Locking | `app/Http/Controllers/CourseProgressController.php:75-140` (`checkedCourse()`) | `course_progress` table (`mark_class_id` JSON array) |
| Certificate Serial & Generation | `app/Http/Controllers/CertificateController.php:25-60` (`show()`, `pdfdownload()`) | `certificates`, `course_progress` tables |
| Automatic Attendance Logging | `app/Http/Controllers/WatchController.php:36-61` (`watchOld()`) | `attandance` table (`setting.attandance_enable`) |
| Wallet Management & Checkout | `app/Wallet.php`, `app/Http/Controllers/WalletController.php`, `WalletPaymentController.php` | `wallet`, `wallet_transactions`, `wallet_settings` tables |
| Affiliate Referral Tracking | `app/Http/Middleware/CheckReferral.php:20`, `app/Http/Controllers/AffiliateController.php` | `affiliate` table; cookie `referral` |
| Support Ticket System | `app/AdminSupport.php`, `app/Http/Controllers/AdminSupportController.php:20-80` | `admin_supports`, `support_types` tables |
| Coupon System | `app/Coupon.php`, `app/Http/Controllers/CouponController.php` | `coupons` table |
| Quiz Assessment & Scoring | `app/QuizStartController.php:12-65`, `app/QuizTopic.php`, `app/QuizAnswer.php` | `quiz_topics`, `quiz_questions`, `quiz_answers` tables |
| Dead Social Callback Code | `app/Http/Controllers/Auth/LoginController.php:231-251` (`handleProviderCallback()`) | Control-flow inspection of return statements |
| Queue Job Auth Dependency | `app/Jobs/EnrollExpire.php:37`, `app/Jobs/AffiliatesPoints.php:37` (`Auth::user()`) | Line-level inspection of `handle()` methods |
| Missing Modules Directory | `composer.json:129`, `config/modules.php:73` (`base_path('Modules')`) | Filesystem absence of `Modules/` directory |

---

## 21. Boundary Enforcement

This artifact strictly records **WHAT CURRENTLY EXISTS** in the inspected repository. It deliberately does **not** contain:
- Functional or non-functional requirements for the new LMS system.
- Target architectural proposals or technology selections.
- Recommendations on retaining, redesigning, or discarding specific legacy features.
- Future-state database schemas, normalized entity models, or API specifications.

Legacy system behavior and architecture are documented here strictly as **evidence**, not as a specification or blueprint for the rewrite.

---

## 22. Summary & Review Readiness (REV-012 Revision)

| Metric / Dimension | Documented Value | Context & Governing Status |
|---|---|---|
| Document Artifact ID | `ART-001` | Maintained stable identity across revisions |
| Version | `1.1` | Targeted revision addressing ART-002 review findings |
| Lifecycle Status | `APPROVED` | Human Gate 1 approval granted by PROJECT_OWNER |
| Documented Feature Areas | 34 modules / functional subsystems | Verified with granular file and schema traceability |
| Reconstructed Execution Flows | 7 core workflows | Fully reconstructed across the 12 governance criteria |
| Recorded Unknowns | 13 items (`UNK-001` — `UNK-013`) | Explicitly registered without speculative gap-filling |
| Recorded Inconsistencies / Risks | 4 items (`INC-001`, `INC-002`, `RISK-001`, `DEAD-001`) | Classified strictly according to evidence nature |
| Gate 1 Status | **APPROVED** | Human Gate 1 approval granted by PROJECT_OWNER after independent re-review |
| Review Readiness | **APPROVED** | Human Gate 1 approval confirmed; ART-003 v1.0 approved; REV-001 through REV-013 resolved |
