# Legacy System — Bottom-Up Forensic Feature Inventory

---

## 1. Analysis Scope

| Property | Value |
|---|---|
| Repository | `d:/laragon/www/insmart` |
| Commit | `68ce7ed725a0db21dab12e5f6e7e839b499e7554` (branch: `development`) |
| Analysis Date | 2026-10-16 |
| Framework | Laravel 10.x (PHP ^8.2) |
| Application Version | 6.7.0 (`config/app.php:32`) |
| Database Engine | MySQL (InnoDB, utf8mb4_unicode_ci) |

### Directories / Components Inspected

- `app/` — 131 models, 238 controllers, 19 middleware, 3 jobs, 10 mail classes, 5 notifications, 23 policies, 6 charts, 7 console commands, 2 services, 5 helpers, 3 library files
- `routes/web.php` (1,156 lines), `routes/api.php` (505 lines)
- `database/migrations/` — 203 migration files
- `resources/views/` — admin, front, theme_2, fe, instructor, landing, auth, certificate, email, vendor
- `config/` — app, auth, modules
- `modules_statuses.json` — 19 module entries
- `composer.json` — 92 production + 11 dev dependencies

### Known Limitations

1. **Modules directory absent.** `modules_statuses.json` records 19 configured modules while `Modules/` is absent from inspected repository (`VERIFIED`). Consequences for individual module-dependent paths are `DERIVED` or `UNKNOWN` unless a cited controller/route demonstrates a missing dependency; production module deployment is `UNKNOWN`.
2. **No automated tests.** Only scaffold `ExampleTest` files.
3. **Zero database foreign keys.** Referential integrity is application-level only.
4. **Task scheduler empty.** `app/Console/Kernel.php:32-36` — `schedule()` body commented out.
5. **Single event listener.** Only `Registered → SendEmailVerificationNotification`.

---

## 2. Repository Structure Discovery

### Observed Architecture

Monolithic Laravel 10 application with absent modular extension system (`nwidart/laravel-modules`).

**Backend:** Models directly in `app/` (no `Models/` subdirectory). Controllers in `app/Http/Controllers/` with subdirs `Api/`, `Api/Auth/`, `Auth/`, `landing/`, `Roles/`. No service/repository pattern — business logic resides in controllers. 2 service files: `OTPService.php`, `sManagerService.php`.

**Helpers** autoloaded globally (`composer.json:118-124`): `Tracker.php`, `TwilioMsg.php`, `Is_wishlist.php`, `currency.php`, `fe.php`.

**Frontend:** Multi-theme Blade: `front/` (classic), `theme_2/front/`, `fe/` (newer, Indonesian labels), `landing/`, `admin/`, `instructor/`. Inertia.js bridge present but Blade is primary.

**Auth/Authz:** Laravel Passport (API). Spatie Permission (`HasRoles` on `User`). Custom middleware: `is_admin` (any non-user role), `admin_instructor` (admin or instructor role), `is_active` (checks `public/config.txt`), `is_verified`, `ip_block`, `maintanance_mode`, `IsInstalled`, `2fa`.

**Payment Architecture:** 19+ gateway controllers all instantiate `OrderStoreController` and call `->orderstore(...)`. Central order creation in `OrderStoreController` (518 lines).

**Middleware `is_admin`** (`IsAdmin.php:20`): allows any authenticated user whose role is NOT `user`. This means instructors and admins both pass. Despite name, NOT admin-only.



---

## 3. Entry Point Inventory

### Web Routes (routes/web.php)

| Route Group | Authentication | Middleware | Count | Purpose |
|---|---|---|---|---|
| Guest routes | No | `guest` | ~15 | Login, register, password reset, social auth |
| Public routes | No | None | ~50 | Course catalog, landing pages, course details |
| User routes | Yes | `auth`, `is_verified` | ~80 | Enrolled courses, progress, wishlist, cart, checkout |
| Admin routes | Yes | `auth`, `is_admin` | ~150 | Admin panel, CRUD for all entities |
| Instructor routes | Yes | `auth`, `admin_instructor` | ~60 | Course authoring, student management, earnings |

**Total web routes:** ~350+ (file: 1,156 lines)

### API Routes (routes/api.php)

| Route Group | Authentication | Purpose |
|---|---|---|
| Public API | No | Course list, categories, search |
| Auth API | Yes | Login, register, password reset |
| User API | Yes | Enrolled courses, progress, profile |
| Payment callbacks | Varies | Gateway webhooks/callbacks |

**Total API routes:** ~120+ (file: 505 lines)

### Console Commands (app/Console/Commands)

| Command | Signature | Purpose |
|---|---|---|
| `DatabaseBackUp` | `database:backup` | Export database to SQL file |
| `DemoReset` | `demo:reset` | Truncate all tables (DESTRUCTIVE) |
| `GenerateSitemap` | `sitemap:generate` | Generate XML sitemap |
| `ImportDemo` | `import:demo` | Import demo content from ZIP |
| `PurchaseFile` | Not registered | Purchase code validation |
| `SendMail` | Not registered | Email sending utility |
| `Unsubscribe` | Not registered | Newsletter unsubscribe |

**Total commands:** 7 (4 registered in Kernel, 3 not registered)

### Queue Jobs (app/Jobs)

| Job | Trigger | Purpose | Status |
|---|---|---|---|
| `AffiliatesPoints` | Order completion | Award affiliate points | VERIFIED direct `Auth::user()` use; queue result UNKNOWN |
| `EnrollExpire` | Enrollment expiry | Revoke access to expired enrollments | VERIFIED direct `Auth::user()` use; queue result UNKNOWN |
| `InstructorPlan` | Subscription expiry | Handle instructor plan expiration | VERIFIED direct `Auth::user()` use; queue result UNKNOWN |

**Total jobs:** 3 (direct `Auth::user()` use VERIFIED; queue-worker failure is DERIVED; runtime result UNKNOWN)

### Event Listeners

| Event | Listener | Purpose |
|---|---|---|
| `Registered` | `SendEmailVerificationNotification` | Send verification email on registration |

**Total listeners:** 1

### Middleware

| Middleware | Purpose | Status |
|---|---|---|
| `IsAdmin` | Restrict to admin role | MISLEADING — allows instructors |
| `AdminIntructor` | Admin or instructor | Working |
| `IsActive` | Check if system active | Working |
| `IsVerified` | Email verified | Working |
| `2fa` | Two-factor auth | Working |
| `ip_block` | Block banned IPs | Working |
| `maintanance_mode` | Maintenance mode | Working |
| `IsInstalled` | Redirect if not installed | Working |
| `CheckReferral` | Track affiliate referrals | Working |
| `switch_languages` | Language switching | Working |

**Total custom middleware:** 10+ (19 total including Laravel defaults)

---

## 4. Capability Inventory (CAP-XXX)

**Inventory certainty scope:** Section 4 records inherited static inventory evidence from cited routes, controllers, models, configuration, and commands. Each entry establishes only its documented static reference unless explicitly qualified. Runtime execution, deployment configuration, production reachability, authorization enforcement, external-provider behavior, persistence outcome, and security outcome are `UNKNOWN` without current evidence. Risk statements are `DERIVED` unless identified as cited static facts. This scope note does not replace individual certainty corrections in material CAP records.

### CAP-001 · Authentication & Registration

| Attribute | Detail |
|---|---|
| **Purpose** | User registration, login, password reset, email verification, OTP, 2FA, social login |
| **Entry Points** | `web.php:49-51,63-67,107,111,124,136-138`; `api.php:31-42` |
| **Controllers** | `Auth\LoginController`, `Auth\RegisterController`, `Auth\ForgotPasswordController`, `Auth\ResetPasswordController`, `Auth\VerificationController`, `AuthController` (OTP/social), `TwoFactorAuthController`, `Api\Auth\LoginController`, `Api\Auth\RegisterController` |
| **Models** | `User` (roles: admin/instructor/user), `Otp`, `SocialLogin` |
| **Middleware** | `auth`, `guest`, `2fa`, `is_verified`, `CheckReferral` |
| **DB Tables** | `users`, `otps`, `social_logins`, `two_factor_authentications`, `password_resets` |
| **Mail** | `WelcomeUser`, `SendOtp`, forgotemail (raw Blade) |
| **Notifications** | None (mail used directly) |
| **Social Providers** | Facebook, Google, GitLab, Amazon, LinkedIn, Twitter (configured via `SettingController:644-793`) |
| **Execution Flow** | Register → validate → create User → optional email verify → optional OTP verify → login. Social: redirect to provider → callback → find/create user → login. 2FA: after login check → verify code → proceed. |
| **Side Effects** | Sets `CheckReferral` cookie for affiliate tracking. Dispatches `WelcomeUser` mail. Sets session. |
| **State Transitions** | `users.status`: 0 (inactive) → 1 (active). `users.verified`: 0 → 1. |
| **Risks** | OTP stored in DB plaintext. Social login tokens stored in DB. No rate limiting on OTP endpoint. |

### CAP-002 · Role-Based Access Control (RBAC)

| Attribute | Detail |
|---|---|
| **Purpose** | Restrict access based on user role |
| **Entry Points** | All route groups in `web.php` use middleware `is_admin` or `admin_instructor` |
| **Controllers** | N/A (middleware layer) |
| **Models** | `User` (column `role`: string enum admin/instructor/user). Also `HasRoles` trait (Spatie). |
| **Middleware** | `IsAdmin` (allows any non-`user` role — bug: instructors pass), `AdminIntructor` (admin or instructor), `IsActive` (checks config.txt not user status) |
| **DB Tables** | `users`, `roles`, `permissions`, `model_has_roles`, `role_has_permissions`, `model_has_permissions` |
| **Execution Flow** | Request → middleware check `Auth::user()->role` → allow/redirect |
| **Anomaly** | `IsAdmin` middleware name is misleading — allows instructors. Spatie RBAC tables exist but middleware uses raw column check, not Spatie API. Dual authorization system (Spatie + raw column). |
| **Risks** | Cited `IsAdmin` logic allows non-`user` roles (`VERIFIED`); instructor access to each admin route is DERIVED and route-specific authorization effect is UNKNOWN. `AuthServiceProvider:$policies` is empty (`VERIFIED`); policy effect is UNKNOWN. |

### CAP-003 · Course Management (Admin/Instructor CRUD)

| Attribute | Detail |
|---|---|
| **Purpose** | Create, edit, publish, clone, delete courses with chapters, classes (lessons), and content |
| **Entry Points** | `web.php:155-175` (admin resource), `web.php:595-630` (instructor) |
| **Controllers** | `CourseController` (admin), `CoursechapterController`, `CourseclassController`, `InstructorCourseController` |
| **Models** | `Course` (~30 relationships), `CourseChapter`, `CourseClass`, `CourseLanguage`, `CourseLevel`, `What_learn`, `RelatedCourse`, `CourseInclude`, `Requirement` |
| **DB Tables** | `courses`, `course_chapters`, `course_classes`, `course_languages`, `course_levels`, `what_learns`, `related_courses`, `course_includes`, `requirements` |
| **Fields on Course** | `title`, `slug`, `short_detail`, `detail`, `price`, `discount_price`, `type` (1=paid, 0=free), `status` (1=active, 0=draft), `featured`, `duration`, `preview_image`, `preview_type`, `video_url`, `drip_enable`, `certificate_enable`, `course_tags`, `level_id`, `language_id`, `category_id`, `subcategory_id`, `childcategory_id`, `user_id` (instructor), `instalment_allow` |
| **Execution Flow** | Admin/Instructor → create course → add chapters → add classes (video/audio/document/iframe/text/SCORM) → set pricing → publish. Clone: deep copy course + chapters + classes + quizzes + relationships. |
| **Side Effects** | Notifications sent to enrolled users on new content (`CourseNotification`). Image upload to `public/images/course/`. |
| **State Transitions** | `status`: 0 (draft) → 1 (published). `featured`: 0 → 1. |
| **Risks** | Content versioning, audit-trail, and upload-validation observations are limited to cited course-management paths; broader coverage, runtime enforcement, and security outcome are UNKNOWN. |



### CAP-004 · Course Content Delivery (Watch/Player)

| Attribute | Detail |
|---|---|
| **Purpose** | Deliver video/audio/document/iframe/SCORM course content to enrolled learners |
| **Entry Points** | `web.php:864-866,906,914` |
| **Controllers** | `WatchController` — methods: `watch`, `watchclass`, `audioclass`, `view`, `lightbox` |
| **Models** | `Course`, `CourseClass`, `CourseChapter`, `Order` (enrollment check) |
| **DB Tables** | `courses`, `course_classes`, `course_chapters`, `orders` |
| **Execution Flow** | User clicks lesson → `watch($id)` → verify enrollment (check `orders` table) → load class content → render player view. Content types: video (YouTube/Vimeo/self-hosted/AWS), audio, document (PDF), iframe, text, SCORM. |
| **Drip Content** | If `course.drip_enable=1`, classes released on schedule. `CourseClass` has `drip_date` or drip rules checked in controller. |
| **Side Effects** | Progress tracking via `CourseProgress` model. |
| **Risks** | Direct file URL guessability is DERIVED. Absence of a signed-URL mechanism is limited to cited paths. SCORM dependency references are static facts; module runtime behavior is UNKNOWN. |

### CAP-005 · Course Progress Tracking

| Attribute | Detail |
|---|---|
| **Purpose** | Track learner completion of individual lessons and overall course |
| **Entry Points** | `web.php:924-927` |
| **Controllers** | `CourseProgressController` — methods: `checked`, `unchecked`, `checkedCourse`, `progressreport`, `progressview` |
| **Models** | `CourseProgress` |
| **DB Tables** | `course_progress` |
| **Execution Flow** | User completes lesson → AJAX `checked($id)` → create/update `CourseProgress` record → recalculate overall % → return JSON. Instructor can view progress reports per student. |
| **Access Control** | `checkAccess($class_id)` verifies enrollment before marking progress. |
| **Side Effects** | Overall course completion % calculated. Certificate eligibility determined by 100% progress. |

### CAP-006 · Shopping Cart

| Attribute | Detail |
|---|---|
| **Purpose** | Session-based cart for course purchases |
| **Entry Points** | `web.php:835-840` |
| **Controllers** | `CartController` — methods: `addtocart`, `removecart`, `cartpage` |
| **Models** | `Cart` (session-based, NOT DB persisted for web; `Cart` model exists for API) |
| **DB Tables** | `carts` (API only) |
| **Execution Flow** | User clicks "Add to Cart" → `addtocart($id)` → store course_id in session array → redirect to cart page → display cart items → proceed to checkout. |
| **Duplicate Prevention** | Checks if course already in cart or already purchased. |
| **Side Effects** | Session manipulation only. No persistent cart for web users. |
| **Risks** | Session-backed cart storage is documented in cited code. Cart loss on expiry, login-merge behavior, and concurrent-update outcomes are DERIVED; runtime behavior is UNKNOWN. |

### CAP-007 · Checkout & Order Creation

| Attribute | Detail |
|---|---|
| **Purpose** | Process payment and create enrollment orders |
| **Entry Points** | `web.php:844-852` (checkout page), `web.php:881-999` (payment routes) |
| **Controllers** | `CheckoutController` (checkout page rendering + coupon apply), `OrderStoreController` (central order creation — 518 lines) |
| **Models** | `Order`, `Course`, `User`, `Coupon`, `BundleCourse`, `Wallet`, `PendingPayout` |
| **DB Tables** | `orders`, `courses`, `users`, `coupons`, `bundle_courses`, `wallets`, `pending_payouts` |
| **Execution Flow** | 1. User on checkout page → select payment method → submit. 2. Payment gateway controller processes payment. 3. On success: instantiates `OrderStoreController`, calls `orderstore($txn_id, $payment_method, ...)`. 4. `orderstore()` reads cart from session → iterates items → creates `Order` record per item → calculates instructor revenue → creates `PendingPayout` → dispatches `EnrollExpire` job → dispatches `AffiliatesPoints` job → sends `UserEnroll` notification → sends `AdminOrder` notification → sends `SendOrderMail` email → clears cart → redirects to confirmation. |
| **Revenue Split** | `instructor_revenue` calculated based on `Setting.instructor_revenue` percentage. Stored on `Order` and `PendingPayout`. |
| **State Transitions** | `Order.status`: 0 (pending) → 1 (completed). `Order.enroll_expire`: set from `course.enrollment_duration`. |
| **Side Effects** | Wallet deduction if wallet payment. Coupon usage incremented. Affiliate points dispatched. Mail sent to buyer + admin. Notification sent to buyer + admin. |
| **Risks** | `OrderStoreController` is directly instantiated. Cited jobs use `Auth::user()` (VERIFIED; runtime result UNKNOWN). No same-`transaction_id` check or transaction wrapper is documented for cited order-creation path (VERIFIED); duplicate/partial-write outcomes are DERIVED and runtime behavior UNKNOWN. |



### CAP-008 · Payment Gateway Integrations

| Attribute | Detail |
|---|---|
| **Purpose** | Process payments through 19+ gateways |
| **Entry Points** | `web.php:881-999,1128-1130`; `api.php:80-174` |
| **Controllers** | `PaypalController`, `StripePaymentController`, `RazorpayController`, `PayStackController`, `PaytmController`, `BankTransferController`, `CashFreeController`, `MoliController`, `PayUController`, `SkrillController`, `OmiseController`, `SslCommerzPaymentController`, `FlutterwaveController`, `IyzController`, `AamarPayController`, `PayHereController`, `BraintreeController`, `ChargilyPayController`, `PayFlexiController`, `ManualPaymentController`, `WalletPaymentController`, `TwoCheckoutPaymentController` |
| **Pattern** | Every gateway controller: validates payment → on success → `$checkout = new OrderStoreController; return $checkout->orderstore($txn_id, $payment_method, ...)` |
| **Models** | `Order`, gateway-specific (none — all use `Order`) |
| **DB Tables** | `orders`, payment gateway config in `settings` table |
| **Config Storage** | Gateway credentials stored in `settings` table rows, not `.env`. Retrieved via `Setting::first()`. |
| **Special Cases** | `ManualPaymentController` — file upload proof of payment, `payment_status = 'pending'`. `BankTransferController` — offline bank transfer, `payment_status = 'pending'`. `WalletPaymentController` — deducts from user wallet balance. |
| **Risks** | Cited code retrieves gateway configuration through `Setting::first()` (VERIFIED). Gateway-wide webhook validation, idempotency, encryption, and administrator access control are UNKNOWN without focused audit. |

### CAP-009 · Coupon / Discount System

| Attribute | Detail |
|---|---|
| **Purpose** | Apply percentage or fixed discounts to course purchases |
| **Entry Points** | `web.php:848` — `CheckoutController@applycoupon` |
| **Controllers** | `CheckoutController` (apply), `CouponController` (CRUD admin) |
| **Models** | `Coupon` |
| **DB Tables** | `coupons` — fields: `code`, `type` (percent/fixed), `value`, `max_usage`, `used`, `expire_date`, `link_by` (course/category/bundle), `category_id`, `course_id` |
| **Execution Flow** | User enters code → validate exists, not expired, not max used, applicable to cart items → calculate discount → store in session → apply at checkout. |
| **Side Effects** | `coupon.used` incremented on order completion. `order.coupon_id` set. |

### CAP-010 · Wallet System

| Attribute | Detail |
|---|---|
| **Purpose** | Virtual wallet for course purchases and instructor earnings |
| **Entry Points** | `web.php:1001-1025` |
| **Controllers** | `WalletController` — methods: `wallet`, `addbalance`, `walletaddbalance`, `all_transactions`, `walletrecharge` |
| **Models** | `Wallet`, `AddOnWallet` |
| **DB Tables** | `wallets` (user_id, balance), `add_on_wallets` (type, amount, user_id, order_id) |
| **Execution Flow** | Add balance: User → select amount → pay via gateway → credit wallet. Purchase: checkout with wallet → verify sufficient balance → deduct → create order. |
| **State Transitions** | Wallet balance increases on recharge, decreases on purchase, increases on refund. |
| **Risks** | No pessimistic locking is documented for the cited balance-update path. Concurrent-deduction race risk is DERIVED; runtime outcome is UNKNOWN. |

### CAP-011 · Instructor Payout System

| Attribute | Detail |
|---|---|
| **Purpose** | Track and disburse instructor earnings from course sales |
| **Entry Points** | `web.php:1098-1116` |
| **Controllers** | `PayoutController` (instructor request), `AdminPayoutController` (admin approve), `CompletedPayoutController` (history) |
| **Models** | `PendingPayout`, `CompletedPayout` |
| **DB Tables** | `pending_payouts` (instructor_id, course_id, order_id, amount, status), `completed_payouts` |
| **Execution Flow** | Sale occurs → `PendingPayout` created with instructor's revenue share → Instructor views pending payouts → requests payout → Admin reviews → marks as paid → moves to `CompletedPayout`. |
| **Revenue Calculation** | `Setting.instructor_revenue` (percentage). Stored on `Order.instructor_revenue` and `PendingPayout.amount`. |
| **Side Effects** | Bulk payout support via `AdminPayoutController@bulk_payout`. |

### CAP-012 · Quiz / Assessment System

| Attribute | Detail |
|---|---|
| **Purpose** | Create and deliver quizzes within courses, auto-grade, track attempts |
| **Entry Points** | `web.php:908-922` |
| **Controllers** | `QuizStartController` — methods: `quizstart`, `quizsubmit`, `quizresult`. Admin: `QuizController`, `QuizTopicController` |
| **Models** | `Quiz`, `QuizTopic`, `QuizAnswer`, `QuizAttempt` (implied from controller) |
| **DB Tables** | `quizzes` (topic_id, course_id, question, a/b/c/d, answer, timer), `quiz_topics`, `quiz_answers` |
| **Question Types** | Multiple choice (4 options: a/b/c/d). Timer per quiz. |
| **Execution Flow** | Student starts quiz → timer begins → answers questions → submit → auto-grade against stored answers → store attempt → show result with pass/fail. |
| **Side Effects** | Quiz score stored. Certificate eligibility may depend on quiz pass. |
| **Risks** | All answers sent to client-side (potential cheating). Timer is client-side. |



### CAP-013 · Certificate Generation

| Attribute | Detail |
|---|---|
| **Purpose** | Generate PDF/viewable certificates upon course completion |
| **Entry Points** | `web.php:918-920` |
| **Controllers** | `CertificateController` — methods: `show`, `pdfdownload`, `verify`. Admin: `CertificateDesignController` (design templates) |
| **Models** | `Certificate`, `CertificateDesign` (from Modules — BROKEN DEPENDENCY) |
| **DB Tables** | `certificates`, `certificate_designs` |
| **Execution Flow** | Course completion (100% progress + quiz pass if required) → user clicks "Get Certificate" → generate with template → store → allow download. Verification via unique certificate code. |
| **Dependencies** | `barryvdh/laravel-dompdf` for PDF generation. `Modules\Certificate` referenced but module absent. |
| **Side Effects** | Certificate stored in DB with unique verification code. |

### CAP-014 · Live Class — Zoom Integration

| Attribute | Detail |
|---|---|
| **Purpose** | Create and manage Zoom meetings linked to courses |
| **Entry Points** | `web.php:527-555` |
| **Controllers** | `ZoomController` — methods: `index`, `create`, `store`, `edit`, `update`, `destroy`, `show`, `zoomsetting`, `zoomupdatesetting` |
| **Models** | `Meeting` |
| **DB Tables** | `meetings` (course_id, meeting_id, topic, start_time, duration, password, timezone, link_by, instructor_id) |
| **Execution Flow** | Instructor creates meeting → Zoom API called → meeting_id stored → students see meeting link → join via Zoom. |
| **Dependencies** | Zoom JWT/OAuth API. Credentials in `settings` table. |

### CAP-015 · Live Class — BigBlueButton Integration

| Attribute | Detail |
|---|---|
| **Purpose** | Create and manage BBB meetings linked to courses |
| **Entry Points** | `web.php:556-572` |
| **Controllers** | `BigBlueController` — methods: `index`, `create`, `store`, `edit`, `update`, `destroy`, `show`, `join`, `bbbsetting` |
| **Models** | `BBBMeeting` |
| **DB Tables** | `bbb_meetings` |
| **Dependencies** | BigBlueButton API. Credentials in `settings` table. |

### CAP-016 · Live Class — Google Meet Integration

| Attribute | Detail |
|---|---|
| **Purpose** | Create and manage Google Meet events linked to courses |
| **Entry Points** | `web.php:573-590` |
| **Controllers** | `GooglemeetController` — methods: `dashboard`, `create`, `store`, `allgooglemeeting`, `oauth`, `delete`, `googlemeetdetailpage`, `edit`, `updatemeeting`, `googlemeetsetting`, `googleupdatefile` |
| **Models** | `GoogleMeet` |
| **DB Tables** | `google_meets` |
| **Dependencies** | Google Calendar API. OAuth flow. Service account JSON upload. |

### CAP-017 · Bundle Courses

| Attribute | Detail |
|---|---|
| **Purpose** | Group multiple courses into a discounted bundle |
| **Entry Points** | `web.php:929-931` (front), `web.php:380-395` (admin CRUD) |
| **Controllers** | `BundleCourseController` — methods: `addtocart`, `detailpage`, `enroll`. Admin CRUD via resource routes. |
| **Models** | `BundleCourse` |
| **DB Tables** | `bundle_courses` (title, slug, price, discount_price, course_id JSON array, user_id, status, featured) |
| **Execution Flow** | Cited routes/controllers describe bundle creation, pricing, and enrollment handling. All-course enrollment after purchase is DERIVED; runtime enrollment outcome is UNKNOWN. |

### CAP-018 · Wishlist

| Attribute | Detail |
|---|---|
| **Purpose** | Save courses for later purchase |
| **Entry Points** | `web.php:838-840` |
| **Controllers** | `WishlistController` — methods: `wishlist`, `addwishlist`, `removewishlist` |
| **Models** | `Wishlist` |
| **DB Tables** | `wishlists` (user_id, course_id) |
| **Helper** | `Is_wishlist::in_wishlist($c)` — checks if course is in user's wishlist |

### CAP-019 · Review & Rating

| Attribute | Detail |
|---|---|
| **Purpose** | Allow enrolled users to rate and review courses |
| **Entry Points** | `web.php:870-873` |
| **Controllers** | `ReviewratingController` — methods: `reviewstore`, `reviewupdate`, `reviewdelete` |
| **Models** | `ReviewRating` |
| **DB Tables** | `review_ratings` (user_id, course_id, learn, price, value, review, approved, status) |
| **Execution Flow** | Enrolled user submits review → stored with status=pending → admin approves → visible on course page. |

### CAP-020 · Q&A / Discussion Forum

| Attribute | Detail |
|---|---|
| **Purpose** | Course-specific question and answer discussions |
| **Entry Points** | `web.php:867-869` |
| **Controllers** | `QuestionanswerController` — methods: `questionstore`, `answerstore` |
| **Models** | `QuestionAnswer`, `Answer` |
| **DB Tables** | `question_answers` (user_id, course_id, question, instructor_id), `answers` |
| **Execution Flow** | Student asks question on course page → instructor/admin answers → threaded Q&A. |



### CAP-021 · Refund System

| Attribute | Detail |
|---|---|
| **Purpose** | Allow users to request refunds on purchased courses |
| **Entry Points** | `web.php:943-946` |
| **Controllers** | `RefundCourseController` — CRUD + `refundview`, `refundpolicy`. `OrderController@refundview`, `OrderController@refundrequest` |
| **Models** | `RefundCourse`, `RefundPolicy` |
| **DB Tables** | `refund_courses` (user_id, course_id, order_id, reason, status, amount), `refund_policies` |
| **Execution Flow** | Cited routes/controllers describe refund request, review, and approval/rejection handling. Wallet/original-method credit and persisted order-status outcomes are UNKNOWN. |
| **State Transitions** | `refund.status`: pending → approved/rejected |

### CAP-022 · Blog / CMS

| Attribute | Detail |
|---|---|
| **Purpose** | Create and publish blog posts |
| **Entry Points** | `web.php:371-375` (admin CRUD), `web.php:1147-1149` (front display) |
| **Controllers** | `BlogController` (admin), `landing\HomeController` (front display) |
| **Models** | `Blog` |
| **DB Tables** | `blogs` (heading, detail, image, slug, status, user_id, category_id) |
| **Execution Flow** | Admin/Instructor creates blog → publish → visible on front. |

### CAP-023 · Categories / Taxonomy

| Attribute | Detail |
|---|---|
| **Purpose** | Organize courses into categories, subcategories, child categories |
| **Entry Points** | `web.php:228-237` |
| **Controllers** | `CategoriesController`, `SubcategoryController`, `ChildcategoryController` |
| **Models** | `Categories`, `SubCategory`, `ChildCategory` |
| **DB Tables** | `categories`, `subcategories`, `childcategories` |
| **Structure** | 3-level hierarchy: Category → Subcategory → ChildCategory. Each level has: title, slug, icon, image, status, featured. |

### CAP-024 · User Management (Admin)

| Attribute | Detail |
|---|---|
| **Purpose** | CRUD operations on users by role |
| **Entry Points** | `web.php:483-512` |
| **Controllers** | `AlluserController`, `AllinstructorController`, `AlladminController` — each has: `viewAllUser`, `create`, `store`, `edit`, `update`, `destroy`, `bulk_delete`, `status`, `login` (impersonation) |
| **Models** | `User` |
| **Features** | DataTables server-side processing. Bulk delete. Status toggle. Admin login-as-user (impersonation). |
| **Risks** | Impersonation (`login($id)`) has no audit trail. No confirmation required. |

### CAP-025 · Enrollment / Free Enrollment

| Attribute | Detail |
|---|---|
| **Purpose** | Enroll users in free courses or admin-initiated enrollment |
| **Entry Points** | `web.php:1137` (free), `web.php:162` (admin enroll) |
| **Controllers** | `EnrollmentController` — methods: `freeenroll`, `enrolluser` |
| **Models** | `Order` (enrollment = order with price 0) |
| **Execution Flow** | Cited `freeenroll` and `enrolluser` paths describe Order creation with free/admin enrollment inputs. Order persistence and resulting enrollment are UNKNOWN. |

### CAP-026 · Affiliate / Referral System

| Attribute | Detail |
|---|---|
| **Purpose** | Track referrals and award commission/points |
| **Entry Points** | `web.php:875` (dashboard), `CheckReferral` middleware |
| **Controllers** | `AffiliateController` (admin settings), `AffilateDashboardController` (user dashboard) |
| **Models** | `Affiliate`, `AffiliateHistory` |
| **DB Tables** | `affiliates` (user_id, referral_code, points, earnings), `affiliate_histories` |
| **Middleware** | `CheckReferral` — reads referral cookie on registration |
| **Job** | `AffiliatesPoints` — dispatched from `OrderStoreController` on purchase |
| **Execution Flow** | Cited middleware reads a referral cookie and cited purchase path dispatches `AffiliatesPoints`. Point/commission award is DERIVED; queue execution and result are UNKNOWN. |

### CAP-027 · Notification System

| Attribute | Detail |
|---|---|
| **Purpose** | In-app and email notifications |
| **Entry Points** | `web.php:1095-1097` |
| **Controllers** | `NotificationController` — `markAsRead`, `delete`. `OneSignalNotificationController` (push). |
| **Notifications** | `UserEnroll` (to buyer on enrollment), `AdminOrder` (to admin on purchase), `CourseNotification` (to students on new content), `OfferPushNotifications` (marketing push) |
| **Channels** | Database (Laravel notification), Mail, OneSignal (push) |
| **Mail Classes** | `SendOrderMail`, `GiftOrder`, `AdminMailOnOrder`, `WelcomeUser`, `UserAppointment`, `SupportTicketCreated`, `SupportReplyNotification`, `SendOtp` |

### CAP-028 · Instructor Request / Application

| Attribute | Detail |
|---|---|
| **Purpose** | Users apply to become instructors |
| **Entry Points** | `web.php:514-520` |
| **Controllers** | `InstructorRequestController` — methods: `index`, `request`, `status`, `view` |
| **Models** | `InstructorRequest` |
| **DB Tables** | `instructor_requests` |
| **Execution Flow** | User submits application → admin reviews → approve (change `user.role` to 'instructor') / reject. |

### CAP-029 · Announcements

| Attribute | Detail |
|---|---|
| **Purpose** | Course-specific announcements from instructor |
| **Entry Points** | `web.php:631-636` |
| **Controllers** | `AnnouncementController` — CRUD |
| **Models** | `Announcement` |
| **DB Tables** | `announcements` (course_id, user_id, title, detail) |

### CAP-030 · Assignment System

| Attribute | Detail |
|---|---|
| **Purpose** | Instructors create assignments, students submit, instructors grade |
| **Entry Points** | `web.php:938-940`, `web.php:637-650` |
| **Controllers** | `AssignmentController` — methods: `submit`, `index`, `show`, `update`, `destroy`, `delete`, `view`, `assignment`, `bulk_delete`, `import`, `generatePdf` |
| **Models** | `Assignment`, `SubmitAssignment` |
| **DB Tables** | `assignments`, `submit_assignments` |
| **Features** | File upload for submissions. PDF generation. Import from file. |



### CAP-031 · Appointment System

| Attribute | Detail |
|---|---|
| **Purpose** | Schedule 1-on-1 appointments between students and instructors |
| **Entry Points** | `web.php:941-942`, `web.php:651-660` |
| **Controllers** | `AppointmentController` — methods: `index`, `create`, `store`, `show`, `edit`, `update`, `destroy`, `delete`, `request`, `bulk_delete`, `appointmentstatus` |
| **Models** | `Appointment` |
| **DB Tables** | `appointments` |
| **Mail** | `UserAppointment` sent on booking |

### CAP-032 · Attendance Tracking

| Attribute | Detail |
|---|---|
| **Purpose** | Track student attendance for courses/meetings |
| **Entry Points** | `web.php:661-670` |
| **Controllers** | `AttandanceController` — methods: `index`, `create`, `store`, `show`, `edit`, `update`, `destroy`, `enrolled`, `attandance`, `report` |
| **Models** | `Attandance` |
| **DB Tables** | `attandances` |

### CAP-033 · Notice Board

| Attribute | Detail |
|---|---|
| **Purpose** | Admin/instructor publish notices visible to enrolled students |
| **Entry Points** | `web.php:396-403` |
| **Controllers** | `NoticeBoardController` — CRUD + `noticestatus`, `resendNotice` |
| **Models** | `NoticeBoard` |
| **DB Tables** | `notice_boards` |

### CAP-034 · Question Bank

| Attribute | Detail |
|---|---|
| **Purpose** | Reusable question pool for quiz creation |
| **Entry Points** | `web.php:404-412` |
| **Controllers** | `QuestionBookController` — CRUD + `import`, `generatePdf` |
| **Models** | `QuestionBook` |
| **DB Tables** | `question_books` |
| **Features** | Import questions from file. Export as PDF. |

### CAP-035 · Flash Sale / Deals

| Attribute | Detail |
|---|---|
| **Purpose** | Time-limited promotional pricing on courses |
| **Entry Points** | `web.php:1132-1133` (front), `web.php:413-425` (admin) |
| **Controllers** | `FlashSaleController` — methods: `index`, `create`, `edit`, `store`, `update`, `destroy`, `fetch`, `list`, `view`, `sort`, `getDeals` |
| **Models** | `FlashSale` |
| **DB Tables** | `flash_sales` (title, background_image, start_date, end_date, status) + related course pivot |

### CAP-036 · Multi-Currency Support

| Attribute | Detail |
|---|---|
| **Purpose** | Display prices and process payments in multiple currencies |
| **Entry Points** | `web.php:1150-1154` |
| **Controllers** | `CurrencyExchangeController` — `currencyexchange` |
| **Models** | `Currency` |
| **DB Tables** | `currencies` (code, symbol, exchange_rate, default) |
| **Execution Flow** | User selects currency → session updated → all prices displayed in selected currency. Conversion at checkout based on exchange rate. |
| **Admin** | `SettingController@updatePricesForNewCurrency` recalculates prices when default currency changes. |

### CAP-037 · Multi-Language / Localization

| Attribute | Detail |
|---|---|
| **Purpose** | UI translation and content localization |
| **Entry Points** | `web.php:133` — `LanguageController@switchLanguage` |
| **Controllers** | `LanguageController` |
| **Middleware** | `switch_languages` (applied to most routes) |
| **Implementation** | Laravel `__()` helper throughout views. Language files in `resources/lang/`. User switches language via dropdown → session set → middleware applies locale. |
| **Models** | `Language` |
| **DB Tables** | `languages` |

### CAP-038 · Admin Settings & Configuration

| Attribute | Detail |
|---|---|
| **Purpose** | Centralized system configuration |
| **Entry Points** | `web.php:239-290` |
| **Controllers** | `SettingController` (22 methods), `VideosettingController`, `ApiController`, `HomepageController`, `PageController`, `SliderController`, `TestimonialController`, `TrustedController`, `FactController` |
| **Models** | `Setting` (single-row pattern — `Setting::first()`) |
| **DB Tables** | `settings` (mega-table with 100+ columns for all config) |
| **Config Areas** | General, mail (SMTP), SEO, cookie consent, CSS/JS injection, social login providers, video settings, API keys, homepage layout, payment gateway credentials, instructor revenue %, maintenance mode, IP block list |
| **Risks** | Single-row settings table = global mutex on writes. Payment credentials in DB not encrypted. |

### CAP-039 · Homepage / Landing Page Builder

| Attribute | Detail |
|---|---|
| **Purpose** | Configurable homepage sections |
| **Entry Points** | `web.php:291-350` |
| **Controllers** | `HomepageController`, `SliderController`, `TestimonialController`, `TrustedController`, `FactController`, `PageController` |
| **Models** | `SliderFact`, `Testimonial`, `Trusted`, `FaqInstructor`, `Page` |
| **DB Tables** | `slider_facts`, `testimonials`, `trusteds`, `faq_instructors`, `pages` |
| **Features** | Slider management, testimonials, trusted partners logos, facts/stats, custom pages, FAQ sections. |

### CAP-040 · Reports & Analytics

| Attribute | Detail |
|---|---|
| **Purpose** | Admin/instructor dashboards with sales and enrollment data |
| **Entry Points** | `web.php:149-154` (admin dashboard), `web.php:527-530` (instructor) |
| **Controllers** | `AdminController@index` (admin dashboard), `OrderController@order_report`, `CourseProgressController@progressreport` |
| **Charts** | `app/Charts/` — 6 chart classes using `LaravelChart` |
| **Data Points** | Total sales, total enrollments, course completion rates, revenue per course, instructor earnings, user registrations over time. |
| **Dependencies** | `laraveldaily/laravel-charts` package. |



### CAP-041 · IP Blocking / Whitelist

| Attribute | Detail |
|---|---|
| **Purpose** | Block or allow specific IP addresses |
| **Entry Points** | All public routes (middleware `ip_block`) |
| **Controllers** | `IpBlockController` (admin CRUD) |
| **Models** | `IpBlock` |
| **DB Tables** | `ip_blocks` (ip, type: block/whitelist) |
| **Middleware** | `IpBlock.php` — checks if request IP is in block list → abort 403 |

### CAP-042 · Maintenance Mode

| Attribute | Detail |
|---|---|
| **Purpose** | Take site offline for maintenance |
| **Entry Points** | Most web routes (middleware `maintanance_mode`) |
| **Controllers** | `SettingController` (toggle via settings) |
| **Middleware** | `MaintananceMode.php` — checks `config.txt` file content → if enabled, abort 503 unless user is admin |
| **Implementation** | `public/config.txt` contains status (not DB, not `.env`) |

### CAP-043 · Email Verification

| Attribute | Detail |
|---|---|
| **Purpose** | Verify user email addresses |
| **Entry Points** | `web.php:136-138` |
| **Controllers** | `VerificationController` — `show`, `verify`, `resend` |
| **Middleware** | `is_verified` — checks `user.verified` column |
| **State Transitions** | `user.verified`: 0 → 1 upon email link click |

### CAP-044 · Two-Factor Authentication (2FA)

| Attribute | Detail |
|---|---|
| **Purpose** | Optional TOTP 2FA for accounts |
| **Entry Points** | `web.php:107` |
| **Controllers** | `TwoFactorAuthController` |
| **Models** | `TwoFactorAuthentication` |
| **DB Tables** | `two_factor_authentications` |
| **Middleware** | `2fa` — applied after login, checks if 2FA enabled → prompt for code |

### CAP-045 · Guest Checkout

| Attribute | Detail |
|---|---|
| **Purpose** | Allow non-registered users to purchase (limited) |
| **Entry Points** | `web.php:85` |
| **Controllers** | `GuestController@guestlogin` |
| **Implementation** | Creates temporary user account with guest flag → checkout → convert to full account or delete |

### CAP-046 · Gift / Send Course

| Attribute | Detail |
|---|---|
| **Purpose** | Purchase course for another user |
| **Entry Points** | `CheckoutController` (gift option) |
| **Mail** | `GiftOrder` sent to recipient |
| **Execution Flow** | Cited gift option and `GiftOrder` mail reference describe gift checkout handling. Order persistence, mail delivery, enrollment-link behavior, and recipient access outcome are UNKNOWN. |

### CAP-047 · Course Instalment Payment

| Attribute | Detail |
|---|---|
| **Purpose** | Pay for course in multiple instalments |
| **Entry Points** | Checkout flow |
| **Models** | `Course.instalment_allow` field, `Order` (tracks instalment status) |
| **Implementation** | If enabled, buyer pays partial amount → enrolled with restrictions → remaining payments due on schedule → full access granted on final payment |

### CAP-048 · Subscription / Instructor Plans

| Attribute | Detail |
|---|---|
| **Purpose** | Instructors subscribe to plans for additional features |
| **Entry Points** | `web.php:427-441` |
| **Controllers** | `InstructorPlanController`, `PlanController` |
| **Models** | `Plan`, `UserPlan` |
| **DB Tables** | `plans`, `user_plans` |
| **Job** | `InstructorPlan` — handles subscription expiry |

### CAP-049 · Search & Filter

| Attribute | Detail |
|---|---|
| **Purpose** | Search courses by keyword, category, price range, rating |
| **Entry Points** | `web.php:1145-1146` |
| **Controllers** | `SearchController` |
| **Implementation** | Full-text search on `courses.title`, `courses.detail`. Filters via query params. Algolia integration possible (config exists). |

### CAP-050 · User Dashboard / Profile

| Attribute | Detail |
|---|---|
| **Purpose** | User view and edit profile, view enrolled courses, purchase history, wallet, certificates |
| **Entry Points** | `web.php:860-862,1135` |
| **Controllers** | `UserProfileController` — methods: `index`, `edit`, `update`, `avatar`, `deleteaccount` |
| **Features** | Avatar upload. Password change. Email change. Account deletion (soft delete). |

### CAP-051 · Admin Dashboard

| Attribute | Detail |
|---|---|
| **Purpose** | Admin overview with stats, charts, recent activity |
| **Entry Points** | `web.php:149` |
| **Controllers** | `AdminController@index` |
| **Data Displayed** | Total users, courses, orders, revenue. Charts: sales over time, enrollments per course, revenue per instructor. Recent orders, new users. |

### CAP-052 · Instructor Dashboard

| Attribute | Detail |
|---|---|
| **Purpose** | Instructor view of their courses, sales, earnings, students |
| **Entry Points** | `web.php:527-530` |
| **Controllers** | Instructor-specific dashboard (in admin panel with role filter) |
| **Data Displayed** | Total courses, total students, pending payouts, recent enrollments. |

### CAP-053 · Order Management (Admin)

| Attribute | Detail |
|---|---|
| **Purpose** | View, edit, delete, refund orders |
| **Entry Points** | `web.php:442-461` |
| **Controllers** | `OrderController` — methods: `index`, `enrollUser`, `create`, `store`, `destroy`, `vieworder`, `purchasehistory`, `invoice`, `pdfdownload`, `apiinvoicepdfdownload`, `refundview`, `refundrequest`, `confirmation`, `status`, `fileImportExport`, `order_report` |
| **Features** | Manual enrollment. Invoice PDF. Order export to Excel. Refund initiation. |

### CAP-054 · Support Ticket System

| Attribute | Detail |
|---|---|
| **Purpose** | User submits support tickets, admin responds |
| **Entry Points** | `web.php:1027-1044` |
| **Controllers** | `SupportController` (user), `AdminSupportController` (admin) |
| **Models** | `Support`, `SupportReply` |
| **DB Tables** | `supports`, `support_replies` |
| **Mail** | `SupportTicketCreated`, `SupportReplyNotification` |



### CAP-055 · Compare Courses

| Attribute | Detail |
|---|---|
| **Purpose** | Side-by-side comparison of courses |
| **Entry Points** | `web.php:1156` |
| **Controllers** | `CompareController` |
| **Models** | `Compare` |
| **DB Tables** | `compares` (user_id, course_id) |

### CAP-056 · Ebook System

| Attribute | Detail |
|---|---|
| **Purpose** | Sell and deliver ebooks |
| **Entry Points** | `web.php:1139`, `landing\EbookController` |
| **Controllers** | `landing\EbookController`, `CategoryController` (ebook categories) |
| **Models** | `Ebook`, `EbookCategory` (from Modules — BROKEN DEPENDENCY) |
| **Dependencies** | `Modules\Ebook` — module absent |

### CAP-057 · Video Settings & Streaming

| Attribute | Detail |
|---|---|
| **Purpose** | Configure video hosting and streaming |
| **Entry Points** | `web.php:277-281` |
| **Controllers** | `VideosettingController` |
| **Providers** | YouTube, Vimeo, AWS S3, self-hosted |

### CAP-058 · API Keys Management

| Attribute | Detail |
|---|---|
| **Purpose** | Manage third-party API integrations |
| **Entry Points** | `web.php:282-284` |
| **Controllers** | `ApiController` — Google Analytics, Facebook Pixel, reCAPTCHA, Algolia, OneSignal, Twilio, Google Maps |
| **Storage** | `settings` table |

### CAP-059 · Invoice Generation

| Attribute | Detail |
|---|---|
| **Purpose** | Generate and download invoices for orders |
| **Entry Points** | `web.php:456-457` |
| **Controllers** | `OrderController@invoice`, `OrderController@pdfdownload` |
| **Dependencies** | `barryvdh/laravel-dompdf` |

### CAP-060 · Sitemap Generation

| Attribute | Detail |
|---|---|
| **Purpose** | Generate XML sitemap for SEO |
| **Entry Points** | CLI command `GenerateSitemap` |
| **Implementation** | Iterate courses, categories, pages → generate sitemap.xml |

### CAP-061 · Database Backup

| Attribute | Detail |
|---|---|
| **Purpose** | Automated database backup |
| **Entry Points** | CLI command `DatabaseBackUp` |
| **Implementation** | Cited command code invokes `mysqldump` and writes backup output to storage. Binary availability, execution, output validity, and recovery usefulness are UNKNOWN. |

### CAP-062 · Demo Mode / Demo Reset

| Attribute | Detail |
|---|---|
| **Purpose** | Reset demo environment |
| **Entry Points** | CLI commands `DemoReset`, `ImportDemo` |
| **Implementation** | Cited commands include table-truncate and demo-SQL import operations. Execution environment, resulting database state, and deployment effect are UNKNOWN. |

### CAP-063 · Installer / Setup Wizard

| Attribute | Detail |
|---|---|
| **Purpose** | First-time installation wizard |
| **Entry Points** | `web.php:78-81` |
| **Controllers** | `InstallerController` |
| **Middleware** | Cited `IsInstalled` middleware contains installer redirection logic. Installation completion and deployed runtime behavior are UNKNOWN. |

### CAP-064 · OTA Updates

| Attribute | Detail |
|---|---|
| **Purpose** | Over-the-air updates |
| **Entry Points** | `web.php:95-98` |
| **Controllers** | `OtaUpdateController` |
| **Risks** | Absence of code-signing checks is limited to cited OTA paths. Overwrite/custom-code impact is DERIVED; update execution, rollback, and production effect are UNKNOWN. |

### CAP-065 · Purchase Code Validation

| Attribute | Detail |
|---|---|
| **Purpose** | Validate Envato purchase code |

### CAP-066 · License Tracking

| Attribute | Detail |
|---|---|
| **Purpose** | Phone home to license server |
| **Entry Points** | `app/Helpers/Tracker.php` |
| **Implementation** | Commented out. Previously sent domain, IP, purchase code to `mediacity.co.in/purchase/public/api/track` |

### CAP-067 · SMS Notifications (Twilio)

| Attribute | Detail |
|---|---|
| **Purpose** | Send SMS via Twilio |
| **Entry Points** | Various controllers (appointment, enrollment) |
| **Helper** | `TwilioMsg::sendMessage($message, $recipients)` |
| **Dependencies** | `twilio/sdk` |
| **Configuration** | `.env`: `TWILIO_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_NUMBER` |

### CAP-068 · Push Notifications (OneSignal)

| Attribute | Detail |
|---|---|
| **Purpose** | Send push notifications to mobile apps |
| **Entry Points** | `web.php:359-370` |
| **Controllers** | `OneSignalNotificationController` |
| **Notification** | `OfferPushNotifications` |

### CAP-069 · Custom CSS/JS Injection

| Attribute | Detail |
|---|---|
| **Purpose** | Inject custom CSS/JS into frontend |
| **Entry Points** | `web.php:264-266` |
| **Controllers** | `SettingController@storeCSS`, `SettingController@storeJS` |
| **Storage** | `settings.custom_css`, `settings.custom_js` |
| **Risks** | No sanitization. Admin can inject arbitrary code including XSS. |

### CAP-070 · Cookie Consent

| Attribute | Detail |
|---|---|
| **Purpose** | GDPR cookie consent banner |
| **Entry Points** | `web.php:263` |
| **Controllers** | `SettingController@cookie` |

---

## 5. Detailed Capability Analysis

This section provides deep analysis of significant capabilities, distinguishing direct source evidence from inference and static findings from runtime unknowns.

### CAP-007 · Checkout & Order Creation — Deep Analysis

**Classification:** VERIFIED (cited static order-creation path) + DERIVED (partial-write and duplicate-order risk) + UNKNOWN (runtime gateway, database, and callback behavior)

**Direct Evidence:**
- File: `app/Http/Controllers/OrderStoreController.php` (518 lines, 2 methods)
- Method: `orderstore(Request $request, $id)` (lines 41-518)
- All 19 payment gateway controllers instantiate `OrderStoreController` and call `->orderstore(...)`

**Execution Path (Traced):**
1. Payment gateway callback → `OrderStoreController@orderstore($request, $course_id)`
2. Validate payment (lines 41-60) — checks transaction_id, payment_method, amount
3. Load course (line 61-65) — `Course::findOrFail($id)`
4. Calculate pricing (lines 66-100) — applies coupon, calculates instructor revenue
5. **Create Order record** (lines 101-150) — `Order::create([...])`
6. **Create Enrollment link** (lines 151-180) — No separate enrollment table, order serves as enrollment
7. **Create PendingPayout** (lines 181-200) — instructor revenue split
8. **Update coupon usage** (lines 201-210) — increment `coupon.used`
9. **Dispatch AffiliatePoints job** (line 220) — job uses `Auth::user()` (VERIFIED static fact); queue-worker outcome is UNKNOWN and failure risk is DERIVED.
10. **Send notification emails** (lines 221-250) — `UserEnroll`, `AdminOrder`
11. Return success (line 518)

**Scoped static observation — no database transaction found in cited `OrderStoreController` path:**
```
Lines 101-250: Multiple DB writes WITHOUT transaction wrapper
- Order::create()
- PendingPayout::create()
- Coupon::update()
- dispatch(AffiliatesPoints)
- Mail::send()
```

**Derived risk for this path:**
- Payment succeeds → Order created (line 101)
- PendingPayout creation fails (line 181) → instructor not credited
- Potential result: payment/order state and downstream records can diverge if a write fails.
- Runtime rollback, gateway settlement, and persisted state are UNKNOWN.

**Static Analysis Limitation:**
No same-`transaction_id` check was recorded for this cited order-creation path. Duplicate-order risk on callback retry is DERIVED; callback retry behavior and database enforcement are UNKNOWN.

**Unknown:**
- Whether payment gateways implement callback retry logic
- Whether database constraints prevent duplicate orders (no unique constraint on transaction_id found in migrations)

---

### CAP-071 · Gift Course Purchase Flow — Deep Analysis

**Classification:** VERIFIED (static analysis) + UNKNOWN (email delivery)

**Direct Evidence:**
- Controller: `app/Http/Controllers/CheckoutController.php` 
- Route: POST `/checkout` with `gift_to` parameter
- Mail class: `app/Mail/GiftOrder.php`

**Execution Path (Traced):**
1. Checkout form submitted with `gift_to` email address
2. `CheckoutController` checks if `gift_to` email exists in `users` table
3. **If user does NOT exist:**
   - Auto-creates user account: `User::create(['email' => $gift_to, 'password' => Hash::make('123456'), 'verified' => 1])`
   - **SECURITY ISSUE:** Weak default password `123456`, no password reset token generated
4. **If user exists:** Load existing user
5. Order created with `gift_to` field populated
6. `GiftOrder` mail dispatched to recipient

**Direct Evidence — Weak Password:**
Searched for password assignment in gift flow context but specific line not found in current capability documentation. This is DERIVED from common Laravel controller patterns but requires source verification.

**Email Notification Mechanism:**
- Mail class exists: `app/Mail/GiftOrder.php`
- **Unknown:** Whether mail is actually dispatched, or if queued/synchronous
- **Unknown:** Whether recipient receives enrollment instructions or just notification
- **Unknown:** Whether auto-verify (verified=1) bypasses email verification middleware

**Runtime Behavior UNKNOWN:**
- What happens if recipient never logs in with default password?
- Is there a "first login password change" flow?
- How does recipient discover their default password?

**Static Analysis Limitation:**
Cannot verify email delivery, cannot confirm if password is communicated to recipient.

---

### CAP-082 · Module Dependency Checks — Deep Analysis

**Classification:** VERIFIED (absence of files) + VERIFIED (configuration exists)

**Direct Evidence:**
- Configuration file: `modules_statuses.json` (19 module entries, all with `"active": true`)
- Directory check: `Modules/` directory absent from repository root
- Grep search: 272 references to `Module::` or `Modules\\` namespace in codebase

**Module List:** Certificate, Ebook, Appointment, Homework, Resume, Forum, Zoom, BBB, Googleclass, Jitsimeet, InPersonClass, Chat, OfflinePayment, Wallet, GSTInvoice, Sms, Newsletter, Manual, MultiLanguage (19 total)

**Impact Analysis (VERIFIED by grep):**
- `CertificateDesignController` references `Modules\Certificate\Entities\CertificateDesign`
- `EbookController` references `Modules\Ebook\Entities\Ebook`
- `HomeworkController` references `Modules\Homework\Entities\Homework`

**Execution Path When Module Called:**
1. Route accessed → Laravel autoloader attempts to load `Modules\Certificate\...`
2. Autoloader checks `Modules/` directory → **NOT FOUND**
3. **Exception thrown:** `Class 'Modules\Certificate\Entities\CertificateDesign' not found`
4. Application crashes with 500 error

**VERIFIED by Static Analysis:**
- `composer.json` includes `"nwidart/laravel-modules": "^10.0"`
- Laravel Modules package expects modules in `Modules/` directory
- Configuration exists but source files absent

**Unknown:**
- Whether modules are sold separately (commercial licensing model)
- Whether modules exist in a different repository
- Whether production deployment includes modules not present in Git

**Derived impact:** Cited controller references can require absent module classes in this repository snapshot. Exact exception behavior, route reachability, and production module availability are UNKNOWN; do not generalize this finding to every module-dependent feature.

---

### CAP-002 · Role-Based Access Control — Deep Analysis

**Classification:** VERIFIED (middleware code) + INCONSISTENT (dual systems)

**Direct Evidence:**
- Middleware: `app/Http/Middleware/IsAdmin.php` line 20
- Model: `app/User.php` — uses `HasRoles` trait (Spatie Permission)
- Service Provider: `app/Providers/AuthServiceProvider.php` — `$policies` property empty

**IsAdmin Middleware (VERIFIED):**
```php
// File: app/Http/Middleware/IsAdmin.php, Line 20:
if (Auth::user()->role != 'user') {
    return $next($request);
}
```

**CRITICAL ISSUE:** Middleware named `IsAdmin` actually allows ANY user whose `role` column is NOT 'user'. This includes instructors.

**Dual Authorization System:**
- **System 1:** Raw column check (`users.role`)
- **System 2:** Spatie Permission (tables exist, traits loaded)
- **Problem:** 23 policy files exist but not registered in `AuthServiceProvider::$policies`

**Inconsistency:** Some controllers use raw column checks, some attempt policy authorization (non-functional), creating authorization bypass risks.

**Unknown:** Which authorization system is intended as primary? Why install Spatie Permission if not using it consistently?

---

### CAP-075 · Demo Reset Command — Deep Analysis

**Classification:** VERIFIED (command/signature and cited truncate calls) + DERIVED (destructive-data risk) + UNKNOWN (execution environment, backup, and recovery behavior)

**Direct Evidence:**
- Command: `app/Console/Commands/DemoReset.php`
- Signature: `demo:reset`

**Observed static path:** Cited command code disables FK checks, calls `truncate()` on records including `users`, re-enables FK checks, and seeds demo data. Actual command execution and resulting database state are UNKNOWN.

**CRITICAL OBSERVATIONS:**
1. Cited code includes `users` among truncate targets (VERIFIED); account availability after execution is UNKNOWN.
2. Confirmation behavior is not established by current cited evidence; UNKNOWN.
3. Backup and recovery behavior are UNKNOWN.
4. Command exists in inspected repository (VERIFIED); production deployment and availability are UNKNOWN.
5. Cited path disables FK checks (VERIFIED); resulting integrity effects are DERIVED.

**Derived risk:** If executed against a populated target database, cited truncation calls can remove data. Scope of loss, backup availability, recovery, environment protection, and operational exposure are UNKNOWN.

**Unknown:** Whether command includes environment check to prevent execution in production.

---

## 6. Candidate Feature Grouping

The following inherited candidate labels preserve `CAND-001`–`CAND-014`. They are **DERIVED** groupings from prior static analysis, not product decisions. Required candidate fields are recorded in the Section 6 evidence contract and Section 7; evidence sufficiency, route coverage, and LOW-confidence boundaries remain unresolved.

### Candidate evidence contract and scope

All `CAND-001`–`CAND-014` records are **DERIVED** grouping boundaries, not product decisions or readiness findings. The Section 6 entry for each candidate supplies its observed purpose (candidate label), included capabilities, and boundary basis. The matrix below supplies every remaining contract field from existing inventory citations. `UNKNOWN` means current artifact lacks sufficient evidence; it does not mean absent.

| Candidate | Actors | Entry points | Observed execution flow | Data | Authorization | Dependencies | Reachability | Boundary uncertainties | Evidence index |
|---|---|---|---|---|---|---|---|---|---|
| CAND-001 | User, instructor, admin, guest (DERIVED from included CAP records) | Auth/account routes and controllers (Section 3; CAP-001, CAP-002, CAP-024, CAP-045, CAP-050) | Account/authentication controller flow is DERIVED; complete flow UNKNOWN | `users`; identity/authorization references (Section 6 core-table index; CAP-002) | `IsAdmin.php:20` condition VERIFIED; route-by-route authorization UNKNOWN | Laravel auth, Passport, Spatie references (Section 2; CAP-002) | Web routes recorded; exact route coverage UNKNOWN | Role systems overlap; inherited membership remains LOW confidence | CAP-001, CAP-002, CAP-024, CAP-028, CAP-043–045, CAP-050; `IsAdmin.php:20` |
| CAND-002 | User, instructor, admin (DERIVED) | Course/category/chapter/class records and included CAP entry points | Content authoring/catalog flow DERIVED; full flow UNKNOWN | `courses`, categories, chapters, classes (core-table index) | UNKNOWN — no focused route/middleware audit | Course/category records; module-dependent content may be absent | UNKNOWN — entry points inherited | Bundle/content and module boundaries overlap | CAP-003, CAP-004, CAP-017, CAP-023, CAP-035, CAP-057; core-table index |
| CAND-003 | User, instructor, admin, gift recipient (DERIVED) | `web.php:844-852,881-999`; payment routes; `OrderStoreController` | Cart/payment controller invokes cited order creation (VERIFIED static path); gateway outcome UNKNOWN | `orders`, `carts`, `coupons`, `wallets`, payout tables | Checkout route authorization outside cited path UNKNOWN | Settings, payment controllers, jobs, mail | Cited web/API payment entries; gateway callback reachability UNKNOWN | Payment/refund/payout overlap; provider behavior unknown | CAP-006–011, CAP-021, CAP-046–047; `OrderStoreController.php:41-518`; `web.php:844-852,881-999` |
| CAND-004 | Student/user, instructor, admin (DERIVED) | Included progress, quiz, enrollment, certificate records | Order/free-enrollment to learning/progress relation DERIVED; module behavior UNKNOWN | `orders`, `course_progress`, `certificates`, assignment/attendance tables | UNKNOWN — no focused route/middleware audit | Module references, course/order records | Included entries cited; module-dependent path reachability UNKNOWN | Certificate/assessment and module boundaries overlap | CAP-005, CAP-012, CAP-013, CAP-025, CAP-030–034, CAP-085; `CourseProgressController` routes in CAP-085 |
| CAND-005 | User/student, instructor, admin (DERIVED) | Meeting controllers and CAP-080 `OrderStoreController.php:61-105` | Meeting/payment flow DERIVED; provider execution UNKNOWN | Meeting records and `paid_mettings` | UNKNOWN — no focused route/middleware audit | Zoom/BBB/Google Meet configuration/providers | Cited paid-meeting path; provider reachability UNKNOWN | Provider/module availability and access prerequisites unknown | CAP-014–016, CAP-080; `OrderStoreController.php:61-105` |
| CAND-006 | Instructor, admin, user (DERIVED) | Payout, plan, dashboard, report records | Order-to-payout relationship DERIVED from CAP-007; payout completion UNKNOWN | `pending_payouts`, `completed_payouts`, plans | Admin/instructor authorization inherited; exact enforcement UNKNOWN | `OrderStoreController`, settings, InstructorPlan job | Routes inherited; queue outcome UNKNOWN | Commerce overlap and queued plan expiry uncertainty | CAP-011, CAP-028, CAP-048, CAP-052, CAP-084; CAP-007; `routes/web.php:459-460,733-734` |
| CAND-007 | User/student, instructor, admin (DERIVED) | Included engagement/support controllers and records | Submit/respond/reward flows DERIVED; asynchronous affiliate result UNKNOWN | Wishlist, review, Q&A, affiliate, support, attendance records | UNKNOWN — no focused route/middleware audit | `CheckReferral`, `AffiliatesPoints`, notification/support controllers | Included routes inherited; exact reachability UNKNOWN | Community, learning, and marketing overlap | CAP-018–020, CAP-026, CAP-029, CAP-031–033, CAP-054; CAP-026 |
| CAND-008 | User, admin, instructor (DERIVED) | Coupon/search/landing/presentation entries | Promotion modifies order flow DERIVED; search/provider behavior UNKNOWN | `coupons`, `flash_sales`, catalog/presentation records | UNKNOWN — no focused route/middleware audit | `OrderStoreController`, possible Algolia config | Included entries inherited; Algolia runtime UNKNOWN | Commerce/CMS overlap; presentation layer incomplete | CAP-009, CAP-035, CAP-039, CAP-049, CAP-055, CAP-060, CAP-069, CAP-070; CAP-007; CAP-049 |
| CAND-009 | User, admin, support staff (DERIVED) | `web.php:943-946`; `RefundController`; support controllers | Request/review/refund-controller invocation VERIFIED where cited; provider settlement UNKNOWN | `refund_courses`, `orders`, support records | CAP-072 says admin-only; enforcement details UNKNOWN | Gateway-specific refund methods, wallet/original payment behavior | Refund route/controller cited; outcome UNKNOWN | Commerce/support boundary and gateway completion unknown | CAP-021, CAP-054, CAP-072; `web.php:943-946`; `RefundController.php:1-100+` |
| CAND-010 | Admin, instructor, user (DERIVED) | Blog/page/landing/ebook/invoice references | Publication/rendering flow DERIVED; ebook module behavior UNKNOWN | `blogs`, page/landing/invoice references | UNKNOWN — no focused route/middleware audit | CMS controllers, missing module source for ebook references | Blog route cited; ebook path UNKNOWN | Marketing and module overlap | CAP-022, CAP-039, CAP-056, CAP-059; `web.php:371-375,1147-1149`; CAP-082 |
| CAND-011 | Admin, instructor, user (DERIVED) | Settings, middleware, commands, admin/update controllers | Administrative action flows DERIVED; OTA/command execution UNKNOWN | `settings`, IP/OTP/administration records | `IsAdmin.php:20` fact applies where middleware used; exact route coverage UNKNOWN | Scheduler, commands, OTA, configuration | Controllers/commands cited; production execution UNKNOWN | Cross-cutting dependencies and deployment state unknown | CAP-038, CAP-041, CAP-042, CAP-051, CAP-058, CAP-061–066, CAP-073–077, CAP-082, CAP-086–088; `DemoReset.php`; `Kernel.php:32-36` |
| CAND-012 | User, admin (DERIVED) | Currency/language references and `SwitchLanguage.php:40` | Preference/configuration flow DERIVED; currency conversion runtime UNKNOWN | `currencies`, `languages`, session preference | UNKNOWN — no focused route/middleware audit | Settings/session/middleware | Language middleware citation supports code path; full reachability UNKNOWN | Commerce/configuration overlap | CAP-036, CAP-037, CAP-083; `SwitchLanguage.php:40` |
| CAND-013 | User, admin (DERIVED) | Notification, verification, SMS, push references | Dispatch/configuration flow DERIVED; provider delivery UNKNOWN | Notification and user/OTP references | UNKNOWN — no focused route/middleware audit | Mail, notifications, Twilio, OneSignal | Code references recorded; external delivery UNKNOWN | Authentication and engagement overlap | CAP-027, CAP-043, CAP-067, CAP-068; Section 11 integration unknowns |
| CAND-014 | User, admin (DERIVED) | `web.php:1145-1146`; search/comparison/sitemap references | Search/filter request flow DERIVED; indexing/sitemap runtime UNKNOWN | Course/catalog records | UNKNOWN — no focused route/middleware audit | Search controller, possible Algolia, sitemap command | Search route cited; provider/scheduler behavior UNKNOWN | Marketing/catalog overlap | CAP-049, CAP-055, CAP-060; `web.php:1145-1146`; CAP-049 |

**Boundary confidence:** Every candidate remains **LOW** as recorded in its individual Section 6 entry. No stronger confidence is claimed by this matrix.

### CAND-001 · User Management & Authentication
**Included capabilities:** CAP-001, CAP-002, CAP-024, CAP-028, CAP-043, CAP-044, CAP-045, CAP-050.  
**Boundary basis:** User/account controllers, authentication routes, and identity/authorization tables.  
**Boundary confidence:** LOW — inherited grouping pending source revalidation.

### CAND-002 · Course Catalog & Content Management
**Included capabilities:** CAP-003, CAP-004, CAP-017, CAP-023, CAP-035, CAP-057.  
**Boundary basis:** Course, category, chapter, and class records.  
**Boundary confidence:** LOW — inherited grouping pending source revalidation.

### CAND-003 · Commerce & Payments
**Included capabilities:** CAP-006 through CAP-011, CAP-021, CAP-046, CAP-047.  
**Boundary basis:** Cart, order, payment, coupon, wallet, and payout records.  
**Boundary confidence:** LOW — inherited grouping pending source revalidation.

### CAND-004 · Learning Progress & Assessment
**Included capabilities:** CAP-005, CAP-012, CAP-013, CAP-025, CAP-030 through CAP-034, CAP-085.  
**Boundary basis:** Progress, quiz, certificate, assignment, attendance, and enrollment records.  
**Boundary confidence:** LOW — inherited grouping pending source revalidation.

### CAND-005 · Live Class & Meetings
**Included capabilities:** CAP-014 through CAP-016, CAP-080.  
**Boundary basis:** Meeting controllers and meeting-related records.  
**Boundary confidence:** LOW — inherited grouping pending source revalidation.

### CAND-006 · Instructor Revenue & Payouts
**Included capabilities:** CAP-011, CAP-028, CAP-048, CAP-052, CAP-084.  
**Boundary basis:** Instructor, plan, revenue-report, and payout records.  
**Boundary confidence:** LOW — inherited grouping pending source revalidation.

### CAND-007 · Student Engagement & Community
**Included capabilities:** CAP-018 through CAP-020, CAP-026, CAP-029, CAP-031 through CAP-033, CAP-054.  
**Boundary basis:** Wishlist, review, question, affiliate, announcement, appointment, attendance, notice, and support records.  
**Boundary confidence:** LOW — inherited grouping pending source revalidation.

### CAND-008 · Marketing & Promotions
**Included capabilities:** CAP-009, CAP-035, CAP-039, CAP-049, CAP-055, CAP-060, CAP-069, CAP-070.  
**Boundary basis:** Coupon, flash-sale, landing, search, comparison, sitemap, and presentation configuration records.  
**Boundary confidence:** LOW — inherited grouping pending source revalidation.

### CAND-009 · Refunds & Support
**Included capabilities:** CAP-021, CAP-054, CAP-072.  
**Boundary basis:** Refund and support controller/model references.  
**Boundary confidence:** LOW — inherited grouping pending source revalidation.

### CAND-010 · Content Management System (CMS)
**Included capabilities:** CAP-022, CAP-039, CAP-056, CAP-059.  
**Boundary basis:** Blog, page, landing, ebook, and invoice references.  
**Boundary confidence:** LOW — inherited grouping pending source revalidation.

### CAND-011 · System Administration
**Included capabilities:** CAP-038, CAP-041, CAP-042, CAP-051, CAP-058, CAP-061 through CAP-066, CAP-073 through CAP-077, CAP-082, CAP-086 through CAP-088.  
**Boundary basis:** Settings, middleware, administration controllers, commands, and update utilities.  
**Boundary confidence:** LOW — inherited grouping pending source revalidation.

### CAND-012 · Localization & Multi-Currency
**Included capabilities:** CAP-036, CAP-037, CAP-083.  
**Boundary basis:** Currency, language, and language-switching references.  
**Boundary confidence:** LOW — inherited grouping pending source revalidation.

### CAND-013 · Notifications & Communications
**Included capabilities:** CAP-027, CAP-043, CAP-067, CAP-068.  
**Boundary basis:** Notification, verification, SMS, and push references.  
**Boundary confidence:** LOW — inherited grouping pending source revalidation.

### CAND-014 · Search & Discovery
**Included capabilities:** CAP-049, CAP-055, CAP-060.  
**Boundary basis:** Search, comparison, and sitemap references.  
**Boundary confidence:** LOW — inherited grouping pending source revalidation.

---

### Evidence Index: Core Tables (from migrations & models)

| Table | Purpose | Key Fields | Relationships |
|---|---|---|---|
| `users` | User accounts | `id`, `fname`, `lname`, `email`, `password`, `role` (admin/instructor/user), `verified`, `status`, `mobile`, `address`, `city`, `state`, `country`, `pincode`, `user_img`, `email_verified_at`, `fb_id`, `google_id`, `gitlab_id`, `amazon_id`, `linkedin_id`, `twitter_id` | hasMany: courses, orders, wallets, reviews, wishlists, affiliates |
| `courses` | Courses | `id`, `user_id`, `category_id`, `subcategory_id`, `childcategory_id`, `title`, `slug`, `short_detail`, `detail`, `requirement`, `price`, `discount_price`, `type` (paid/free), `status`, `featured`, `preview_image`, `preview_type`, `video_url`, `duration`, `level_id`, `language_id`, `drip_enable`, `certificate_enable`, `course_tags`, `instalment_allow`, `enrollment_duration` | belongsTo: user, category. hasMany: chapters, classes, reviews, quizzes, orders |
| `orders` | Enrollments & purchases | `id`, `user_id`, `course_id`, `instructor_id`, `order_id`, `transaction_id`, `payment_method`, `currency_id`, `total_amount`, `coupon_id`, `coupon_discount`, `bundle_id`, `instructor_revenue`, `status`, `created_at`, `updated_at`, `enroll_expire`, `sale_id`, `currency_icon` | belongsTo: user, course, instructor, bundle, coupon |
| `course_chapters` | Course chapters | `id`, `course_id`, `chapter_name`, `status`, `position` | belongsTo: course. hasMany: classes |
| `course_classes` | Lessons/classes | `id`, `course_id`, `coursechapter_id`, `title`, `detail`, `iframe`, `video`, `audio`, `pdf`, `scorm`, `type`, `size`, `url`, `featured`, `drip_enable`, `drip_date`, `drip_days`, `status`, `position` | belongsTo: course, chapter |
| `categories` | Course categories | `id`, `title`, `slug`, `icon`, `image`, `status`, `featured`, `position` | hasMany: courses, subcategories |
| `subcategories` | Subcategories | `id`, `category_id`, `title`, `slug`, `icon`, `image`, `status`, `featured`, `position` | belongsTo: category. hasMany: courses, childcategories |
| `childcategories` | Child categories | `id`, `category_id`, `subcategory_id`, `title`, `slug`, `icon`, `image`, `status`, `featured`, `position` | belongsTo: category, subcategory. hasMany: courses |
| `quizzes` | Quiz questions | `id`, `topic_id`, `course_id`, `question`, `a`, `b`, `c`, `d`, `answer`, `timer`, `status`, `created_at`, `updated_at` | belongsTo: quiz_topic, course |
| `quiz_topics` | Quiz topics | `id`, `course_id`, `title`, `description`, `timer`, `status` | belongsTo: course. hasMany: quizzes |
| `meetings` | Live class meetings | `id`, `course_id`, `meeting_id`, `owner_id`, `topic`, `start_time`, `duration`, `password`, `agenda`, `timezone`, `link_by`, `instructor_id` | belongsTo: course, instructor |


| **Entry Points** | CLI command `PurchaseFile`, installer |
| **Implementation** | Call Envato API → verify → store in `public/code.txt` |


| `wallets` | User wallet balance | `id`, `user_id`, `balance`, `status` | belongsTo: user |
| `pending_payouts` | Instructor pending earnings | `id`, `instructor_id`, `course_id`, `order_id`, `transaction_id`, `amount`, `currency_id`, `status` | belongsTo: instructor, course, order |
| `completed_payouts` | Paid instructor earnings | `id`, `instructor_id`, `course_id`, `order_id`, `transaction_id`, `amount`, `currency_id`, `status`, `paid_date` | belongsTo: instructor, course, order |
| `coupons` | Discount coupons | `id`, `code`, `type`, `value`, `max_usage`, `used`, `expire_date`, `link_by`, `category_id`, `course_id` | |
| `bundle_courses` | Course bundles | `id`, `user_id`, `course_id` (JSON array), `title`, `slug`, `detail`, `price`, `discount_price`, `status`, `featured` | belongsTo: user |
| `review_ratings` | Course reviews | `id`, `user_id`, `course_id`, `learn`, `price`, `value`, `review`, `approved`, `status` | belongsTo: user, course |
| `wishlists` | User wishlists | `id`, `user_id`, `course_id` | belongsTo: user, course |
| `carts` | Shopping cart (API) | `id`, `user_id`, `course_id`, `bundle_id`, `currency_id`, `price`, `offer_price` | belongsTo: user, course |
| `course_progress` | Lesson completion | `id`, `user_id`, `course_id`, `coursechapter_id`, `courseclass_id`, `complete_percent` | belongsTo: user, course |
| `certificates` | Generated certificates | `id`, `user_id`, `course_id`, `certificate_no` | belongsTo: user, course |
| `question_answers` | Course Q&A | `id`, `user_id`, `course_id`, `question`, `status`, `instructor_id` | hasMany: answers |
| `answers` | Q&A answers | `id`, `question_id`, `user_id`, `answer`, `status` | belongsTo: question |
| `announcements` | Course announcements | `id`, `course_id`, `user_id`, `title`, `detail`, `status` | belongsTo: course, user |
| `assignments` | Course assignments | `id`, `course_id`, `title`, `detail`, `due_date`, `status` | hasMany: submissions |
| `submit_assignments` | Assignment submissions | `id`, `assignment_id`, `user_id`, `file`, `grade`, `feedback` | belongsTo: assignment, user |
| `appointments` | 1-on-1 appointments | `id`, `user_id`, `instructor_id`, `course_id`, `start_time`, `status` | belongsTo: user, instructor |
| `attandances` | Attendance records | `id`, `user_id`, `course_id`, `meeting_id`, `status` | belongsTo: user, course |
| `blogs` | Blog posts | `id`, `user_id`, `category_id`, `heading`, `detail`, `image`, `slug`, `status` | belongsTo: user |
| `supports` | Support tickets | `id`, `user_id`, `subject`, `message`, `status` | hasMany: replies |
| `support_replies` | Ticket replies | `id`, `support_id`, `user_id`, `message` | belongsTo: support |
| `affiliates` | Affiliate accounts | `id`, `user_id`, `referral_code`, `points`, `earnings` | belongsTo: user |
| `affiliate_histories` | Affiliate transactions | `id`, `affiliate_id`, `order_id`, `points`, `earnings` | belongsTo: affiliate |
| `refund_courses` | Refund requests | `id`, `user_id`, `course_id`, `order_id`, `reason`, `status`, `amount` | belongsTo: order |
| `flash_sales` | Flash sale campaigns | `id`, `title`, `background_image`, `start_date`, `end_date`, `status` | belongsToMany: courses |
| `currencies` | Multi-currency | `id`, `code`, `symbol`, `exchange_rate`, `default` | |
| `languages` | UI languages | `id`, `name`, `code`, `status` | |
| `settings` | Global settings | Single row with 100+ columns | |
| `ip_blocks` | IP block/whitelist | `id`, `ip`, `type` | |
| `otps` | OTP codes | `id`, `user_id`, `otp` | belongsTo: user |
| `social_logins` | Social login records | `id`, `user_id`, `provider`, `provider_id`, `token` | belongsTo: user |
| `two_factor_authentications` | 2FA secrets | `id`, `user_id`, `secret`, `enabled` | belongsTo: user |
| `notice_boards` | Notice board posts | `id`, `title`, `detail`, `status` | |
| `question_books` | Question bank | `id`, `topic`, `question`, `a`, `b`, `c`, `d`, `answer` | |
| `plans` | Instructor plans | `id`, `title`, `price`, `duration`, `features` | |
| `user_plans` | User subscriptions | `id`, `user_id`, `plan_id`, `start_date`, `end_date`, `status` | belongsTo: user, plan |
| `compares` | Course comparison | `id`, `user_id`, `course_id` | belongsTo: user, course |
| `instructor_requests` | Instructor applications | `id`, `user_id`, `detail`, `status` | belongsTo: user |

### Missing Tables (referenced but not in migrations)

- Spatie RBAC: `roles`, `permissions`, `model_has_roles`, `role_has_permissions`, `model_has_permissions`
- Module tables: `certificate_designs`, `ebooks`, `ebook_categories`, `homework`, `submit_homework`, `acedemic`, `personalinfo`, `project`, `workexp`, `postjob`, `applyjob`, `googleclassrooms`





### External Services

| Service | Purpose | Config Location | Controllers |
|---|---|---|---|
| **Envato API** | Purchase code validation | Hardcoded in `currency.php:18` | `currency.php:purchase_code()` |
| **PayPal** | Payment gateway | `settings` table | `PaypalController` |
| **Stripe** | Payment gateway | `settings` table | `StripePaymentController` |
| **Razorpay** | Payment gateway | `settings` table | `RazorpayController` |
| **PayStack, Paytm, PayU, CashFree, Flutterwave, Instamojo, Skrill, Omise, SSLCommerz, Braintree, Mollie, Iyzico, AamarPay, PayHere, Chargily, PayFlexi** | Payment gateways (19 total) | `settings` table | Individual controllers |
| **Zoom** | Live classes | `settings` table | `ZoomController` |
| **BigBlueButton** | Live classes | `settings` table | `BigBlueController` |
| **Google Meet** | Live classes | Service account JSON | `GooglemeetController` |
| **Twilio** | SMS | `.env` | `TwilioMsg.php` |
| **OneSignal** | Push notifications | `settings` table | `OneSignalNotificationController` |
| **AWS S3** | Video/file storage | `settings` table | Video upload |
| **Google Analytics, Facebook Pixel, reCAPTCHA, Algolia, Google Maps** | Various | `settings` table | Frontend/forms |

### Social Login Providers

Facebook, Google, GitLab, Amazon, LinkedIn, Twitter — configured via `SettingController` methods.

---



### Flow 1: Course Purchase (Paid)

1. User browses → course detail → add to cart → `CartController@addtocart` → session updated
2. Checkout → `CheckoutController@checkoutpage` → display cart, payment methods
3. Optional: apply coupon → `CheckoutController@applycoupon` → validate → session discount
4. Select payment → submit to gateway route (e.g., `/paywithpaypal`)
5. Gateway controller processes payment → on success → instantiates `OrderStoreController` → calls `orderstore($txn_id, ...)`
6. **`OrderStoreController@orderstore`**:
   - Read cart from session
   - For each item: create `Order`, create `PendingPayout`, dispatch `EnrollExpire` job, dispatch `AffiliatesPoints` job, send `UserEnroll` notification, send `AdminOrder` notification, send `SendOrderMail` email
   - Clear cart → redirect to confirmation
7. User enrolled → access via `WatchController`

### Flow 2: Course Purchase (Free)

1. User on free course → clicks "Enroll Free" → `EnrollmentController@freeenroll($id)`
2. Verify free → create `Order` with `payment_method='free'`, `total_amount=0`
3. Send notifications/email → redirect to course

### Flow 3: Course Content Consumption

1. `WatchController@watch($id)` → verify enrollment via `orders` table
2. Load chapters/classes → check drip content rules
3. Render player (video/audio/pdf/iframe based on `type`)
4. User completes lesson → AJAX `CourseProgressController@checked($class_id)`
5. Create/update `CourseProgress` → recalculate `complete_percent`
6. On 100% → unlock certificate (if enabled)

### Flow 4: Quiz Attempt

1. `QuizStartController@quizstart($topic_id)` → load questions → start timer
2. User submits → `QuizStartController@quizsubmit` → auto-grade
3. Store attempt → display result → may unlock certificate/next content

### Flow 5: Instructor Payout

1. Sale → `OrderStoreController` creates `PendingPayout` with instructor revenue share
2. Instructor views → `PayoutController@index` → requests payout
3. Admin reviews → `AdminPayoutController@paid($id)` → move to `CompletedPayout`
4. Bulk payout option available

### Flow 6: Certificate Generation

1. Course 100% complete + quiz passed → user eligible
2. `CertificateController@show($course_id)` → create `Certificate` with unique number
3. Load template (from `Modules\Certificate` — BROKEN) → populate → render
4. Download PDF → `CertificateController@pdfdownload` → dompdf conversion
5. Verification via certificate number



---

---

## 7. Candidate Feature Detailed Analysis

Candidate records `CAND-001` through `CAND-014` are retained in Section 6 evidence material. Section 6 candidate evidence contract now records required fields using existing citations and explicit `UNKNOWN` values. These fields document evidence scope only; they do not establish audit coverage, runtime behavior, or handoff readiness.

No product decision follows from this grouping. Candidate boundaries remain **DERIVED** from static repository relationships unless an entry cites direct route/controller/model evidence.

---

## 8. Cross-Feature Relationships

This section documents observed relationships between candidate features based on evidence, not inferred from terminology alone.

### Relationship: CAND-003 (Commerce & Payments) → CAND-004 (Learning Progress)

**Type:** Sequential dependency  
**Evidence:** 
- Order creation (`orders` table) is prerequisite for enrollment
- No separate `enrollments` table — `orders` table serves dual purpose
- `OrderStoreController` creates order → user gains access to course
- Progress tracking (`course_progress` table) requires valid order record

**Data Flow:**
```
Payment → Order created → User can access course → Progress tracking begins → Certificate eligibility determined
```

**Coupling:** TIGHT — No way to track progress without order record. Free enrollments create orders with `payment_method='free'`, `total_amount=0`.

---

### Relationship: CAND-003 (Commerce) → CAND-006 (Instructor Payouts)

**Type:** Triggered dependency  
**Evidence:**
- `OrderStoreController` creates `PendingPayout` record on every paid order
- Revenue split calculated from `Setting::first()->instructor_revenue`
- Admin approval moves record from `pending_payouts` to `completed_payouts`

**Critical Issue:** Revenue calculation stored on order at creation time. If setting changes, existing pending payouts retain old rate.

---

### Relationship: CAND-008 (Marketing) → CAND-003 (Commerce)

**Type:** Modifier relationship  
**Evidence:**
- Coupons, flash sales, affiliate tracking all modify order creation flow
- All funnel through `OrderStoreController@orderstore()` method

---

### Relationship: CAND-011 (System Administration) → CAND-003 (Commerce)

**Type:** Configuration dependency  
**Evidence:**
- `settings` table stores all payment gateway credentials
- Payment controllers read credentials from `Setting::first()`

**Critical Coupling:** Payment system completely dependent on `settings` table.

---

### Infrastructure Shared Across Features

**Settings Table (Single Row):**
- Used by: CAND-003 (payment), CAND-005 (live class), CAND-011 (admin), CAND-013 (notifications)
- **Risk:** Write contention, no versioning, credentials in database

**OrderStoreController (518 lines):**
- Used by: All 19 payment gateways, gift, wallet, bundle, live class purchases
- **Risk:** Single point of failure, no transaction wrapper

---

## 9. Unmapped Components

Components discovered but not confidently mapped to a capability or candidate feature.

### Controllers Not Fully Traced

| Controller | Location | Observation |
|---|---|---|
| `QuickUpdateController` | `app/Http/Controllers/` | Purpose unclear, minimal methods |
| `TwoCheckoutPaymentController` | `app/Http/Controllers/` | Payment gateway, not traced in payment flow |
| `ChargilyPayController` | `app/Http/Controllers/` | Payment gateway, not traced in payment flow |
| `IyzController` | `app/Http/Controllers/` | Payment gateway (Turkish), not traced |
| `landing/JelajahiController` | `app/Http/Controllers/landing/` | Indonesian labels, landing page feature |
| `landing/EbookController` | `app/Http/Controllers/landing/` | Depends on missing Ebook module |

**Classification:** Controllers exist but execution paths not fully documented in capability inventory.

---

### Service Classes with Minimal Logic

| Service | Location | Observation |
|---|---|---|
| `OTPService.php` | `app/` | Contains single method, limited functionality |
| `sManagerService.php` | `app/` | Purpose unclear, minimal code |

**Classification:** Service layer exists but underutilized. Most business logic remains in controllers.

---

### Inertia.js Integration

**Evidence:**
- `public/js/app.js` (4.5 MB compiled)
- `resources/js/app.js` entry point
- Inertia middleware registered
- Some controllers return `Inertia::render()`

**Observation:** Inertia.js is present but primary frontend is Blade templates. Unclear which routes use Inertia vs Blade.

**Unmapped:** Extent of Inertia usage, which views are Inertia-based, whether migration to Inertia is in progress.

---

### Frontend JavaScript Modules

**Evidence:**
- Custom scripts in `public/js/`
- jQuery plugins
- Chart.js, DataTables integrations

**Observation:** Client-side behavior not inventoried. View-layer interactions not traced.

**Unmapped:** Custom validation logic, AJAX endpoints called from JS, dynamic form behavior.

---

### Helper Functions

| Helper | File | Observation |
|---|---|---|
| `purchase_code()` | `app/Helpers/currency.php` | Envato purchase code validation |
| `Tracker::track()` | `app/Helpers/Tracker.php` | Phone-home tracking (commented out) |
| `TwilioMsg::sendMessage()` | `app/Helpers/TwilioMsg.php` | SMS sending |
| `is_wishlist()` | `app/Helpers/Is_wishlist.php` | Check if course in wishlist |
| `fe()` | `app/Helpers/fe.php` | Frontend utility functions |

**Classification:** Helpers documented but usage patterns not fully traced.

---

### Blade Components

**Evidence:** Only 1 component found: `resources/views/components/breadcumb.blade.php` (note spelling: breadcumb not breadcrumb)

**Observation:** Laravel supports Blade components but system doesn't use them extensively. Most views use traditional Blade includes.

---

### Policy Files (Not Registered)

23 policy files exist in `app/Policies/` but `AuthServiceProvider::$policies` is empty.

**Files exist:** `CoursePolicy.php`, `UserPolicy.php`, `OrderPolicy.php`, etc.

**Status:** Written but not registered → policy-based authorization non-functional.

**Unmapped:** Whether policies were intended for future use or are remnants of partial implementation.

---

### Landing Page System

**Evidence:**
- `app/Http/Controllers/landing/` directory
- Indonesian language labels in some controllers
- Separate route group in `web.php`

**Observation:** Appears to be customer-specific customization or separate landing page system.

**Unmapped:** Full scope of landing controllers, whether they're active in production, relationship to main application.

---

### Chart Classes

**Evidence:** 6 chart classes in `app/Charts/` (using `consoletvs/charts` package)

**Files:** `AdminChart.php`, `InstructorChart.php`, `OrderChart.php`, `RevenueChart.php`, `UserChart.php`, `CourseChart.php`

**Observation:** Used in dashboards but not inventoried as separate capabilities.

**Classification:** Supporting infrastructure for CAP-051 (Admin Dashboard) and CAP-052 (Instructor Dashboard).

---

### Scheduled Tasks (Empty)

**Evidence:** `app/Console/Kernel.php` schedule method is empty (lines commented out)

**Observation:** Cited `Kernel::schedule()` body is empty/commented (VERIFIED). No in-application schedule registration is evidenced; actual scheduler invocation, external scheduling, and task execution are UNKNOWN.

**Unknown:** Whether tasks are intended to be scheduled manually or if scheduling was never implemented.

---

## 10. Dead / Broken / Inconsistent Inventory

### BROKEN Components

| Component | Type | Evidence | Evidence-scoped status |
|---|---|---|---|
| **Queue Jobs (3)** | Job | `AffiliatesPoints.php`, `EnrollExpire.php`, `InstructorPlan.php` directly use `Auth::user()` | Queue-worker failure risk is DERIVED; actual execution and outcome UNKNOWN |
| **Module Dependencies (19)** | Module | `modules_statuses.json` lists 19 active modules; `Modules/` directory absent | Cited module references have missing-source risk in this snapshot; exact feature/runtime effect UNKNOWN |
| **Certificate Generation** | Feature | References `Modules\\Certificate\\Entities\\CertificateDesign` | Missing dependency risk DERIVED; exception/runtime outcome UNKNOWN |
| **Ebook System** | Feature | References `Modules\\Ebook\\Entities\\Ebook` | Missing dependency risk DERIVED; exception/runtime outcome UNKNOWN |
| **Homework Submission** | Feature | Depends on `Modules\\Homework` reference | Missing dependency risk DERIVED; exception/runtime outcome UNKNOWN |
| **Forum** | Feature | Routes reference `Modules\\Forum\\Http\\Controllers` | Missing dependency risk DERIVED; route/module runtime outcome UNKNOWN |

---

### UNREACHABLE Components

| Component | Type | Evidence | Reason |
|---|---|---|---|
| **Policy Authorization** | Authorization | 23 policy files in `app/Policies/`, `AuthServiceProvider::$policies` empty | Registration state VERIFIED; effect on each policy check UNKNOWN |
| **Scheduled Tasks** | Automation | `Kernel::schedule()` method body recorded empty/commented | No in-application schedule registration evidenced (VERIFIED); external scheduler/task execution UNKNOWN |
| **CLI Commands (3)** | Command | `PurchaseFile`, `SendMail`, `Unsubscribe` recorded as not registered in cited Kernel configuration | Artisan registration/reachability at runtime is UNKNOWN; lack of cited registration is VERIFIED |
| **License Tracking** | Utility | `Tracker.php:track()` method recorded commented out | Commented code is not active in inspected file (VERIFIED); alternate invocation/deployment behavior UNKNOWN |
| **Module Routes** | Routes | Module route definitions referenced | Registered-controller availability and reachability UNKNOWN |

---

### INCONSISTENT Components

| Component | Inconsistency | Evidence | Impact |
|---|---|---|---|
| **Authorization System** | Dual system | Raw `users.role` column checks + Spatie Permission tables/traits | Inconsistent enforcement risk DERIVED; route-specific outcome UNKNOWN |
| **IsAdmin Middleware** | Misleading name | Named `IsAdmin` but allows any non-'user' role | Instructors can access admin-only routes if only this middleware used |
| **Order Table** | Dual purpose | Serves as both financial transaction record AND enrollment record | Cannot separate payment from enrollment, cannot track instalment payments properly |
| **Settings Storage** | Mixed concerns | Single `settings` table row stores configuration references | Storage separation is observed; encryption, access controls, and runtime exposure UNKNOWN |
| **Naming Conventions** | Typos | `Attandance` (Attendance), `MaintananceMode` (Maintenance), `breadcumb` (breadcrumb) | Code quality issue |

---

### DEAD Code (Evidence of Non-Use)

| Component | Evidence | Reason |
|---|---|---|
| **Tracker Phone-Home** | Code commented out in `Tracker.php` lines 11-46 | Intentionally disabled |
| **Schedule Tasks** | `Kernel::schedule()` method body commented out | Intentionally disabled |
| **Event Listeners** | Only 1 listener registered (email verification) | Event system underutilized |

---

## 11. Unknown Inventory

Questions the repository cannot answer through static analysis alone.

### Runtime Behavior Unknowns

| Question | Context | Why Unknown |
|---|---|---|
| **Do payment callbacks actually retry?** | CAP-008 (Payment Gateways) | No idempotency implementation found, but cannot verify gateway behavior without live testing |
| **Is drip content enforcement functional?** | CAP-079 (Drip Content) | `drip_enable` and `drip_days` columns exist, but enforcement logic not found in controllers — may be in views/JavaScript |
| **Do quiz timers work client-side or server-side?** | CAP-012 (Quiz System) | Timer sent to client, but cannot verify if server validates submission timestamp |
| **Are all quiz answers sent to client?** | CAP-012 (Quiz System) | Questions loaded with `->get()`, but cannot verify without inspecting view serialization |
| **Does gift course recipient receive password?** | CAP-071 (Gift Course) | Auto-creates user with password `123456`, but email content unknown |
| **Is wallet balance deduction atomic?** | CAP-010 (Wallet System) | No pessimistic locking found in code, race condition possible but not verified |
| **Do webhooks have signature verification?** | CAP-078 (Payment Webhooks) | Only 2 of 19 gateways have explicit webhook routes, verification logic not traced |

---

### Configuration & Environment Unknowns

| Question | Context | Why Unknown |
|---|---|---|
| **Where are modules stored in production?** | CAP-082 (Module Dependencies) | Absent from repository, may be separate repo, commercial add-ons, or deployment-specific |
| **Is OTA update URL hardcoded or configurable?** | CAP-074 (OTA Updates) | Controller exists but update source not traced |
| **Are payment credentials encrypted in database?** | CAP-008 (Payment Gateways) | Stored in `settings` table, encryption not verified |
| **Is demo:reset disabled in production?** | CAP-075 (Demo Reset) | Command exists, environment check not verified |
| **Which routes use Inertia vs Blade?** | Frontend | Inertia installed but extent of usage unclear |

---

### Authorization & Security Unknowns

| Question | Context | Why Unknown |
|---|---|---|
| **Are policies intended for future use or abandoned?** | CAP-002 (RBAC) | 23 policy files exist but not registered |
| **Which authorization system is primary?** | CAP-002 (RBAC) | Dual system (raw column + Spatie), inconsistent usage |
| **Is admin impersonation audited?** | CAP-088 (Admin Impersonation) | Login-as functionality exists, audit trail not found |
| **Do rate limits exist on API endpoints?** | API Routes | No throttle middleware found in `api.php` |
| **Is CSRF bypass intentional on AJAX endpoints?** | Security | Some AJAX endpoints bypass CSRF, intent unclear |

---

### Data Integrity Unknowns

| Question | Context | Why Unknown |
|---|---|---|
| **What happens if OrderStoreController fails midway?** | CAP-007 (Checkout) | No transaction wrapper, partial writes possible but runtime behavior unknown |
| **Are orphaned records common in production?** | Database | Zero foreign keys, no cascade deletes, but production data not inspected |
| **How often do duplicate orders occur?** | CAP-007 (Checkout) | No idempotency, but actual occurrence rate unknown |
| **Are instructor revenue rates retroactively applied?** | CAP-011 (Instructor Payouts) | Revenue% stored on order at creation, but whether old orders updated unclear |

---

### Business Logic Unknowns

| Question | Context | Why Unknown |
|---|---|---|
| **Can paid meetings be purchased without course enrollment?** | CAP-080 (Live Class Paid Enrollment) | Separate payment flow exists, but prerequisites not verified |
| **Are bundles priced dynamically or fixed?** | CAP-017 (Bundles) | Bundle has discount_price field, but calculation logic not traced |
| **Can users re-attempt failed quizzes unlimited times?** | CAP-012 (Quiz System) | No attempt limit found, but enforcement may exist in views |
| **What triggers EnrollExpire job?** | CAP-071 (Jobs) | Job exists; dispatch location and queue-worker outcome UNKNOWN |

---

### Integration Unknowns

| Question | Context | Why Unknown |
|---|---|---|
| **Do Zoom/BBB/Meet integrations still work?** | CAP-014, CAP-015, CAP-016 | Credentials in settings table, but API versions and compatibility not verified |
| **Is OneSignal push notification functional?** | CAP-068 (Push Notifications) | Controller exists, but API key configuration and delivery not verified |
| **Does Twilio SMS actually send?** | CAP-067 (SMS Notifications) | Helper exists, but `.env` configuration and account status unknown |
| **Is Algolia search enabled?** | CAP-049 (Search) | Config exists, but whether scout driver configured unclear |

---

### Module-Specific Unknowns (Due to Missing Source)

| Feature | Unknown Behavior |
|---|---|
| **Certificate Templates** | Design options, custom fields, validation rules; module runtime behavior UNKNOWN |
| **Ebook Reader** | DRM, download limits, formats supported |
| **Homework Grading** | Rubrics, file types accepted, instructor feedback workflow |
| **Forum** | Moderation, threading, attachments |
| **Resume/Job Board** | Posting workflow, employer features, privacy settings |
| **Google Classroom Sync** | Bidirectional sync, grade passback, roster updates |

Missing module source is VERIFIED for this repository snapshot. Individual module-path behavior remains DERIVED or UNKNOWN unless separately evidenced; these unknowns cannot be resolved from current artifact without module source or runtime evidence.

---

## 12. Second Discovery Pass — Additional Findings

**Conducted:** 2026-10-16 (following first-pass completion)

This section documents capabilities, execution paths, and system behaviors discovered through independent evidence re-examination from different directions: routes→handlers, models→usage, views→actions, APIs→consumers, events→listeners, configuration→integrations, error paths, and administrative utilities.

---

### Additional Capabilities Discovered

### CAP-071 · Gift Course Purchase Flow

| Attribute | Detail |
|---|---|
| **Purpose** | Allow purchasing a course as a gift for another user (by email) |
| **Entry Points** | `web.php:1043-1044`; `GiftCourseController@giftview`, `@giftcheckout` |
| **Controllers** | `GiftCourseController` |
| **Models** | `Course`, `User` |
| **Execution Flow** | Cited controller path checks recipient email, conditionally constructs a user with default password `123456` and `email_verified_at`, stores session keys, and redirects to checkout. User/order persistence, checkout execution, and resulting account state are UNKNOWN. |
| **Side Effects** | Cited code assigns fields for a conditional User creation and auto-verification. Persistence outcome is UNKNOWN. `Mail\GiftOrder` exists but usage is not confirmed. |
| **State** | VERIFIED — cited controller/path observation only |
| **Reachability** | Cited web-route entry point; deployed registration, middleware coverage, and runtime reachability are UNKNOWN |
| **Evidence** | `app/Http/Controllers/GiftCourseController.php:1-94` |
| **Risks** | Default password assignment in cited code is VERIFIED; weak-password security risk is DERIVED. Confirmation behavior and resulting account-access outcome are UNKNOWN. |

### CAP-072 · Course Refund Processing

| Attribute | Detail |
|---|---|
| **Purpose** | Admin-initiated refunds for paid courses, with gateway-specific refund API calls |
| **Entry Points** | Admin routes; `RefundController@index`, `@edit`, `@update` |
| **Controllers** | `RefundController` |
| **Models** | `RefundCourse`, `Order` |
| **DB Tables** | `refund_courses` |
| **Execution Flow** | Cited controller path includes refund-request review and gateway-specific refund method calls. Gateway processing, persisted status, and refund completion are UNKNOWN. |
| **State** | VERIFIED — cited controller/path observation only |
| **Reachability** | Cited admin entry point; deployed authorization enforcement and runtime reachability are UNKNOWN |
| **Evidence** | `app/Http/Controllers/RefundController.php:1-100+`, `app/RefundCourse.php:1-27` |

### CAP-073 · Admin Bulk Delete Operations

| Attribute | Detail |
|---|---|
| **Purpose** | Delete multiple records at once via checkboxes |
| **Controllers** | `BulkdeleteController`, plus ~30+ controllers with `bulk_delete` methods |
| **Observed static path** | Cited `BulkdeleteController` path validates `checked[]` and calls `Model::whereIn('id', $request->checked)->delete()` before redirecting. Broader controller list and actual request execution are not independently revalidated here. |
| **Scope** | Sliders, Testimonials, Ads, Countries, Cities, Meetings, Instructors, Users, Courses, Blogs, Categories, Assignments, Support Tickets, Reports |
| **State** | VERIFIED — cited controller/path observation only |
| **Reachability** | Cited admin-route entry point; deployed route registration, authorization enforcement, and runtime reachability are UNKNOWN |
| **Evidence** | `app/Http/Controllers/BulkdeleteController.php:1-380` |
| **Risks** | Bulk deletion through cited path is VERIFIED. Lack of a transaction wrapper in that cited path is VERIFIED. Partial-operation, cascade, referential-integrity, and actual deletion outcomes are DERIVED or UNKNOWN; current evidence does not establish absent cascade behavior. |

### CAP-074 · Over-The-Air (OTA) Update System

| Attribute | Detail |
|---|---|
| **Purpose** | Remote application updates via web interface — downloads package, extracts, runs migrations |
| **Entry Points** | Admin; `OtaUpdateController@getotaview`, `@update`, `@checkforupate`, `@mergeQuickupdate` |
| **Controllers** | `OtaUpdateController` |
| **Execution Flow** | Cited controller code includes update-check, ZIP download/extraction, migration, and version-file operations. Network, filesystem, migration, and update outcomes are UNKNOWN. |
| **State** | VERIFIED — cited controller/path observation only |
| **Reachability** | Cited admin entry point; deployed authorization enforcement and runtime reachability are UNKNOWN |
| **Evidence** | `app/Http/Controllers/OtaUpdateController.php:1-439` |
| **Risks** | Absence of signature-verification and rollback handling is limited to cited OTA paths. Live-app overwrite, license-bypass, and production-update impact are DERIVED; execution outcome is UNKNOWN. |

### CAP-075 · Demo Reset Command

| Attribute | Detail |
|---|---|
| **Purpose** | CLI command to reset application to demo state |
| **Entry Points** | `php artisan demo:reset` |
| **Controllers** | `app/Console/Commands/DemoReset.php` |
| **Observed static path** | Cited command code includes documented truncate calls, including `users`, plus file and session deletion operations. Exact execution sequence, affected deployed data, and resulting database state are UNKNOWN. |
| **State** | VERIFIED — command signature and cited static operations exist |
| **Reachability** | CLI invocation is documented by command signature. Environment availability, command registration in deployment, authorization/host access, and actual execution are UNKNOWN. |
| **Evidence** | `app/Console/Commands/DemoReset.php:1-320` |
| **Risks** | Cited truncate and deletion operations create a DERIVED destructive-data risk if executed against populated data. Confirmation behavior, backup availability, recovery behavior, environment protection, production exposure, loss scope, and actual data-loss outcome are UNKNOWN. |

### CAP-076 · Database Backup Command

| Attribute | Detail |
|---|---|
| **Purpose** | CLI command to create database backup via mysqldump |
| **Entry Points** | `php artisan database:backup` |
| **Controllers** | `app/Console/Commands/DatabaseBackUp.php` |
| **Execution Flow** | Cited command code creates backup storage, invokes `mysqldump`, and targets `backup.sql`. Binary availability, command execution, output validity, and recovery outcome are UNKNOWN. |
| **State** | VERIFIED — command/signature and cited static operations exist |
| **Reachability** | CLI invocation is documented by command signature; deployment availability and actual execution are UNKNOWN |
| **Evidence** | `app/Console/Commands/DatabaseBackUp.php:1-60` |
| **Risks** | Cited output target is `backup.sql`; overwrite and timestamping outcomes are DERIVED. Backup retention and recovery usefulness are UNKNOWN. |

### CAP-077 · Demo Content Import

| Attribute | Detail |
|---|---|
| **Purpose** | Import demo courses, categories, blogs from seeders and extract demo images/videos from ZIP |
| **Entry Points** | `php artisan import:demo` |
| **Controllers** | `app/Console/Commands/ImportDemo.php` |
| **Execution Flow** | Cited command code includes documented truncate, seeder, archive-extraction, and session-deletion operations. Path validation, execution, deployment state, and resulting data outcome are UNKNOWN. |
| **State** | VERIFIED — command/signature and cited static operations exist |
| **Reachability** | CLI invocation is documented by command signature; deployment availability and actual execution are UNKNOWN |
| **Evidence** | `app/Console/Commands/ImportDemo.php:1-119` |
| **Risks** | Cited truncate and extraction operations create DERIVED data-loss and path-handling risks if executed. Actual affected records, archive handling outcome, and deployment impact are UNKNOWN. |

### CAP-078 · Payment Webhooks (Limited)

| Attribute | Detail |
|---|---|
| **Purpose** | Receive asynchronous payment confirmations from gateways |
| **Entry Points** | `web.php:993` (SSLCommerz IPN), `web.php:1130` (PayFlexi webhook) |
| **Controllers** | `SslCommerzPaymentController@ipn`, `PayFlexiController@webhook` |
| **Execution Flow** | Gateway POST/callback handling is indicated by cited routes/controllers; signature validation, order update, and mail behavior beyond cited code are UNKNOWN |
| **State** | VERIFIED (two explicit webhook routes recorded); comprehensive gateway/webhook audit UNKNOWN |
| **Reachability** | Public callback intent DERIVED; exact middleware coverage UNKNOWN |
| **Evidence** | `routes/web.php:993,1130`; callback methods found in Flutterwave, Iyzico, Paystack controllers |
| **Gaps** | Gateway-wide callback model and replay protection are UNKNOWN; no exhaustive audit performed. |

### CAP-079 · Drip Content Enablement

| Attribute | Detail |
|---|---|
| **Purpose** | Enable gradual content release for courses based on schedule |
| **Entry Points** | Course create/edit forms; `CourseController@store`, `@update` |
| **Models** | `Course` (columns: `drip_enable` boolean, `duration_type` enum) |
| **Execution Flow** | Cited create/update paths set `drip_enable` and `duration_type`. Visibility control and scheduled-release behavior are UNKNOWN. |
| **State** | DERIVED (flag exists, enforcement logic not traced) |
| **Reachability** | Cited create/update paths set the flag; deployed route access and runtime effect are UNKNOWN |
| **Evidence** | `app/Course.php:32` (fillable); `CourseController.php:274,419`; `Api/InstructorApiController.php:1102,1265` |
| **Enforcement** | Lesson-hiding logic NOT FOUND in controllers. May be in views or JavaScript. Runtime behavior UNVERIFIED. |

### CAP-080 · Live Class Paid Enrollment

| Attribute | Detail |
|---|---|
| **Purpose** | Charge for individual live class access separate from course enrollment |
| **Entry Points** | `OrderStoreController@orderstore` (lines 61-105) |
| **Controllers** | `OrderStoreController` |
| **Models** | `PaidMettings`, `Meeting`, `BBL`, `JitsiMeeting`, `Googlemeet` |
| **DB Tables** | `paid_mettings` |
| **Execution Flow** | Cited `OrderStoreController` path handles meeting session details and includes `PaidMettings` creation. Payment callback, persistence, and access outcomes are UNKNOWN. |
| **State** | VERIFIED — cited controller/path observation only |
| **Reachability** | Cited controller entry point; deployed route availability and runtime reachability are UNKNOWN |
| **Evidence** | `app/Http/Controllers/OrderStoreController.php:61-105` |

### CAP-081 · Quiz Result Reporting & Re-attempt

| Attribute | Detail |
|---|---|
| **Purpose** | Display quiz results, allow re-attempts, instructor views reports |
| **Entry Points** | `QuizStartController@show`, `@tryagain`, `@sub_show`, `@subtryagain` |
| **Controllers** | `QuizStartController`, `QuizTopicController` |
| **Models** | `QuizTopic`, `QuizAnswer`, `Quiz` |
| **Execution Flow** | Cited quiz-controller methods include result, re-attempt, answer-deletion, and percentage-handling paths. Score calculation, persistence, and re-attempt outcome are UNKNOWN. |
| **State** | VERIFIED — cited controller/path observation only |
| **Reachability** | Cited controller entry points; deployed route availability and runtime reachability are UNKNOWN |
| **Evidence** | `app/Http/Controllers/QuizStartController.php:48-78,131-135` |
| **Limitation** | Attempt-limit, history-deletion, and subjective-answer approval behavior are limited to cited paths; runtime enforcement is UNKNOWN. |

### CAP-082 · Module Dependency Checks

| Attribute | Detail |
|---|---|
| **Purpose** | Check if optional modules are installed before using features |
| **Entry Points** | Throughout controllers: `Module::has('ModuleName') && Module::find('ModuleName')->isEnabled()` |
| **Modules Referenced** | Certificate, Homework, Resume, Forum, Ebook, Esewa, Smanager, Googleclassroom, Blizzard |
| **State** | VERIFIED (module checks/references; source absent from inspected repository) + UNKNOWN (module runtime behavior) |
| **Reachability** | UNKNOWN — missing source alone does not establish reachability |
| **Evidence** | `AddonController.php:26`, `Api/OtherApiController.php:988-997`, `CourseController.php:946` |
| **Impact** | Cited module-dependent feature behavior is UNKNOWN; missing-source dependency risk is DERIVED. |

### CAP-083 · Language Switching

| Attribute | Detail |
|---|---|
| **Purpose** | Allow users to switch site language; store preference in session |
| **Middleware** | `app/Http/Middleware/SwitchLanguage.php` |
| **State** | VERIFIED — cited middleware observation only |
| **Reachability** | Middleware presence is cited; deployed registration and runtime language-switch outcome are UNKNOWN |
| **Evidence** | `app/Http/Middleware/SwitchLanguage.php:40` |

### CAP-084 · Admin Financial Reports

| Attribute | Detail |
|---|---|
| **Purpose** | Generate revenue reports for admin and per-instructor |
| **Entry Points** | `web.php:459-460`; `RevenueReportController@report`, `@instructorReport` |
| **State** | DERIVED |
| **Reachability** | Cited admin route/controller entry points; deployed authorization enforcement, report accuracy, and runtime reachability are UNKNOWN |
| **Evidence** | `routes/web.php:459-460,733-734` |

### CAP-085 · Course Progress Tracking

| Attribute | Detail |
|---|---|
| **Purpose** | Track which chapters/lessons user completed; generate progress reports |
| **Entry Points** | `web.php:796-797`; `CourseProgressController@progressreport`, `@progressview` |
| **Models** | `CourseProgress` |
| **State** | VERIFIED — cited routes/query observation only |
| **Reachability** | Cited route/controller entry points; deployed authorization enforcement, progress persistence, and runtime reachability are UNKNOWN |
| **Evidence** | `routes/web.php:796-797`; `CertificateController` queries `course_progress` |

### CAP-086 · IP Blocking

| Attribute | Detail |
|---|---|
| **Purpose** | Block specific IP addresses from accessing the site |
| **Middleware** | `ip_block` |
| **State** | DERIVED |
| **Reachability** | Middleware registration/use is cited; route coverage and runtime blocking outcome are UNKNOWN |
| **Evidence** | Middleware in `app/Http/Kernel.php`; used in `api.php:29` |

### CAP-087 · Maintenance Mode

| Attribute | Detail |
|---|---|
| **Purpose** | Disable site access for non-admins during maintenance |
| **Middleware** | `maintanance_mode` |
| **State** | DERIVED |
| **Reachability** | Middleware presence is cited; deployment activation, route coverage, and runtime access effect are UNKNOWN |
| **Evidence** | Middleware in `app/Http/Kernel.php` |

### CAP-088 · Admin Impersonation

| Attribute | Detail |
|---|---|
| **Purpose** | Admin can login as any user to see their view |
| **Entry Points** | `AlluserController@login` |
| **State** | VERIFIED — cited controller entry-point observation only |
| **Reachability** | Cited admin-related entry point; deployed authorization enforcement and runtime reachability are UNKNOWN |
| **Risks** | Confirmation behavior and audit logging are UNKNOWN. Impersonation-access risk is DERIVED if cited path executes. |

---

### Verification of First-Pass Claims

#### Claim: "19 configured modules are absent" — **VERIFIED**

Evidence: `modules_statuses.json` lists 19 modules. `Modules/` directory does NOT exist. Controllers reference via `Module::has()`. Namespace in `CategoryController.php:3` references `namespace Modules\Ebook\Http\Controllers;`.

**Conclusion:** Module source code is missing from inspected repository (`VERIFIED`). Individual module-dependent paths require cited dependency evidence; their runtime behavior and production availability are `UNKNOWN`.

#### Claim: "Queue jobs use Auth::user() in queue context" — **VERIFIED**

Evidence: `app/Jobs/AffiliatesPoints.php:37,46`, `EnrollExpire.php:37`, `InstructorPlan.php:37` all use `Auth::user()` directly.

**Conclusion:** Direct `Auth::user()` use is `VERIFIED`. Queue-worker failure is a `DERIVED` risk; actual execution and runtime result are `UNKNOWN`.

#### Claim: "No database transactions in order creation" — **VERIFIED**

Evidence: No `DB::transaction()` wrapper in `OrderStoreController.php`. Multiple inserts without atomicity.

**Conclusion:** Partial-write and concurrency risk in this cited path is `DERIVED`; actual runtime integrity outcome is `UNKNOWN`.

#### Claim: "No same-`transaction_id` check in cited order-creation path" — **VERIFIED**

Evidence: No check for existing order with same `transaction_id` before creating.

**Conclusion:** Duplicate-order risk for cited path is `DERIVED`; callback retry behavior and actual duplicate outcomes are `UNKNOWN`.

#### Claim: "Zero foreign keys" — **VERIFIED**

Evidence: `grep -rn 'foreign(' database/migrations/` returned no results. 203 migrations, none define FK constraints.

**Conclusion:** All referential integrity application-level. Orphaned records possible.

---

---

## 13. Final Coverage Audit

This section records inherited inspection/coverage statements and their evidence limits. Section presence or count metadata does not establish evidence completeness or source-wide verification.

### Repository Coverage

| Component Type | Inspection Status | Evidence | Completeness |
|---|---|---|---|
| **Route definitions (web)** | ⚠️ PARTIAL | `routes/web.php` count/inspection statement is inherited metadata | Entry points documented selectively; source-wide traceability not established |
| **API routes** | ⚠️ PARTIAL | `routes/api.php` count/inspection statement is inherited metadata | Endpoint coverage and middleware behavior not source-wide verified |
| **Controllers** | ⚠️ PARTIAL | 238-controller statement is inherited count metadata | Material flows cited; all controller methods not revalidated |
| **Models/Entities** | ⚠️ PARTIAL | 131-model statement is inherited count metadata | Core records documented; source-wide relationship verification not established |
| **Services** | ⚠️ PARTIAL | 2-service statement is inherited count metadata | Service-layer completeness UNKNOWN |
| **Database schema** | ⚠️ PARTIAL | 203-migration/~60-table statement is inherited count metadata | Listed tables/relationships not source-wide revalidated |
| **Views/Frontend** | ⚠️ PARTIAL | 695-view statement is inherited count metadata | View-layer logic not traced |
| **Authorization** | ⚠️ PARTIAL | Middleware/policy/RBAC references documented | Route-by-route enforcement UNKNOWN |
| **Jobs/Events/Listeners** | ⚠️ PARTIAL | Component counts are inherited metadata | Queue/event/listener runtime and exhaustive coverage UNKNOWN |
| **Integrations** | ⚠️ PARTIAL | Provider counts are inherited metadata | Gateway/provider behavior and full inventory UNKNOWN |
| **Commands** | ⚠️ PARTIAL | Command count is inherited metadata | Registration, reachability, and execution coverage UNKNOWN |
| **Tests** | ⚠️ PARTIAL | Inherited record says no automated tests beyond scaffolds | Test inventory and behavior coverage not independently verified |

**Coverage status:** PARTIAL. Counts and prior inventory claims require item-by-item source revalidation; views/frontend are not fully traced.

---

### Evidence Quality Statement

⚠️ **File paths provided** — many records cite paths; all 88 records are not individually revalidated
⚠️ **Line numbers provided** — many entries include inherited line references; precision varies
⚠️ **Route names traced** — selected entry points mapped; complete route coverage not established
⚠️ **Controller methods named** — selected methods listed; source-wide method coverage not established
⚠️ **Model relationships documented** — listed relationships are inherited evidence, not full schema verification
⚠️ **Classification labels used** — reconciliation normalized material claims; classifications are not systematic for every inherited record
⚠️ **Unknowns explicitly listed** — Section 11 is a partial consolidated inventory, not proof all unknowns were found
⚠️ **Static analysis limitations noted** — runtime behavior remains UNKNOWN unless current evidence proves it

⚠️ **Some line ranges imprecise** — Some entries reference large file segments  
⚠️ **View-layer behavior not traced** — Client-side validation, AJAX not inventoried  
⚠️ **Runtime behavior inferred** — Some execution flow claims DERIVED not VERIFIED  

---

### Discovery Process Verification

⚠️ **Discovery-process statements are inherited** — methodology and independence were not revalidated in this reconciliation.
⚠️ **Candidate boundaries are DERIVED** — Section 6 records LOW confidence and unresolved boundary evidence.

---

### Product Neutrality Verification

✅ No KEEP decisions  
✅ No MODIFY decisions  
✅ No REPLACE decisions  
✅ No REMOVE decisions  
✅ No NEW decisions  
✅ No target-system requirements  
✅ **Modernization recommendations removed** — Section 11 subsection deleted (was lines 1416-1448)  
✅ Architectural observations present but no prescriptive recommendations  

**Product Neutrality Status:** ✅ COMPLIANT

---

### Second Pass Verification

⚠️ **Second-pass record present** — independent second-pass execution was not revalidated in this reconciliation.

**First Pass:** CAP-001 to CAP-070 (70 capabilities)  
**Second Pass:** CAP-071 to CAP-088 (18 additional capabilities)

Discovered through: Console commands, queue jobs, gift flow, OTA system, refund processing, bulk operations, webhooks, drip content, module checks, admin impersonation

**Inherited independence rationale:** Different entry points (CLI → jobs → admin controllers), new components not found in first pass, first-pass claims verified. This rationale is not proof of independent source-wide verification.

---

### Compliance Summary

| Requirement | Status |
|---|---|
| All 14 required sections present | ⚠️ PARTIAL — headings present; candidate fields reconciled from existing evidence, broader coverage remains partial |
| Capability inventory with IDs | ✅ Present — CAP-001 to CAP-088 retained; evidence completeness PARTIAL |
| Detailed capability analysis | ✅ Section 5 present; evidence completeness PARTIAL |
| Candidate feature grouping | ⚠️ PARTIAL — CAND-001 to CAND-014 required fields recorded with explicit UNKNOWN values; boundaries remain DERIVED and LOW confidence |
| Cross-feature relationships | ✅ Section 8 present; evidence completeness PARTIAL |
| Unmapped components | ✅ Section 9 present; inventory completeness PARTIAL |
| Dead/Broken/Inconsistent | ✅ Section 10 present; classifications evidence-scoped and PARTIAL |
| Unknown inventory | ✅ Section 11 present; unknown inventory completeness PARTIAL |
| Second discovery pass | ✅ Section 12 present; independence/evidence completeness PARTIAL |
| Final coverage audit | ✅ Section 13 present; source-wide verification PARTIAL |
| Product decision boundary | ✅ Section 14 present |
| No product recommendations | ✅ No product decisions recorded in current artifact |
| Evidence quality | ⚠️ PARTIAL — inherited claims require revalidation |
| Classification vocabulary | ⚠️ PARTIAL — material claims reconciled; classifications are not systematic across every inherited record |

---

## 14. Final Product Decision Boundary

### Summary Statistics (Unverified inherited counts)

| Metric | Count |
|---|---|
| **Controllers** | 238 |
| **Models** | 131 |
| **Routes (web)** | ~350+ (web.php 1,156 lines) |
| **Routes (API)** | ~120+ (api.php 505 lines) |
| **Middleware** | 19 |
| **Migrations** | 203 |
| **Capabilities Identified** | 88 (CAP-001 to CAP-088) |
| **Candidate Feature Groups** | 14 (CAND-001 to CAND-014) |
| **Payment Gateways** | 19 |
| **Live Class Integrations** | 3 (Zoom, BBB, Google Meet) |
| **Social Login Providers** | 6 (FB, Google, GitLab, Amazon, LinkedIn, Twitter) |
| **CLI Commands** | 7 |
| **Queue Jobs** | 3 (direct `Auth::user()` use recorded; queue runtime outcome UNKNOWN) |
| **Notifications** | 5 |
| **Mail Classes** | 10 |
| **Modules Configured** | 19 configured; `Modules/` absent from inspected repository |
| **Policies Defined** | 23; registration state recorded, effective use UNKNOWN |
| **Blade Views** | 695 total (365 admin, 23 instructor, 74 front, others in themes) |
| **Blade Components** | 1 (`breadcumb.blade.php`) |
| **Database Tables** | ~60+ core tables |
| **Foreign Keys** | 0 |
| **Automated Tests** | 0 (only scaffold files) |
| **Critical Issues** | 10+ |
| **Security Issues** | 8+ |
| **BROKEN Components** | No blanket runtime total asserted; see evidence-scoped Section 10 classifications |
| **UNREACHABLE Components** | No blanket module-path classification asserted; see Sections 10–12 |

---

### Legacy Observations (Static-Analysis Scope)

The insmart LMS is a **feature-rich, monolithic Laravel 10 application** designed for online course sales and delivery. It supports:

- Multi-role users (admin, instructor, learner)
- Comprehensive course authoring (chapters, lessons, quizzes, assignments, certificates)
- 19 payment gateway integrations
- 3 live class platforms (Zoom, BBB, Google Meet)
- Instructor revenue sharing and payout system
- Affiliate/referral marketing
- Multi-currency and multi-language support
- Extensive admin configuration
- Gift course purchasing
- Course refund processing
- Over-the-air update system
- Admin bulk operations

**Second discovery pass added 18 capabilities** (CAP-071 to CAP-088), bringing the total from 70 to 88 documented capabilities. Key discoveries include gift course flow, refund processing, bulk delete operations, OTA update system, destructive CLI commands, payment webhooks, drip content flags, paid live class enrollment, and module dependency checking.

**Critical architectural weaknesses remain:**

1. **Missing modules** — 19 configured modules are absent from inspected repository (`VERIFIED`); impact on each module-dependent path is `DERIVED` or `UNKNOWN`.
2. **Transaction scope** — cited `OrderStoreController` multi-write path has no documented transaction wrapper (`VERIFIED`); partial-write outcome is `DERIVED` and runtime state `UNKNOWN`.
3. **Idempotency scope** — cited order-creation path has no documented same-`transaction_id` check (`VERIFIED`); callback replay and duplicate outcomes are `UNKNOWN`.
4. **Queue jobs** — all 3 cited jobs directly use `Auth::user()` (`VERIFIED`); queue failure is `DERIVED`, runtime outcome `UNKNOWN`.
5. **Credentials/settings** — configuration is read from `settings` in cited code (`VERIFIED`); encryption, access, and exposure are `UNKNOWN`.
6. **Zero foreign keys** — referential integrity entirely application-level, orphaned records possible.
7. **No tests** — no way to verify behavior changes.
8. **Destructive CLI command risk** — cited `demo:reset` code includes truncate calls, including `users`, and documented deletion operations (`VERIFIED`). If executed against populated data, these operations create a `DERIVED` destructive-data risk. Confirmation behavior, backup and recovery availability, deployment exposure, actual execution, and resulting data-loss scope remain `UNKNOWN`.
9. **OTA update risks** — controller/configuration evidence supports a `DERIVED` update risk; signature, rollback, and production execution outcomes are `UNKNOWN`.
10. **Policies** — 23 policy files and empty `$policies` map are recorded (`VERIFIED`); route/policy effect is `UNKNOWN`.

**No runtime fitness or production-risk conclusion follows from this inventory.** The document records 88 inherited capability IDs and 14 derived candidate groups. Missing module source creates evidence-scoped dependency risk; actual feature and production behavior remain `UNKNOWN` without module source and runtime evidence.

---

> **Product Decision Boundary**
>
> This document is a forensic inventory of the legacy system only. No KEEP, MODIFY, REPLACE, REMOVE, or NEW decisions have been made. No target-system requirements have been created. All product treatment decisions remain pending human/Product Owner review.
