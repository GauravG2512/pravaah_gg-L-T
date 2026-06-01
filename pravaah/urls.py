"""
PRAVAAH – Integrated Management Suite
Main URL Configuration

This file registers URL routes for all 19 apps in the PRAVAAH platform.
Each app's urls.py handles its own internal routes (list, detail, create,
update, delete, etc.).

URL structure:
    /admin/             → Django Admin panel
    /accounts/          → Login, logout, password reset
    /users/             → User management & role assignment
    /students/          → Student admission & profile
    /trainers/          → Trainer profiles & skills
    /programs/          → Training programs
    /courses/           → Courses & modules
    /batches/           → Batch creation & management
    /sessions/          → Session scheduling
    /attendance/        → Attendance marking & reports
    /assessments/       → Assessments & grading
    /certificates/      → Certificate generation & verification
    /hostels/           → Hostel master data
    /rooms/             → Room inventory
    /allocations/       → Room allocation & transfers
    /finance/           → Invoices & payments
    /notifications/     → Notification centre
    /reports/           → MIS & BI reports
    /dashboard/         → Analytics dashboard
    /api/               → REST API gateway (DRF)
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # ── Django Admin ──────────────────────────────────────────────────────────
    path('admin/', admin.site.urls),

    # ── Authentication & User Management ─────────────────────────────────────
    path('accounts/',       include('apps.accounts.urls')),
    path('users/',          include('apps.users.urls')),

    # ── Core Domain Modules ───────────────────────────────────────────────────
    path('students/',       include('apps.students.urls')),
    path('trainers/',       include('apps.trainers.urls')),

    # ── Training Program & Course Modules ─────────────────────────────────────
    path('programs/',       include('apps.programs.urls')),
    path('courses/',        include('apps.courses.urls')),

    # ── Batch, Session & Attendance Modules ───────────────────────────────────
    path('batches/',        include('apps.batches.urls')),
    path('sessions/',       include('apps.sessions.urls')),
    path('attendance/',     include('apps.attendance.urls')),

    # ── Assessment & Certification Modules ────────────────────────────────────
    path('assessments/',    include('apps.assessments.urls')),
    path('certificates/',   include('apps.certificates.urls')),

    # ── Hostel Management Modules ─────────────────────────────────────────────
    path('hostels/',        include('apps.hostels.urls')),
    path('rooms/',          include('apps.rooms.urls')),
    path('allocations/',    include('apps.allocations.urls')),

    # ── Finance Module ────────────────────────────────────────────────────────
    path('finance/',        include('apps.finance.urls')),

    # ── Common / Support Modules ──────────────────────────────────────────────
    path('notifications/',  include('apps.notifications.urls')),

    # ── Shared Services ───────────────────────────────────────────────────────
    path('reports/',        include('apps.reports.urls')),
    path('dashboard/',      include('apps.dashboard.urls')),

    # ── REST API Gateway ──────────────────────────────────────────────────────
    path('api/',            include('apps.api.urls')),

]

# ── Serve media files in development ─────────────────────────────────────────
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)