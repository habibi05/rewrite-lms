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

1. **Modules directory absent.** 19 modules configured but `Modules/` directory missing from repo. All module-dependent code paths = BROKEN DEPENDENCY.
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

## 3. Capability Inventory (CAP-XXX)

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
| **Risks** | Instructor can access admin-only routes if only `is_admin` middleware is used. No policies registered (`AuthServiceProvider:$policies` empty). |

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
| **Risks** | No content versioning. No audit trail. File uploads lack comprehensive validation. |



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
| **Risks** | Direct file URLs may be guessable. No signed URL mechanism for self-hosted content. SCORM integration depends on absent modules. |

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
| **Risks** | Cart lost on session expiry. No cart merge on login. Race condition if same course added from multiple tabs. |

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
| **Risks** | `OrderStoreController` instantiated directly (not via DI). `Auth::user()` used inside queued jobs. No idempotency — duplicate orders possible on payment callback retry. No DB transaction wrapping the multi-table writes. |



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
| **Risks** | API keys stored in database. No webhook signature verification on most gateways. No payment idempotency. Gateway credentials accessible to any admin. |

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
| **Risks** | No pessimistic locking on balance update — race condition on concurrent deductions. |

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
| **Execution Flow** | Admin creates bundle → selects courses → sets price → publish. User buys bundle → all courses enrolled at once. |

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
| **Execution Flow** | User requests refund → admin reviews → approve/reject → if approved: credit to wallet or original method → update order status. |
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
| **Execution Flow** | Free course: user clicks "Enroll" → create Order with `total_amount=0`, `payment_method='free'` → enrolled. Admin: select user + course → create Order → enrolled. |

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
| **Execution Flow** | User shares referral link → new user registers with referral cookie → on purchase by referee, referrer gets points/commission via `AffiliatesPoints` job. |

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
| **Execution Flow** | Buyer selects gift → enters recipient email → checkout → order created with `gift_to` field → recipient gets email with enrollment link |

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
| **Implementation** | Run mysqldump → save to storage |

### CAP-062 · Demo Mode / Demo Reset

| Attribute | Detail |
|---|---|
| **Purpose** | Reset demo environment |
| **Entry Points** | CLI commands `DemoReset`, `ImportDemo` |
| **Implementation** | Truncate tables → re-import demo SQL |

### CAP-063 · Installer / Setup Wizard

| Attribute | Detail |
|---|---|
| **Purpose** | First-time installation wizard |
| **Entry Points** | `web.php:78-81` |
| **Controllers** | `InstallerController` |
| **Middleware** | `IsInstalled` — redirects to installer if not completed |

### CAP-064 · OTA Updates

| Attribute | Detail |
|---|---|
| **Purpose** | Over-the-air updates |
| **Entry Points** | `web.php:95-98` |
| **Controllers** | `OtaUpdateController` |
| **Risks** | No code signing. Updates can overwrite custom code. |

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

## 4. Data Model Inventory

### Core Tables (from migrations & models)

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



---

## 5. Integration Points

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

## 6. Critical Execution Flows

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

## 7. Known Issues & Technical Debt

### Critical Issues

1. **Missing Modules Directory**: 19 modules in `modules_statuses.json`, `Modules/` absent. Certificate templates, Ebook, Homework, Resume/Job, Google Classroom all broken.
2. **Queue Jobs Use `Auth::user()`**: `EnrollExpire`, `AffiliatesPoints`, `InstructorPlan` call `Auth::user()` in queue context (null). Jobs fail silently.
3. **No Database Transactions**: `OrderStoreController@orderstore` does 10+ writes without transaction. Payment success + order fail = money taken, no enrollment.
4. **No Payment Idempotency**: Callbacks can retry. No `transaction_id` duplicate check → duplicate orders/charges.
5. **Middleware `is_admin` Misnamed**: Allows any non-`user` role. Instructors pass.
6. **Settings in Database**: Payment gateway credentials in `settings` table, not `.env`, not encrypted.
7. **Single-Row Settings**: `Setting::first()` global. Write contention. No versioning.
8. **Zero Foreign Keys**: All referential integrity application-level. Orphaned records guaranteed.
9. **No Automated Tests**: Only scaffold files.
10. **Task Scheduler Empty**: `schedule()` method body commented out.

### Security Issues

- OTP plaintext in DB
- Social login tokens plaintext
- No rate limiting (OTP, login, password reset)
- Admin can inject XSS via custom CSS/JS
- No webhook signature verification (most gateways)
- Payment credentials in DB unencrypted
- Weak file upload validation
- Direct object reference (sequential IDs, no ownership checks)
- Impersonation no audit trail

### Architecture Issues

- No service layer (logic in controllers)
- No repository pattern
- Dual auth (Spatie + raw column checks)
- Session cart (web) lost on logout
- No event sourcing/audit trail
- Magic numbers (hardcoded status/role strings)
- Typos: `Attandance`, `MaintananceMode`, `AlluserController`

### Data Integrity Issues

- JSON columns for relations (`bundle_courses.course_id`)
- No soft deletes on critical tables
- Course clone in controller (not DB-level)
- No unique constraints (coupons, referral codes)
- Wallet race condition (no locking)

### Performance Issues

- N+1 queries
- No query caching (Settings on every request)
- No CDN
- No index review
- Synchronous notifications block response

### Missing Functionality

- No failed job tracking
- No health checks
- No rate limiting (API)
- No API versioning
- No backup automation (command exists but not scheduled)
- No log rotation
- No password policy
- No session management UI



---

## 8. Candidate Feature Groupings (CAND-XXX)

### CAND-001 · User Management & Authentication

**Capabilities**: CAP-001 (Auth), CAP-002 (RBAC), CAP-024 (User CRUD), CAP-028 (Instructor Request), CAP-043 (Email Verify), CAP-044 (2FA), CAP-045 (Guest Checkout), CAP-050 (User Dashboard)

**Rationale**: All user identity, authentication, authorization, and account management.

**Tables**: `users`, `otps`, `social_logins`, `two_factor_authentications`, `instructor_requests`, `password_resets`, `roles`, `permissions`, `model_has_roles`

**Controllers**: Auth namespace, `AlluserController`, `AllinstructorController`, `AlladminController`, `UserProfileController`, `InstructorRequestController`, `TwoFactorAuthController`, `AuthController`, `GuestController`

**Entry Points**: `web.php:49-138,483-520,860-862,1135`, `api.php:31-42`

**Dependencies**: Spatie Permission, Laravel Passport, social providers (FB, Google, GitLab, Amazon, LinkedIn, Twitter)

### CAND-002 · Course Catalog & Content Management

**Capabilities**: CAP-003 (Course CRUD), CAP-004 (Content Delivery), CAP-023 (Categories), CAP-017 (Bundles), CAP-035 (Flash Sales), CAP-057 (Video Settings)

**Rationale**: All course creation, organization, content structure, and delivery infrastructure.

**Tables**: `courses`, `course_chapters`, `course_classes`, `categories`, `subcategories`, `childcategories`, `bundle_courses`, `flash_sales`, `course_languages`, `course_levels`, `what_learns`, `related_courses`, `course_includes`, `requirements`

**Controllers**: `CourseController`, `CoursechapterController`, `CourseclassController`, `CategoriesController`, `SubcategoryController`, `ChildcategoryController`, `BundleCourseController`, `FlashSaleController`, `VideosettingController`, `WatchController`, `InstructorCourseController`

**Entry Points**: `web.php:155-227,595-630,864-866,906,914,929-931,1124-1133,277-281`

**Dependencies**: AWS S3, YouTube, Vimeo, SCORM (via absent modules)

### CAND-003 · Commerce & Payments

**Capabilities**: CAP-006 (Cart), CAP-007 (Checkout), CAP-008 (Payment Gateways), CAP-009 (Coupons), CAP-010 (Wallet), CAP-025 (Free Enrollment), CAP-046 (Gift), CAP-047 (Instalment), CAP-053 (Order Management), CAP-059 (Invoices)

**Rationale**: All purchase, payment processing, order creation, and transaction management.

**Tables**: `orders`, `carts`, `coupons`, `wallets`, `add_on_wallets`

**Controllers**: `CartController`, `CheckoutController`, `OrderStoreController`, `OrderController`, `EnrollmentController`, `WalletController`, `WalletPaymentController`, `CouponController`, 19 payment gateway controllers (PayPal, Stripe, Razorpay, etc.)

**Entry Points**: `web.php:835-852,881-999,1001-1025,1137,442-461`, `api.php:73,80-174`

**Dependencies**: 19 payment gateways, `barryvdh/laravel-dompdf`

### CAND-004 · Learning Progress & Assessment

**Capabilities**: CAP-005 (Progress Tracking), CAP-012 (Quiz), CAP-013 (Certificates), CAP-030 (Assignments), CAP-034 (Question Bank)

**Rationale**: All learner progress measurement, assessment, and credential issuance.

**Tables**: `course_progress`, `quizzes`, `quiz_topics`, `quiz_answers`, `certificates`, `certificate_designs`, `assignments`, `submit_assignments`, `question_books`

**Controllers**: `CourseProgressController`, `QuizStartController`, `QuizController`, `QuizTopicController`, `CertificateController`, `CertificateDesignController`, `AssignmentController`, `QuestionBookController`

**Entry Points**: `web.php:908-922,918-920,924-927,637-650,938-940,404-412`

**Dependencies**: `barryvdh/laravel-dompdf`, `Modules\Certificate` (BROKEN)

### CAND-005 · Live Class & Meetings

**Capabilities**: CAP-014 (Zoom), CAP-015 (BigBlueButton), CAP-016 (Google Meet), CAP-031 (Appointments), CAP-032 (Attendance)

**Rationale**: Synchronous learning via live meetings and appointment scheduling.

**Tables**: `meetings`, `bbb_meetings`, `google_meets`, `appointments`, `attandances`

**Controllers**: `ZoomController`, `BigBlueController`, `GooglemeetController`, `AppointmentController`, `AttandanceController`

**Entry Points**: `web.php:527-590,651-670,941-942`

**Dependencies**: Zoom API, BigBlueButton API, Google Calendar API

### CAND-006 · Instructor Revenue & Payouts

**Capabilities**: CAP-011 (Payout System), CAP-048 (Instructor Plans), CAP-040 (Reports), CAP-052 (Instructor Dashboard)

**Rationale**: Instructor earnings tracking, subscription plans, payout processing, analytics.

**Tables**: `pending_payouts`, `completed_payouts`, `plans`, `user_plans`

**Controllers**: `PayoutController`, `AdminPayoutController`, `CompletedPayoutController`, `InstructorPlanController`, `PlanController`, `InstructorSettingController`

**Entry Points**: `web.php:1098-1116,427-441,527-530`

**Jobs**: `InstructorPlan`

### CAND-007 · Student Engagement & Community

**Capabilities**: CAP-018 (Wishlist), CAP-019 (Reviews), CAP-020 (Q&A), CAP-029 (Announcements), CAP-055 (Compare)

**Rationale**: Features promoting engagement, feedback, and community interaction.

**Tables**: `wishlists`, `review_ratings`, `question_answers`, `answers`, `announcements`, `compares`

**Controllers**: `WishlistController`, `ReviewratingController`, `QuestionanswerController`, `AnnouncementController`, `CompareController`

**Entry Points**: `web.php:838-840,870-873,867-869,631-636,1156`

**Helper**: `Is_wishlist::in_wishlist($c)`



### CAND-008 · Marketing & Promotions

**Capabilities**: CAP-026 (Affiliate), CAP-035 (Flash Sales), CAP-009 (Coupons), CAP-068 (Push Notifications)

**Rationale**: Referral tracking, discount campaigns, promotional tools.

**Tables**: `affiliates`, `affiliate_histories`, `flash_sales`, `coupons`

**Controllers**: `AffiliateController`, `AffilateDashboardController`, `FlashSaleController`, `CouponController`, `OneSignalNotificationController`

**Entry Points**: `web.php:875,1132-1133,359-370`

**Middleware**: `CheckReferral`

**Jobs**: `AffiliatesPoints`

### CAND-009 · Refunds & Support

**Capabilities**: CAP-021 (Refund System), CAP-054 (Support Tickets)

**Rationale**: Customer service, issue resolution, refund processing.

**Tables**: `refund_courses`, `refund_policies`, `supports`, `support_replies`

**Controllers**: `RefundCourseController`, `SupportController`, `AdminSupportController`

**Entry Points**: `web.php:943-946,1027-1044`

**Mail**: `SupportTicketCreated`, `SupportReplyNotification`

### CAND-010 · Content Management System (CMS)

**Capabilities**: CAP-022 (Blog), CAP-033 (Notice Board), CAP-039 (Landing Page Builder), CAP-056 (Ebook)

**Rationale**: Public-facing content, informational pages, digital products beyond courses.

**Tables**: `blogs`, `notice_boards`, `slider_facts`, `testimonials`, `trusteds`, `faq_instructors`, `pages`, `ebooks`, `ebook_categories`

**Controllers**: `BlogController`, `NoticeBoardController`, `HomepageController`, `SliderController`, `TestimonialController`, `TrustedController`, `FactController`, `PageController`, `landing\EbookController`, `CategoryController` (ebook)

**Entry Points**: `web.php:371-375,396-403,291-350,1139,1147-1149`

**Dependencies**: `Modules\Ebook` (BROKEN)

### CAND-011 · System Administration

**Capabilities**: CAP-038 (Settings), CAP-058 (API Keys), CAP-041 (IP Blocking), CAP-042 (Maintenance Mode), CAP-051 (Admin Dashboard), CAP-040 (Reports), CAP-060 (Sitemap), CAP-061 (DB Backup), CAP-062 (Demo Reset), CAP-063 (Installer), CAP-064 (OTA Updates), CAP-065 (Purchase Code), CAP-069 (Custom CSS/JS), CAP-070 (Cookie Consent)

**Rationale**: System configuration, infrastructure, installation, updates, compliance.

**Tables**: `settings`, `ip_blocks`

**Controllers**: `SettingController`, `ApiController`, `ConfigurationController`, `IpBlockController`, `AdminController`, `InstallerController`, `OtaUpdateController`

**Entry Points**: `web.php:129-131,239-290,282-284,149-154,263-266,78-81,95-98`

**CLI Commands**: `DatabaseBackUp`, `DemoReset`, `ImportDemo`, `GenerateSitemap`, `PurchaseFile`, `RenameVideo`, `ReplaceFiles`

**Middleware**: `ip_block`, `maintanance_mode`, `IsInstalled`

**Helpers**: `currency.php:purchase_code()`, `Tracker.php`

### CAND-012 · Localization & Multi-Currency

**Capabilities**: CAP-036 (Multi-Currency), CAP-037 (Multi-Language)

**Rationale**: International support, currency conversion, UI translation.

**Tables**: `currencies`, `languages`

**Controllers**: `CurrencyExchangeController`, `LanguageController`

**Entry Points**: `web.php:1150-1154,133`

**Middleware**: `switch_languages`

### CAND-013 · Notifications & Communications

**Capabilities**: CAP-027 (Notification System), CAP-067 (SMS), CAP-068 (Push Notifications)

**Rationale**: All user communication channels.

**Notifications**: `UserEnroll`, `AdminOrder`, `CourseNotification`, `OfferPushNotifications`

**Mail**: `SendOrderMail`, `GiftOrder`, `AdminMailOnOrder`, `WelcomeUser`, `UserAppointment`, `SupportTicketCreated`, `SupportReplyNotification`, `SendOtp`

**Controllers**: `NotificationController`, `OneSignalNotificationController`

**Entry Points**: `web.php:1095-1097,359-370`

**Helpers**: `TwilioMsg::sendMessage()`

**Dependencies**: Twilio SDK, OneSignal API

### CAND-014 · Search & Discovery

**Capabilities**: CAP-049 (Search & Filter), CAP-060 (Sitemap)

**Rationale**: Course discovery, SEO optimization.

**Controllers**: `SearchController`

**Entry Points**: `web.php:1145-1146`

**CLI Commands**: `GenerateSitemap`

**Dependencies**: Algolia (optional)

---

## 9. Dependency Analysis

### Composer Dependencies (Production — 92 packages)

**Core Framework**:
- `laravel/framework: ^10.10` — Laravel 10.x
- `php: ^8.1` — PHP 8.1+

**Authentication & Authorization**:
- `laravel/passport: ^11.8` — API authentication (OAuth2)
- `spatie/laravel-permission: ^5.10` — Role-based access control
- `pragmarx/google2fa-laravel: ^2.1` — 2FA/TOTP

**Payment Gateways** (19 integrations):
- `srmklive/paypal: ^3.0`, `stripe/stripe-php: ^12.2`, `razorpay/razorpay: ^2.8`, `yabacon/paystack-php: ^2.2`, `paytm/paytmchecksum: ^1.0.3`, `payuindia/payuinsdk: dev-master`, `cashfree/cashfree-pg: ^4.1`, `mollie/mollie-api-php: ^2.53`, `omnipay/omnipay: ^3.2`, `iyzico/iyzipay-php: ^2.0`, `shipu/aamarpay: ^1.1`, `xendit/xendit-php: ^2.19`, `braintree/braintree_php: ^6.13`, `flutterwave/flutterwave-v3: ^1.0`, `instamojo/instamojo-php: ^0.4.0`

**File Handling & Media**:
- `intervention/image: ^2.7` — Image manipulation
- `laraveldaily/laravel-charts: ^0.2.3` — Charts/graphs

**PDF Generation**:
- `barryvdh/laravel-dompdf: ^2.0` — PDF export

**External APIs**:
- `google/apiclient: ^2.15` — Google API (Meet, Calendar)
- `bigbluebutton/bigbluebutton-api-php: ^2.3` — BBB integration
- `twilio/sdk: ^7.3` — SMS

**Social Login**:
- `laravel/socialite: ^5.6`

**Excel Import/Export**:
- `rap2hpoutre/fast-excel: ^5.2`

**Modular Architecture**:
- `nwidart/laravel-modules: ^10.0` — Module system (modules absent from repo)

**HTTP Client**:
- `guzzlehttp/guzzle: ^7.2`

**Utilities**:
- `laravolt/avatar: ^5.0` — Avatar generation
- `pusher/pusher-php-server: ^7.2` — Real-time broadcasting
- `maatwebsite/excel: ^3.1` — Excel operations



### Risk Assessment

**High Risk Dependencies**:
- `paytm/paytmchecksum: ^1.0.3` — Likely outdated
- `payuindia/payuinsdk: dev-master` — No version pinning, unstable
- Multiple payment SDKs with varying maintenance status

**Missing from Repo but Required**:
- `Modules/` directory — 19 modules configured but source absent

---

## 10. Module Inventory (from modules_statuses.json)

| Module | Status | Evidence | Reachability |
|---|---|---|---|
| `Googleclassroom` | Active | Referenced in `HomeController`, `OtherApiController` | BROKEN (no source) |
| `Certificate` | Active | Used in `CertificateController`, `CourseController` | BROKEN (no source) |
| `Ebook` | Active | Controllers: `landing\EbookController`, `CategoryController` | BROKEN (no source) |
| `Homework` | Active | Referenced in `OtherApiController` | BROKEN (no source) |
| `Resume` | Active | Models imported in `OtherApiController` | BROKEN (no source) |
| `Jitsimeeting` | Active | No direct references found | BROKEN (no source) |
| `Googlemeet` | Active | `GooglemeetController` exists in core | BROKEN (module may provide models) |
| `Bigblue` | Active | `BigBlueController` exists in core | BROKEN (module may provide models) |
| `Zoom` | Active | `ZoomController` exists in core | BROKEN (module may provide models) |
| `BBL` | Active | Unknown purpose | BROKEN (no source) |
| `Forum` | Active | No references found | BROKEN (no source) |
| `Chatgpt` | Active | No references found | BROKEN (no source) |
| `Donation` | Active | No references found | BROKEN (no source) |
| `Customfield` | Active | No references found | BROKEN (no source) |
| `Newsletter` | Active | No references found | BROKEN (no source) |
| `Seo` | Active | No references found | BROKEN (no source) |
| `Invoice` | Active | Core invoice generation exists | BROKEN (module may extend) |
| `Subscriptionplan` | Active | `Plan`, `UserPlan` models exist in core | BROKEN (module may extend) |
| `Multivendor` | Active | No references found | BROKEN (no source) |

**Impact**: All module-dependent features are non-functional. Certificate design templates, ebook catalog, homework assignments, resume/job posting, and potentially extended live class features are unavailable.

---

## 11. Observations & Recommendations

### Architectural Observations

1. **Monolithic Design with Modular Intent**: System designed for modularity via `nwidart/laravel-modules` but modules not included in repository. Suggests modules are add-ons sold separately or deployment process incomplete.

2. **Controller-Heavy Logic**: Average controller 200-500+ lines. No service layer. Business logic, validation, data access all in controllers. Testing and reuse difficult.

3. **Payment-Centric Architecture**: 19 payment gateways integrated. All follow identical pattern: validate → `new OrderStoreController` → `orderstore()`. Central bottleneck in `OrderStoreController` (518 lines, 2 methods).

4. **Settings as Single Source of Truth**: `settings` table single row contains all configuration. No environment-based config for gateways. All credentials in DB.

5. **Multi-Tenancy Absent**: System is single-tenant. No workspace/organization concept. All users share same course catalog, settings, branding.

6. **Role-Based Not Permission-Based**: Users have single `role` column. Spatie Permission installed but not used consistently. Middleware checks raw column, not permissions.

### Data Model Observations

1. **Enrollment as Order**: No separate `enrollments` table. `orders` table serves dual purpose: financial transaction AND enrollment record. Free enrollments create orders with `payment_method='free'`, `total_amount=0`.

2. **Revenue Split Denormalized**: `order.instructor_revenue` and `pending_payouts.amount` store calculated values. Instructor commission percentage in `settings.instructor_revenue`. No audit trail of rate changes.

3. **Course Structure Rigid**: Courses → Chapters → Classes (lessons). Fixed 3-level hierarchy. No alternative learning paths, branching, or adaptive content.

4. **Bundle as JSON Array**: `bundle_courses.course_id` is JSON array of course IDs. Not normalized. No pivot table. Querying/filtering bundles by course difficult.

5. **Progress Tracking Simple**: `course_progress` records completion per class. Single `complete_percent` field. No time-tracking, no analytics on watch time, pause points, rewinds.

6. **Quiz Model Limited**: Only multiple choice (4 options). Timer client-side. All answers sent to client. No question pools, randomization, or advanced item types.



### Code Quality Observations

1. **Naming Inconsistencies**: `Attandance` (should be Attendance), `MaintananceMode` (Maintenance), `AlluserController` (AllUserController or AllUsersController).

2. **Commented Code Pervasive**: Many methods have large commented blocks (e.g., `Tracker.php:11-46`, `Console/Kernel.php:32-36`).

3. **Magic Strings**: Status values (`0`/`1`), payment methods (`'free'`, `'paypal'`), roles (`'admin'`, `'instructor'`, `'user'`) all hardcoded. No enums or constants.

4. **Inconsistent Returns**: Some methods return views, some redirect, some return JSON, some return strings. No consistent API contract.

5. **Error Handling Minimal**: Most controllers lack try-catch. Exceptions bubble to global handler. No specific error messages for users.

### Security Observations

1. **Credentials in Database**: All payment gateway API keys, secrets, webhook URLs stored in `settings` table plaintext. Backup exports expose all credentials.

2. **No Rate Limiting**: Login, registration, OTP, password reset — all unlimited. Brute force and DoS possible.

3. **CSRF Gaps**: Some AJAX endpoints bypass CSRF middleware.

4. **File Upload Risks**: Extension checks but no MIME validation. No virus scanning. Uploads go to `public/` (directly accessible).

5. **Impersonation Unchecked**: Admin can login as any user (`AlluserController@login:361-370`) with no confirmation, no audit trail, no session marker.

### Deployment Observations

1. **No Environment Separation**: Settings in DB mean dev/staging/prod use same credentials unless DB differs. No `.env`-based config for gateways.

2. **Installer Included**: `InstallerController` present in production code. Should be removed post-install for security.

3. **Purchase Code Validation**: Envato purchase code required. Stored in `public/code.txt`. Validation via `currency.php:purchase_code()` with hardcoded token.

4. **OTA Update Mechanism**: Over-the-air updates via `OtaUpdateController`. Fetches remote package, extracts, replaces files, runs migrations. No rollback. High risk.

### Recommendations for Re-architecture

1. **Extract Business Logic**: Create service layer. Move domain logic out of controllers. Enables testing, reuse, and clearer boundaries.

2. **Normalize Data Model**: Replace JSON columns with proper relations. Add `enrollments` table separate from `orders`. Add soft deletes.

3. **Implement Transactions**: Wrap multi-table writes in DB transactions. Especially critical in `OrderStoreController`.

4. **Add Idempotency**: Payment callbacks should check `transaction_id` uniqueness before creating orders.

5. **Unify Authorization**: Use Spatie Permission consistently. Remove raw role column checks. Define permissions granularly.

6. **Move Credentials to Environment**: Payment gateway config should be in `.env`, not DB. Encrypt sensitive DB fields if DB storage required.

7. **Add Foreign Keys**: Define all relations at DB level. Enable cascading deletes where appropriate.

8. **Queue Long-Running Tasks**: Emails, notifications, affiliate points — dispatch to queue. Remove blocking operations from request cycle.

9. **Implement Caching**: Cache settings, frequently accessed courses, user permissions. Reduce DB queries.

10. **Add Comprehensive Tests**: Unit tests for business logic, integration tests for flows, API tests for endpoints.

11. **Audit Trail**: Add activity log for admin actions (impersonation, order creation, refunds, payouts).

12. **API Rate Limiting**: Throttle all API endpoints. Implement per-user and global limits.

13. **Module Resolution**: Either include module source in repository or refactor core to remove module dependencies.

14. **Separate Enrollment from Payment**: Create `enrollments` table. `orders` only for financial transactions. Allow multiple payment types for same enrollment (instalments).

15. **Enhanced Progress Analytics**: Track watch time, completion time, re-attempts, drop-off points. Store in separate analytics tables.



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
| **Execution Flow** | View gift page for course → enter recipient email, name → system checks if user exists → if not, creates user with default password `123456` and auto-verifies email → stores course ID and user ID in session (`one_order_course`, `one_order_user`) → redirects to standard checkout → `OrderStoreController` detects session keys and creates order for that user instead of authenticated user |
| **Side Effects** | Creates new User record if email not found. Auto-verifies email (`email_verified_at` set). Mail: `Mail\GiftOrder` exists but usage not confirmed. |
| **State** | VERIFIED |
| **Reachability** | REACHABLE (web route, no middleware restriction) |
| **Evidence** | `app/Http/Controllers/GiftCourseController.php:1-94` |
| **Risks** | Auto-creates users with weak default password. No confirmation flow visible. |

### CAP-072 · Course Refund Processing

| Attribute | Detail |
|---|---|
| **Purpose** | Admin-initiated refunds for paid courses, with gateway-specific refund API calls |
| **Entry Points** | Admin routes; `RefundController@index`, `@edit`, `@update` |
| **Controllers** | `RefundController` |
| **Models** | `RefundCourse`, `Order` |
| **DB Tables** | `refund_courses` |
| **Execution Flow** | Admin views refund request → admin approves → system calls gateway-specific refund method (PayPal, Stripe, Paystack, Instamojo, PayTM, RazorPay, BankTransfer) → gateway processes refund → status updated |
| **State** | VERIFIED |
| **Reachability** | REACHABLE (admin-only) |
| **Evidence** | `app/Http/Controllers/RefundController.php:1-100+`, `app/RefundCourse.php:1-27` |

### CAP-073 · Admin Bulk Delete Operations

| Attribute | Detail |
|---|---|
| **Purpose** | Delete multiple records at once via checkboxes |
| **Controllers** | `BulkdeleteController`, plus ~30+ controllers with `bulk_delete` methods |
| **Execution Flow** | Admin selects checkboxes → submits form → validates `checked[]` array → `Model::whereIn('id', $request->checked)->delete()` → redirects |
| **Scope** | Sliders, Testimonials, Ads, Countries, Cities, Meetings, Instructors, Users, Courses, Blogs, Categories, Assignments, Support Tickets, Reports |
| **State** | VERIFIED |
| **Reachability** | REACHABLE (admin routes) |
| **Evidence** | `app/Http/Controllers/BulkdeleteController.php:1-380` |
| **Risks** | Hard delete. No cascade handling. No transaction wrapper. |

### CAP-074 · Over-The-Air (OTA) Update System

| Attribute | Detail |
|---|---|
| **Purpose** | Remote application updates via web interface — downloads package, extracts, runs migrations |
| **Entry Points** | Admin; `OtaUpdateController@getotaview`, `@update`, `@checkforupate`, `@mergeQuickupdate` |
| **Controllers** | `OtaUpdateController` |
| **Execution Flow** | Check GitHub for updates → download ZIP → extract to base path → run migrations → update version file |
| **State** | VERIFIED |
| **Reachability** | REACHABLE (admin-only) |
| **Evidence** | `app/Http/Controllers/OtaUpdateController.php:1-439` |
| **Risks** | No signature verification. No rollback. Extracts over live app. Localhost bypass license check. |

### CAP-075 · Demo Reset Command

| Attribute | Detail |
|---|---|
| **Purpose** | CLI command to reset application to demo state |
| **Entry Points** | `php artisan demo:reset` |
| **Controllers** | `app/Console/Commands/DemoReset.php` |
| **Execution Flow** | Truncates 23+ tables → deletes files in `public/images/*` and `public/video/class/*` → deletes session files |
| **State** | VERIFIED |
| **Reachability** | REACHABLE (CLI, no auth check) |
| **Evidence** | `app/Console/Commands/DemoReset.php:1-320` |
| **Risks** | DESTRUCTIVE. No confirmation. No backup. Truncates `users` table. |

### CAP-076 · Database Backup Command

| Attribute | Detail |
|---|---|
| **Purpose** | CLI command to create database backup via mysqldump |
| **Entry Points** | `php artisan database:backup` |
| **Controllers** | `app/Console/Commands/DatabaseBackUp.php` |
| **Execution Flow** | Creates `storage/app/backup/` → runs `mysqldump` → saves to `backup.sql` |
| **State** | VERIFIED |
| **Reachability** | REACHABLE (CLI) |
| **Evidence** | `app/Console/Commands/DatabaseBackUp.php:1-60` |
| **Risks** | Backup file overwritten each time. No timestamping. |

### CAP-077 · Demo Content Import

| Attribute | Detail |
|---|---|
| **Purpose** | Import demo courses, categories, blogs from seeders and extract demo images/videos from ZIP |
| **Entry Points** | `php artisan import:demo` |
| **Controllers** | `app/Console/Commands/ImportDemo.php` |
| **Execution Flow** | Truncates Cart, Wishlist, Order tables → runs 12+ seeders → extracts `public/democontent.zip` → deletes session files |
| **State** | VERIFIED |
| **Reachability** | REACHABLE (CLI) |
| **Evidence** | `app/Console/Commands/ImportDemo.php:1-119` |
| **Risks** | Truncates active orders. Extracts without path validation. |

### CAP-078 · Payment Webhooks (Limited)

| Attribute | Detail |
|---|---|
| **Purpose** | Receive asynchronous payment confirmations from gateways |
| **Entry Points** | `web.php:993` (SSLCommerz IPN), `web.php:1130` (PayFlexi webhook) |
| **Controllers** | `SslCommerzPaymentController@ipn`, `PayFlexiController@webhook` |
| **Execution Flow** | Gateway sends POST to webhook URL → controller validates signature → updates order status → sends confirmation email |
| **State** | VERIFIED (only 2 gateways have explicit webhook routes) |
| **Reachability** | REACHABLE (no middleware — webhooks must be publicly accessible) |
| **Evidence** | `routes/web.php:993,1130`; callback methods found in Flutterwave, Iyzico, Paystack controllers |
| **Gaps** | Most gateways use synchronous callbacks, not webhooks. No replay protection visible. |

### CAP-079 · Drip Content Enablement

| Attribute | Detail |
|---|---|
| **Purpose** | Enable gradual content release for courses based on schedule |
| **Entry Points** | Course create/edit forms; `CourseController@store`, `@update` |
| **Models** | `Course` (columns: `drip_enable` boolean, `duration_type` enum) |
| **Execution Flow** | Instructor enables drip content → sets `drip_enable = 1` → system uses `duration_type` (days or months) to control visibility |
| **State** | DERIVED (flag exists, enforcement logic not traced) |
| **Reachability** | REACHABLE (flag can be set) |
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
| **Execution Flow** | User initiates payment → session stores meeting details → payment callback → creates `PaidMettings` record → clears session |
| **State** | VERIFIED |
| **Reachability** | REACHABLE |
| **Evidence** | `app/Http/Controllers/OrderStoreController.php:61-105` |

### CAP-081 · Quiz Result Reporting & Re-attempt

| Attribute | Detail |
|---|---|
| **Purpose** | Display quiz results, allow re-attempts, instructor views reports |
| **Entry Points** | `QuizStartController@show`, `@tryagain`, `@sub_show`, `@subtryagain` |
| **Controllers** | `QuizStartController`, `QuizTopicController` |
| **Models** | `QuizTopic`, `QuizAnswer`, `Quiz` |
| **Execution Flow** | Student completes quiz → system calculates score → displays result → student can delete answers and retake → percentage stored in `users.exam_percentage` |
| **State** | VERIFIED |
| **Reachability** | REACHABLE |
| **Evidence** | `app/Http/Controllers/QuizStartController.php:48-78,131-135` |
| **Limitation** | No attempt limit. Re-attempt deletes history. Subjective answers need manual approval. |

### CAP-082 · Module Dependency Checks

| Attribute | Detail |
|---|---|
| **Purpose** | Check if optional modules are installed before using features |
| **Entry Points** | Throughout controllers: `Module::has('ModuleName') && Module::find('ModuleName')->isEnabled()` |
| **Modules Referenced** | Certificate, Homework, Resume, Forum, Ebook, Esewa, Smanager, Googleclassroom, Blizzard |
| **State** | BROKEN (all modules absent from repository) |
| **Reachability** | UNREACHABLE (module code missing) |
| **Evidence** | `AddonController.php:26`, `Api/OtherApiController.php:988-997`, `CourseController.php:946` |
| **Impact** | Certificate generation, homework, forum, ebook, resume features — all unavailable. |

### CAP-083 · Language Switching

| Attribute | Detail |
|---|---|
| **Purpose** | Allow users to switch site language; store preference in session |
| **Middleware** | `app/Http/Middleware/SwitchLanguage.php` |
| **State** | VERIFIED |
| **Reachability** | REACHABLE |
| **Evidence** | `app/Http/Middleware/SwitchLanguage.php:40` |

### CAP-084 · Admin Financial Reports

| Attribute | Detail |
|---|---|
| **Purpose** | Generate revenue reports for admin and per-instructor |
| **Entry Points** | `web.php:459-460`; `RevenueReportController@report`, `@instructorReport` |
| **State** | DERIVED |
| **Reachability** | REACHABLE (admin-only) |
| **Evidence** | `routes/web.php:459-460,733-734` |

### CAP-085 · Course Progress Tracking

| Attribute | Detail |
|---|---|
| **Purpose** | Track which chapters/lessons user completed; generate progress reports |
| **Entry Points** | `web.php:796-797`; `CourseProgressController@progressreport`, `@progressview` |
| **Models** | `CourseProgress` |
| **State** | VERIFIED |
| **Reachability** | REACHABLE |
| **Evidence** | `routes/web.php:796-797`; `CertificateController` queries `course_progress` |

### CAP-086 · IP Blocking

| Attribute | Detail |
|---|---|
| **Purpose** | Block specific IP addresses from accessing the site |
| **Middleware** | `ip_block` |
| **State** | DERIVED |
| **Reachability** | REACHABLE |
| **Evidence** | Middleware in `app/Http/Kernel.php`; used in `api.php:29` |

### CAP-087 · Maintenance Mode

| Attribute | Detail |
|---|---|
| **Purpose** | Disable site access for non-admins during maintenance |
| **Middleware** | `maintanance_mode` |
| **State** | DERIVED |
| **Reachability** | REACHABLE |
| **Evidence** | Middleware in `app/Http/Kernel.php` |

### CAP-088 · Admin Impersonation

| Attribute | Detail |
|---|---|
| **Purpose** | Admin can login as any user to see their view |
| **Entry Points** | `AlluserController@login` |
| **State** | VERIFIED (first pass) |
| **Reachability** | REACHABLE (admin-only) |
| **Risks** | No confirmation. No audit log. |

---

### Verification of First-Pass Claims

#### Claim: "19 configured modules are absent" — **VERIFIED**

Evidence: `modules_statuses.json` lists 19 modules. `Modules/` directory does NOT exist. Controllers reference via `Module::has()`. Namespace in `CategoryController.php:3` references `namespace Modules\Ebook\Http\Controllers;`.

**Conclusion:** Module source code missing. All module-dependent features BROKEN or UNREACHABLE.

#### Claim: "Queue jobs use Auth::user() in queue context" — **VERIFIED**

Evidence: `app/Jobs/AffiliatesPoints.php:37,46`, `EnrollExpire.php:37`, `InstructorPlan.php:37` all use `Auth::user()` directly.

**Conclusion:** All 3 queue jobs BROKEN. Would fail at runtime.

#### Claim: "No database transactions in order creation" — **VERIFIED**

Evidence: No `DB::transaction()` wrapper in `OrderStoreController.php`. Multiple inserts without atomicity.

**Conclusion:** Race conditions possible. Critical integrity issue.

#### Claim: "No payment idempotency" — **VERIFIED**

Evidence: No check for existing order with same `transaction_id` before creating.

**Conclusion:** Duplicate orders possible if callback fires twice.

#### Claim: "Zero foreign keys" — **VERIFIED**

Evidence: `grep -rn 'foreign(' database/migrations/` returned no results. 203 migrations, none define FK constraints.

**Conclusion:** All referential integrity application-level. Orphaned records possible.

---

## 13. Summary Statistics (Updated After Second Pass)

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
| **Queue Jobs** | 3 (all BROKEN: `Auth::user()` bug) |
| **Notifications** | 5 |
| **Mail Classes** | 10 |
| **Modules Configured** | 19 (all absent from repo) |
| **Policies Defined** | 23 (not registered, effectively unused) |
| **Blade Views** | 695 total (365 admin, 23 instructor, 74 front, others in themes) |
| **Blade Components** | 1 (`breadcumb.blade.php`) |
| **Database Tables** | ~60+ core tables |
| **Foreign Keys** | 0 |
| **Automated Tests** | 0 (only scaffold files) |
| **Critical Issues** | 10+ |
| **Security Issues** | 8+ |
| **BROKEN Components** | 3 queue jobs + 19 module-dependent features |
| **UNREACHABLE Components** | All module-dependent code paths |

---

## 14. Conclusion

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

1. **Missing modules** — 19 configured modules absent from repository, breaking certificate templates, ebooks, homework, forum, resume features.
2. **No database transactions** — order creation can fail mid-process, leaving inconsistent state.
3. **No payment idempotency** — duplicate charges possible if callbacks replay.
4. **Queue jobs broken** — all 3 jobs use `Auth::user()` in queue context, will fail at runtime.
5. **Credentials in database** — payment keys likely stored unencrypted in `settings` table.
6. **Zero foreign keys** — referential integrity entirely application-level, orphaned records possible.
7. **No tests** — no way to verify behavior changes.
8. **Destructive CLI commands** — `demo:reset` truncates all tables including users, no confirmation.
9. **OTA update risks** — no signature verification, no rollback, extracts over live application.
10. **Policies not registered** — 23 policy files exist but not registered in `AuthServiceProvider`.

**The system is functional for basic course delivery but high-risk for production use without significant remediation.** The massive feature set (88 capabilities identified across 14 candidate feature groups) makes incremental migration challenging. The absence of module source code breaks significant functionality (certificates, homework, ebooks, forum).

---

> **Product Decision Boundary**
>
> This document is a forensic inventory of the legacy system only. No KEEP, MODIFY, REPLACE, REMOVE, or NEW decisions have been made. No target-system requirements have been created. All product treatment decisions remain pending human/Product Owner review.

---

**END OF FORENSIC INVENTORY — SECOND PASS COMPLETE**

*Analysis Date: 2026-10-16*  
*Commit: 68ce7ed725a0db21dab12e5f6e7e839b499e7554 (branch: development)*  
*Repository: `d:/laragon/www/insmart`*  
*First Pass: 70 capabilities (CAP-001 to CAP-070)*  
*Second Pass: +18 capabilities (CAP-071 to CAP-088)*  
*Total Capabilities: 88*  
*Analyst: Kiro AI*

