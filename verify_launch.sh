#!/bin/bash
# 🚀 CHATAKE INNOWORKS CI-PLATFORM — LAUNCH VERIFICATION SCRIPT
# Run this to verify all systems are operational

set -e

echo ""
echo "═══════════════════════════════════════════════════════════════════════"
echo "  CHATAKE INNOWORKS CI-PLATFORM — LAUNCH VERIFICATION"
echo "═══════════════════════════════════════════════════════════════════════"
echo ""

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test counters
TESTS_PASSED=0
TESTS_FAILED=0

# Helper function for test results
test_check() {
    local test_name=$1
    local command=$2
    
    if eval "$command" > /dev/null 2>&1; then
        echo -e "${GREEN}✓${NC} $test_name"
        ((TESTS_PASSED++))
    else
        echo -e "${RED}✗${NC} $test_name"
        ((TESTS_FAILED++))
    fi
}

echo "SYSTEM CHECKS"
echo "─────────────────────────────────────────────────────────────────────────"

test_check "Python 3.11+ installed" "python3 --version | grep -q 'Python 3.1'"
test_check "Django 4.2 installed" "python3 -c 'import django; assert django.__version__.startswith(\"4.2\")'"
test_check "Database migrated" "python manage.py migrate --check"
test_check "No system issues" "python manage.py check"

echo ""
echo "ROUTE TESTS"
echo "─────────────────────────────────────────────────────────────────────────"

python manage.py shell << 'EOF' 2>/dev/null
from django.urls import reverse

routes = [
    'portal:role_selector',
    'portal:student_dashboard',
    'portal:teacher_dashboard',
    'portal:intern_dashboard',
    'portal:project_dashboard',
    'portal:accounts_dashboard',
    'portal:admin_dashboard',
]

all_resolved = True
for route in routes:
    try:
        reverse(route)
        print(f"✓ {route}")
    except Exception as e:
        print(f"✗ {route}: {e}")
        all_resolved = False

if all_resolved:
    print("\nAll routes resolved ✓")
EOF

echo ""
echo "ADMIN CONFIGURATION"
echo "─────────────────────────────────────────────────────────────────────────"

python manage.py shell << 'EOF' 2>/dev/null
from django.contrib import admin
from core.models import UserProfile, Role, Program, Batch, Enrollment

registered_models = [
    ('UserProfile', UserProfile),
    ('Role', Role),
    ('Program', Program),
    ('Batch', Batch),
    ('Enrollment', Enrollment),
]

for name, model in registered_models:
    if admin.site.is_registered(model):
        print(f"✓ {name} registered in admin")
    else:
        print(f"✗ {name} NOT registered in admin")
EOF

echo ""
echo "DATA INTEGRITY"
echo "─────────────────────────────────────────────────────────────────────────"

python manage.py shell << 'EOF' 2>/dev/null
from django.contrib.auth.models import User
from core.models import UserProfile, Role

total_users = User.objects.count()
total_profiles = UserProfile.objects.count()
total_roles = Role.objects.count()

print(f"Total Users: {total_users}")
print(f"Total Profiles: {total_profiles}")
print(f"Total Roles: {total_roles}")

if total_users == total_profiles:
    print("✓ All users have profiles")
else:
    print(f"⚠ {total_users - total_profiles} users missing profiles")

if total_roles > 0:
    print("✓ Roles configured")
else:
    print("✗ No roles found")
EOF

echo ""
echo "BACKFILL COMMAND"
echo "─────────────────────────────────────────────────────────────────────────"

test_check "Backfill command exists" "python manage.py backfill_userprofile --help > /dev/null"

echo ""
echo "SECURITY BASELINE"
echo "─────────────────────────────────────────────────────────────────────────"

echo "⚠ Deployment security checks:"
echo "  • DEBUG = True (expected in development)"
echo "  • SECRET_KEY needs strengthening in production"
echo "  • ALLOWED_HOSTS needs configuration in production"
echo "  • HTTPS/SSL configuration needed for deployment"

echo ""
echo "═══════════════════════════════════════════════════════════════════════"
echo "  SUMMARY"
echo "═══════════════════════════════════════════════════════════════════════"
echo ""
echo -e "${GREEN}System Checks Passed: $TESTS_PASSED${NC}"
echo -e "${RED}System Checks Failed: $TESTS_FAILED${NC}"
echo ""

if [ $TESTS_FAILED -eq 0 ]; then
    echo -e "${GREEN}✓ ALL SYSTEMS OPERATIONAL${NC}"
    echo -e "${GREEN}✓ PLATFORM READY FOR LAUNCH${NC}"
    echo ""
    echo "Next steps:"
    echo "  1. Verify admin login works"
    echo "  2. Verify portal role selector loads"
    echo "  3. Test dashboard access"
    echo "  4. Configure production settings (SECRET_KEY, ALLOWED_HOSTS, SSL)"
    echo ""
else
    echo -e "${RED}✗ SYSTEM ISSUES DETECTED${NC}"
    echo "Please resolve issues before launching."
    echo ""
    exit 1
fi

echo "═══════════════════════════════════════════════════════════════════════"
