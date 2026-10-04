---
document: ANALYSIS
artifact_id: ART-001
version: 1.0
status: DRAFT
owner: RE-RESEARCHER
prompt_id: RE-001
sources:
  - legacy LMS repository (d:/laragon/www/insmart)
  - analysis/legacy-schema-snapshot.md
---

# Existing System Analysis — Legacy LMS (InSmart / eClass)

## 1. Scope of Investigation

This artifact documents the **existing legacy LMS system** as observed from source code, configuration files, database schema, and project structure. All conclusions follow the evidence classification defined in the governance contracts.

**Boundary:** This document records WHAT EXISTS. It does not prescribe requirements, recommendations, or designs for a new system.

### Evidence Sources

| Source | Description |
|---|---|
| Repository root | `d:/laragon/www/insmart` |
| Schema snapshot | `analysis/legacy-schema-snapshot.md` — 175 tables, generated 2026-10-04 |
| Source code | PHP controllers, models, routes, middleware, config, jobs, mail, views |
| Configuration | `composer.json`, `config/`, `.env`, `modules_statuses.json` |

---

## 2. Repository & System Overview

| Property | Value | Classification |
|---|---|---|
| Framework | Laravel 10.x | FACT — `composer.json`: `"laravel/framework": "^10.34.0"` |
| PHP Version | ≥ 8.2 | FACT — `composer.json`: `"php": "^8.2"` |
| Application Version | 6.7.0 | FACT — `config/app.php` line 32 |
| Database | MySQL (InnoDB, utf8mb4_unicode_ci) | FACT — schema snapshot |
| Database Name | `project_insmart` | FACT — schema snapshot |
| Total Tables/Views | 175 | FACT — schema snapshot |
| Total Controllers | ~170+ PHP files | FACT — filesystem |
| Total Models | ~130+ PHP files in `app/` root | FACT — models at `app/*.php` |
| Total Migrations | 203 | FACT — `database/migrations/` |
| Route Files | web.php (1156 lines), api.php (505 lines) | FACT |
| Tests | Only scaffold ExampleTest | FACT |
| Frontend | Blade templates (multiple themes), Inertia.js configured | FACT |
| Module System | `nwidart/laravel-modules` 8.2 | FACT |
| Active Modules | 19 modules enabled | FACT — `modules_statuses.json` |
| API Auth | Laravel Passport | FACT — `config/auth.php` |
| Web Auth | Session-based | FACT |
| Authorization | Spatie Permission (roles + permissions) | FACT |
| Product Origin | eClass LMS variant with customizations | DERIVED |

### Application Name

`config/app.php` uses `env('APP_NAME', 'Laravel')`. Database `project_insmart`. Setting model defaults: "Eclass Learning Management". **DERIVED** — fork/customization of eClass LMS.


---

## 3. Technology & Runtime — Key Backend Dependencies

| Package | Purpose | Classification |
|---|---|---|
| `laravel/framework ^10.34.0` | Core framework | FACT |
| `laravel/passport` | API OAuth2 authentication | FACT |
| `laravel/socialite` | Social login (Google, Facebook, Amazon, GitLab, LinkedIn, Twitter) | FACT |
| `spatie/laravel-permission ^5.5` | RBAC (roles + permissions) | FACT |
| `spatie/laravel-translatable` | Multi-language model translations | FACT |
| `spatie/laravel-activitylog` | Activity logging | FACT |
| `spatie/laravel-backup` | Database backup | FACT |
| `inertiajs/inertia-laravel` | Inertia.js SSR bridge | FACT |
| `intervention/image` | Image manipulation | FACT |
| `nwidart/laravel-modules` | Modular architecture (addons) | FACT |
| `yajra/laravel-datatables-oracle` | Server-side DataTables | FACT |
| `niklasravnsborg/laravel-pdf` | PDF generation (certificates, invoices) | FACT |
| `pragmarx/google2fa-laravel` | 2FA via Google Authenticator | FACT |
| `joedixon/laravel-translation` | Translation management | FACT |
| `torann/currency` | Multi-currency support | FACT |
| `torann/geoip` | GeoIP detection | FACT |
| `rap2hpoutre/fast-excel` | Excel import/export | FACT |
| `spatie/laravel-sitemap` | Sitemap generation | FACT |
| `aws/aws-sdk-php` + `league/flysystem-aws-s3-v3` | AWS S3 storage | FACT |
| `kutia-software-company/larafirebase` | Firebase push | FACT |
| `laravel-notification-channels/onesignal` | OneSignal push | FACT |
| `twilio/sdk` | SMS via Twilio | FACT |
| `alaouy/youtube` | YouTube API | FACT |
| `vimeo/laravel` | Vimeo integration | FACT |
| `google/apiclient` | Google API (Meet, Classroom) | FACT |
| `bigbluebutton/bigbluebutton-api-php` | BigBlueButton | FACT |
| `mailchimp/marketing` + `spatie/laravel-newsletter` | Email marketing | FACT |
| `silviolleite/laravelpwa` | PWA support | FACT |
| `yadahan/laravel-authentication-log` | Login audit trail | FACT |
| `jackiedo/dotenv-editor` | .env editor (admin panel) | FACT |
| `consoletvs/charts` | Chart generation | FACT |

### Payment Gateway Packages

PayPal, Stripe (+ Cashier), Razorpay, Braintree, Mollie, Paystack, Flutterwave (Rave), Paytm, Midtrans, PayU, Iyzico, Omise, Square, Skrill, AamarPay, M-Pesa, Worldpay, SslCommerz, CashFree, ChargilyPay, 2Checkout, DPOPayment, Esewa, Onepay, Paytab, Bkash, PayFlexi, ManualPayment, BankTransfer, WalletPayment, UPI — all observed as packages or controllers. **Classification: FACT.**

### Enabled Modules (nwidart)

AuthorizeNet, Bkash, Certificate, Chatboard, DPOPayment, Ebook, Esewa, Forum, Googleclassroom, Homework, Onepay, Paytab, Resume, Smanager, Upi, SquarePay, Worldpay, Midtrains, MPesa — all enabled. **FACT.**

Note: `Modules/` directory not found at repository root — module file location **UNKNOWN**.

### Autoloaded Helpers

`Tracker.php`, `TwilioMsg.php`, `Is_wishlist.php`, `currency.php`, `fe.php` — all in `app/Helpers/`. **FACT.**


---

## 4. Architecture

### Architectural Pattern

**DERIVED.** Monolithic MVC with these characteristics:

- **No service layer** — controllers directly access Eloquent models and DB facade. Business logic in controllers.
- **No repository pattern** — direct Eloquent/DB queries in controllers.
- **Flat model structure** — all models in `app/` root (not `app/Models/`).
- **Module system** — `nwidart/laravel-modules` for add-on features.
- **Dual frontend** — Blade templates (primary) + Inertia.js bridge configured.

### Observed Layers

```
HTTP Request → Global Middleware → Route Middleware → Controller → Eloquent Model → MySQL
```

Evidence: `AdminController::index()` directly queries `User::count()`, `Course::count()`. `EnrollmentController::enroll()` uses `DB::table('orders')->insert()`. No service/repository intermediaries.

**FACT.**

---

## 5. Application Structure

```
app/
├── Charts/          — 6 chart classes
├── Console/Commands/ — 7 Artisan commands
├── Helpers/         — 5 helper files
├── Http/Controllers/ — ~170+ controllers (flat + Auth/, Api/, Roles/, landing/)
├── Http/Middleware/  — 19 middleware classes
├── Http/Requests/   — 44 form request classes
├── Jobs/            — 3 jobs
├── Library/         — SslCommerz (3 files)
├── Mail/            — 10 mailable classes
├── Notifications/   — 5 notification classes
├── Policies/        — 23 policy classes
├── Providers/       — 6 service providers
├── Services/        — 2 services (OTPService, sManagerService)
├── *.php            — ~130+ model files (flat in app root)
```

**FACT.**

---

## 6. Routing & Middleware

### Web Route Structure (FACT)

1. **Unauthenticated** — login, register, OTP, installer, cache clear
2. **`auth` + `is_admin`** — admin panel (~400+ routes): user/course/category/order/settings/payment/blog/quiz/certificate management
3. **`admin_instructor` + `auth`** — shared admin/instructor: Zoom, BBL, Jitsi, Google Meet, course CRUD, quiz, chapters, assignments, attendance
4. **`is_verified` + `2fa` + `maintanance_mode` + `switch_languages`** — public/student: browsing, cart, search, enrollment, checkout, payments, dashboard, certificates
5. **Payment callbacks** — Stripe, PayPal, Razorpay, etc.
6. **Currency management** — `manage/currency`
7. **Indonesian routes** — `jelajahi/` prefix (explore) with kelas, tes, ebook

### API Route Structure (FACT)

1. **Public** — login, register, home, courses, blog, FAQ, payment keys
2. **Authenticated** (`auth:api` via Passport) — wishlist, cart, enrollment, profile, orders, progress, quiz, assignments, Q&A, reviews, instructor dashboard, certificates, wallet, affiliate, resume, jobs

### Key Middleware

| Middleware | Behavior | Classification |
|---|---|---|
| `IsAdmin` | Allows any role except 'user' — `roles()->where('name', '!=', 'user')->exists()` | FACT |
| `AdminIntructor` | Allows admin or instructor — `hasAnyRole(['admin', 'instructor'])` | FACT |
| `IsVerified` | Email verification if `verify_enable` setting is 1 | FACT |
| `IsActive` | Reads `public/config.txt`; redirects if not '1' | FACT |
| `IpBlock` | IP blocking | FACT |
| `MaintananceMode` | Custom maintenance mode | FACT |
| `Google2FAAuthenticator` | 2FA enforcement | FACT |
| `SwitchLanguage` | Language switching | FACT |
| `CheckReferral` | Referral tracking via cookie (in web group) | FACT |
| `HandleInertiaRequests` | Inertia.js (in web group) | FACT |
| `role` / `permission` / `role_or_permission` | Spatie permission | FACT |


---

## 7. User Roles & Authorization

### Role System (FACT)

- Spatie `HasRoles` trait on User model.
- Roles referenced: `admin`, `instructor`, `user`.
- `User.role` varchar column also exists in `users` table.

**CONFLICT (CON-001):** Dual role tracking — Spatie roles table AND `users.role` string column:
- Spatie: `hasRole('admin')` in LoginController, `hasAnyRole()` in AdminIntructor middleware.
- String: `Auth::User()->role == "admin"` in AdminController, InstructorController.

### Permission Examples (FACT)

`courses.view`, `courses.create`, `courses.edit`, `courses.delete`, `certificate.manage`, `dashboard.manage`.

---

## 8. Authentication

### Web Auth (FACT)

- Email + password login
- Social login (Google, Facebook, Amazon, GitLab, LinkedIn, Twitter) via Socialite
- OTP login routes exist; activation state UNKNOWN
- Google 2FA middleware + `google2fa_secret` field
- Email verification (`MustVerifyEmail`, `IsVerified` middleware)
- Remember me, status-based deactivation, role-based redirect
- Guest checkout route defined

### API Auth (FACT)

Passport OAuth2, API login/register, social API login (FB, Google).

### Registration (FACT)

Fields: fname, lname, email, password. Conditional captcha. Referral tracking. Welcome email.


---

## 9. Major Modules & Features

### 9.1 Course Management (FACT)

**Course** (`courses`): belongs to User/Categories/CourseLanguage/RefundPolicy. Has many chapters, classes, quizzes, reviews, orders, progress, wishlists, etc. Translatable: title, short_detail, detail, requirement. Types: free/paid. Features: featured, slug, preview, drip, tags (JSON), multi-category (JSON), country targeting (JSON), institute. Admin approval via status + `courserejects`.

**CourseChapter** (`course_chapters`): ordered chapters, drip scheduling. **CourseClass** (`course_classes`): video/PDF/zip/audio/file/AWS content, preview, subtitles, drip.

### 9.2 Enrollment & Orders (FACT)

Free: `EnrollmentController@enroll` → DB insert. Paid: buynow → session → checkout → payment → `OrderStoreController@orderstore`. Order fields: course_id, user_id, instructor_id, transaction_id, payment_method, total_amount (varchar!), coupon_discount, currency, status, enroll_start/expire, bundle, subscription, refunded. **CON-002:** total_amount varchar but code rounds as numeric. `EnrollExpire` job deletes expired.

### 9.3 Cart & Checkout (FACT)

Cart model (user_id, course_id, price, coupon). Session cart for guests. Currency conversion via `torann/currency`. UserCurrency per user.

### 9.4 Quiz & Assessment (FACT)

QuizTopic (per-course, marks, timer, retry). Quiz/quiz_questions (MCQ, video/image-based, translatable). QuizAnswer. CSV import, admin approval, reports.

### 9.5 Assignment (FACT)

User/instructor/course/chapter linked. File upload + rating.

### 9.6 Certificate (FACT)

PDF from CourseProgress. Serial: `{progress_id}CR-{uniqid}`. Extensive design customization. Per-course/quiz toggle.

### 9.7 Course Progress (FACT)

JSON arrays: mark_chapter_id, all_chapter_id, mark_class_id, all_class_id. Completion = marked vs total.

### 9.8 Review & Rating (FACT)

Multi-dimension (learn, price, value) + text. Admin approval. Report reviews, helpful votes.

### 9.9 Bundle Courses (FACT)

course_id as JSON array. Subscription support (Stripe fields).

### 9.10 Live Meetings (FACT)

Zoom, BigBlueButton, Jitsi, Google Meet, Google Classroom. Recordings, paid meetings, attendance per type.

### 9.11 Blog (FACT)

CRUD, public listing, category blogs, admin approval.

### 9.12 Wallet (FACT)

Balance + transactions + settings. Wallet payment for purchases.

### 9.13 Affiliate / Referral (FACT)

Config (ref_length, points). User referred_by/affiliate_id. Cookie tracking, wallet credit.

### 9.14 Instructor Payout (FACT)

Revenue sharing. PendingPayout → admin approval → CompletedPayout. Methods: PayPal, bank, Paytm.

### 9.15 E-book (FACT)

Module: own cart, orders, categories, reviews.

### 9.16 Forum (FACT)

Module: categories, topics, comments.

### 9.17 Homework (FACT)

Module: homework + submissions. Course-linked, marks, deadlines.

### 9.18 Chatboard (FACT)

Module: conversations + messages. Text/media, seen status.

### 9.19 Resume / Job Portal (FACT)

Module: personal info, projects, work experience, academics, job posts, applications.

### 9.20 Subscription / Plans (FACT)

PlanSubscribe, InstructorPlan (course limits). Stripe subscription on orders.

### 9.21 Coupon (FACT), 9.22 Notifications (FACT), 9.23 Support Tickets (FACT), 9.24 Pages/CMS (FACT), 9.25 Flash Sales (FACT), 9.26 Attendance (FACT), 9.27 Watch Course (FACT), 9.28 Compare (FACT), 9.29 Wishlist (FACT)

All verified from models, controllers, and schema. See section 2 for source references.

### 9.30 Admin Dashboard & Reporting (FACT)

Admin/instructor dashboards with graphs. Reports: revenue, financial, quiz, progress, device logs, activity.

### 9.31 Multi-language (FACT)

`spatie/laravel-translatable` on models. SwitchLanguage middleware. JSON translations.

### 9.32 Theme System (FACT)

Setting.theme controls theme. Views: front/, theme_2/, fe/. ThemeController. ColorOption.

### 9.33 Installer / OTA Update (FACT)

InstallerController (DB setup). OtaUpdateController (updates). IS_INSTALLED env, config.txt/code.txt.

### 9.34 SEO / Marketing (FACT)

SeoDirectory, Google Tag Manager, sitemap.


---

## 10. Data Architecture — Key Entity Relationships

**DERIVED** — reconstructed from model relationships and schema.

```
User (users)
 ├── has many → Course [as instructor]
 ├── has many → Order [as student]
 ├── has many → ReviewRating, Question, Wishlist, Blog, CourseClass
 ├── has many → PendingPayout, CompletedPayout, BundleCourse, PlanSubscribe
 ├── has one → Wallet
 └── belongs to → Allcountry, Allstate, Allcity

Course (courses)
 ├── belongs to → User, Categories, CourseLanguage, RefundPolicy
 ├── has many → CourseChapter → CourseClass
 ├── has many → WhatLearn, CourseInclude, RelatedCourse
 ├── has many → Question → Answer, Announcement
 ├── has many → ReviewRating, ReportReview, Order, PendingPayout
 ├── has many → QuizTopic → Quiz → QuizAnswer
 └── has many → CourseProgress, Wishlist

Order (orders)
 └── belongs to → User (student), User (instructor), Course, BundleCourse
```

### Schema: No Foreign Keys (FACT)

Schema snapshot: **zero foreign-key relationships** across all 175 tables. All referential integrity enforced at Eloquent level only.

### Data Type Issues (FACT)

- `orders.total_amount` — varchar(191), treated as numeric in code
- Various `_id` fields use varchar instead of int (e.g., `institute.user_id`)


---

## 11. Background & Scheduled Processing

### Jobs (FACT)

| Job | Purpose | Issue |
|---|---|---|
| `EnrollExpire` | Deletes expired orders | Uses `Auth::user()` in `handle()` — broken in queue context |
| `AffiliatesPoints` | Wallet credit on referral | Same `Auth::user()` issue |
| `InstructorPlan` | UNKNOWN — not inspected | UNKNOWN |

**CON-003:** Both `EnrollExpire` and `AffiliatesPoints` use `Auth::user()` inside queue job `handle()`. Not available in worker context — likely only works if dispatched synchronously. **DERIVED.**

### Artisan Commands (FACT)

DatabaseBackUp, DemoReset, GenerateSitemap, ImportDemo, PurchaseFile (UNKNOWN purpose), RenameVideo, ReplaceFiles, Currency commands.

### Scheduled Tasks (FACT)

`Console/Kernel::schedule()` is **empty**. No automated recurring tasks.

---

## 12. Events / Listeners (FACT)

Only default: `Registered → SendEmailVerificationNotification`. No custom events/listeners.

---

## 13. Configuration & Environment

### Settings Pattern (FACT)

`Setting::first()` is the primary config store, accessed throughout codebase. Controls: theme, feature toggles, currency, social URLs, logo, etc.

`AppServiceProvider::boot()` shares `gsetting`, `currency`, `isetting`, `zoom_enable`, `terms`, `hsetting` to all views.

### Additional Settings Tables (FACT)

homesettings (25 toggle flags), featuresettings, instructor_settings, mobile_settings, player_settings, videosettings, wallet_settings, servicesettings, color_options, widget_settings.

### Key Env Dependencies (FACT)

`IS_INSTALLED` (installation gate), `DEFAULT_THEME` (conditional routing), payment gateway keys, mail config.

### License / Activation (FACT)

`IsActive` middleware → `public/config.txt`. `public/code.txt` → purchase verification. `verify_status` on settings. `demolock` in config.

---

## 14. File / Storage (DERIVED)

- Local: `public/images/` subdirectories
- AWS S3: packages present, `aws_upload` field on CourseClass
- Media manager: `itskodinger/midia`
- Image optimization: `spatie/laravel-image-optimizer`
- Video: local + YouTube + Vimeo + URL-based

---

## 15. Tests (FACT)

Only scaffold tests: `ExampleTest.php` (Feature + Unit). **No meaningful test coverage.**


---

## 16. Reachability & Activity Observations

| Component | Status | Classification |
|---|---|---|
| nwidart Modules | 19 enabled in JSON, `Modules/` dir not found at root | UNKNOWN |
| Scheduled tasks | Empty schedule() | FACT |
| EnrollExpire job | Auth::user() in handle — broken in queue | DERIVED |
| AffiliatesPoints job | Same Auth issue | DERIVED |
| Theme 2 views | theme_2/ exists but Login/Register use fe/ views | DERIVED — may be inactive |
| Old course routes | `courses/old/{slug}` suggests legacy migration | DERIVED |
| Social login callback | Unreachable code after Auth::attempt block (LoginController line 244+) | FACT — dead code |
| custom_login() | Uses old theme check — may be inactive | DERIVED |
| Module imports | `Modules\Googleclassroom`, `Modules\Certificate` imported in CourseController | FACT |
| DEFAULT_THEME env | Conditional route loading for 'classic' theme | FACT |
| Three theme variants | front.*, theme_2.front.*, fe.* views coexist | FACT |

---

## 17. Constraints (FACT)

- No DB foreign keys (all 175 tables)
- No service layer (business logic in controllers)
- No repository pattern
- No test coverage
- Monolithic routing (1156-line web.php)
- String-typed numeric columns
- Inconsistent naming (Attandance, announsment, truested)
- Mixed coding patterns (DB facade + Eloquent + raw inserts)
- Theme coupling (if/else in controllers)

---

## 18. Unknowns

| ID | Area | Description |
|---|---|---|
| UNK-001 | Modules filesystem | `Modules/` dir not found; file location unknown |
| UNK-002 | OTP authentication | Routes defined, activation state unclear |
| UNK-003 | Inertia.js usage | Middleware active, extent of Vue pages unknown |
| UNK-004 | InstructorPlan job | Not inspected |
| UNK-005 | PurchaseFile command | Purpose undetermined |
| UNK-006 | Database seeders | Not inspected |
| UNK-007 | Complete view layer | 179 view subdirs; full mapping not done |
| UNK-008 | Payment gateway internals | 20+ gateways, only headers inspected |
| UNK-009 | S3/AWS actual usage | Packages present, upload paths not traced |
| UNK-010 | Google Classroom depth | Module enabled, flow not traced |
| UNK-011 | Push notification triggers | Packages present, trigger points not mapped |
| UNK-012 | Subscription lifecycle | Stripe fields exist, full flow not traced |

---

## 19. Conflicts

| ID | Area | Description | Evidence |
|---|---|---|---|
| CON-001 | Role system | Dual tracking: Spatie HasRoles + users.role column | User.php HasRoles trait; AdminController `role == "admin"`; LoginController `hasRole('admin')` |
| CON-002 | Data types | orders.total_amount varchar but treated as numeric | Schema: varchar(191); Order::boot() calls round() |
| CON-003 | Queue jobs | EnrollExpire/AffiliatesPoints use Auth::user() in handle() | app/Jobs/EnrollExpire.php:37, app/Jobs/AffiliatesPoints.php:37 |
| CON-004 | Dead code | Unreachable code in social login callback | LoginController.php lines 244-251, after Auth::attempt block |

---

## 20. Evidence Traceability

| Claim | Source |
|---|---|
| Laravel 10 | composer.json: `"laravel/framework": "^10.34.0"` |
| PHP ≥ 8.2 | composer.json: `"php": "^8.2"` |
| Version 6.7.0 | config/app.php line 32 |
| 175 tables | legacy-schema-snapshot.md metadata |
| Passport API | config/auth.php api guard |
| Spatie permissions | composer.json + User.php HasRoles + Kernel.php middleware |
| No foreign keys | legacy-schema-snapshot.md (every table) |
| No tests | tests/ directory listing |
| Empty schedule | Console/Kernel.php lines 32-36 |
| IsAdmin behavior | Http/Middleware/IsAdmin.php line 20 |
| Direct role check | Http/Controllers/AdminController.php line 51 |
| Models in app root | filesystem: 130+ .php files in app/ |
| 19 modules | modules_statuses.json |
| Order rounding | app/Order.php lines 17-31 |
| EnrollExpire Auth | app/Jobs/EnrollExpire.php line 37 |
| Dead social code | Http/Controllers/Auth/LoginController.php lines 231-251 |
| DB insert enrollment | Http/Controllers/EnrollmentController.php lines 23-31 |
| View composer sharing | Providers/AppServiceProvider.php lines 67-90 |

---

## 21. Boundary Statement

This document records **what exists**. It does NOT contain: requirements for new system, architecture recommendations, feature retention/removal decisions, target technology choices, database redesign, API/UI design.

Legacy behavior here is **evidence, not blueprint**.

---

## 22. Summary

| Metric | Value |
|---|---|
| Features documented | 34 modules |
| Flows traced | Enrollment, orders, auth, authorization, courses |
| Unknowns | 12 (UNK-001 — UNK-012) |
| Conflicts | 4 (CON-001 — CON-004) |
| Blocking issues | None |
| Review readiness | Ready for independent review |

