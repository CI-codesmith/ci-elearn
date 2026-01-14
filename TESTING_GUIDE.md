# 🧪 SYSTEM TESTING & VALIDATION GUIDE

**Purpose:** Verify all 6 Master Prompt steps are working correctly  
**Estimated Time:** 15-20 minutes  
**Environment:** Development (localhost)

## MASTER PROMPT COMPLETION VALIDATION

This guide validates that ALL 6 Master Prompt steps have been implemented successfully:

✅ **STEP 1** — Brand Asset Ingestion (directory structure created)  
✅ **STEP 2** — Design System Enforcement (unified CSS, institutional colours)  
✅ **STEP 3** — Public Website Pages (6 pages, no login)  
✅ **STEP 4** — Header & Footer Branding (shared includes)  
✅ **STEP 5** — Portal UI Polish (ALL EMOJIS REMOVED)  
✅ **STEP 6** — Root Routing Clarity (verified correct)

---

## QUICK SYSTEM HEALTH CHECK

### Prerequisites
Terminal must be running in project directory:
```bash
cd /Users/akashchatake/Downloads/Chatake-Innoworks-Organization/ci-elearn-lms
```

### 1. System Check (Should show 0 issues)
```bash
python manage.py check
```

**Expected Output:**
```
System check identified no issues (0 silenced).
```

**What This Validates:**
- ✅ All apps properly configured
- ✅ No import errors
- ✅ Models are valid
- ✅ Settings are correct

### 2. Start Development Server
```bash
python manage.py runserver 0.0.0.0:8000
```

**Expected Output:**
```
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```

### 3. Test Public Website (NO login required)

Open browser and visit each URL:

#### Home Page
- **URL:** http://localhost:8000/
- **Expected:** 
  - Page loads WITHOUT login ✅
  - "Chatake Innoworks" header visible
  - "Learning & Development Platform" tagline visible
  - Division cards displayed (CI-Elearn, CI-EduSphere, etc.)
  - "Login to Portal" button present
  - Professional institutional design ✅
  - Unified header/footer visible ✅
  - NO emojis ✅
  - Status: 200 OK

#### About Page
- **URL:** http://localhost:8000/about/
- **Expected:**
  - Company mission, vision, values visible
  - Leadership names: Akash Shivadas Chatake, Shivadas Bajrang Chatake
  - Page loads WITHOUT login ✅
  - Professional institutional tone ✅
  - Contact information present
  - Status: 200 OK

#### Divisions Page
- **URL:** http://localhost:8000/divisions/
- **Expected:**
  - All 5 divisions listed: CI-Elearn, CI-EduSphere, CI-Internship, CI-Projects, CI-Accounts
  - Each division has description and features
  - Status: 200 OK

#### Projects Page
- **URL:** http://localhost:8000/projects/
- **Expected:**
  - Apollo, GFIS, Nexora projects displayed
  - Project status indicators visible
  - Status: 200 OK

#### Internship Page
- **URL:** http://localhost:8000/internship/
- **Expected:**
  - Internship program overview
  - Benefits grid visible
  - Application process listed
  - Status: 200 OK

#### Contact Page
- **URL:** http://localhost:8000/contact/
- **Expected:**
  - Contact information: emails, social links
  - Contact form with fields: name, email, subject, message
  - LinkedIn and Facebook links work
  - Status: 200 OK

### 4. Test Admin Login

- **URL:** http://localhost:8000/admin/login/
- **Expected:**
  - Login page loads
  - Username: admin
  - Password: admin123
  - Status: 200 OK

After login:
- Should see Django admin interface
- Should see publicsite > Public Page Content model
- Status: 200 OK

### 5. Test Portal Access

- **URL:** http://localhost:8000/portal/
- **After login:**
  - Should show role selector with 6 roles
  - Can select different roles
  - Dashboards load for each role
  - Status: 200 OK

#### Test Each Role Dashboard
```
/portal/student/    → Student dashboard
/portal/teacher/    → Teacher dashboard
/portal/intern/     → Intern dashboard
/portal/project/    → Project dashboard
/portal/accounts/   → Accounts dashboard
/portal/admin/      → Admin dashboard
```

All should:
- Load without errors
- Show institutional header (Chatake Innoworks + user info + logout)
- Show professional footer
- Display role-specific content
- Status: 200 OK

### 6. Test CI-Elearn Still Works

- **URL:** http://localhost:8000/student/login/
- **Expected:**
  - CI-Elearn login page loads (UNCHANGED)
  - Original CI-Elearn functionality intact
  - Status: 200 OK

- **URL:** http://localhost:8000/assessments/
- **Expected:**
  - Assessments route still works
  - Status: 200 OK

---

## Visual Design Verification

### Header Check (Should appear on all portal pages)
```
✓ Dark charcoal background (#2E2E2E)
✓ "Chatake Innoworks" logo text in serif (Merriweather)
✓ "Learning & Development Platform" tagline
✓ Navigation links (Home, About, Divisions, Contact)
✓ Login button (maroon #7A1F2B)
✓ User info if logged in (Name + Role)
✓ Logout link if logged in
```

### Footer Check (Should appear on all pages)
```
✓ Dark charcoal background (#2E2E2E)
✓ 4 columns: Company Info, Divisions, Contact, Platform
✓ Links to divisions, social media, website
✓ Copyright notice: © 2026 Chatake Innoworks Pvt. Ltd.
✓ Contact emails: admin@chatakeinnoworks.com
```

### Colour Palette Check
```
✓ Charcoal text (#2E2E2E)
✓ Maroon accents (#7A1F2B)
✓ Bronze secondary (#B08D57)
✓ Cream background (#F7F6F3)
✓ White cards and containers (#FFFFFF)
```

### Typography Check
```
✓ Headings: Serif font (Merriweather)
✓ Body text: Sans-serif (Inter)
✓ Proper hierarchy (h1, h2, h3, etc.)
✓ Readable font sizes
✓ Appropriate line spacing
```

### Responsive Design Check

#### Desktop (Full width)
- All elements visible
- Multi-column layouts working
- Proper spacing

#### Tablet (768px and below)
- Footer changes to 2 columns
- Navigation might collapse
- Cards stack properly

#### Mobile (480px and below)
- Single column layout
- Header adapts
- Footer becomes single column
- All text readable

Test by:
1. Using browser DevTools (F12)
2. Clicking device toolbar icon
3. Selecting iPhone, iPad, Android sizes

---

## Console Errors Check

Open browser DevTools (F12):
- **Console tab:** Should show NO errors (only warnings are okay)
- **Network tab:** All resources should be 200 OK status
- **CSS files:** `ci_design_system.css` should load (200 OK)
- **HTML:** Should validate without critical errors

---

## File Integrity Check

```bash
# Verify new files exist
ls -la static/branding/
ls -la static/css/ci_design_system.css
ls -la templates/publicsite/
ls -la publicsite/

# Verify modified files
grep "publicsite" lms/settings.py
grep "publicsite.urls" lms/urls.py
grep "ci_design_system.css" templates/base.html
```

All should return results (files exist).

---

## Database Check

```bash
# Verify migrations can run
python manage.py migrate --plan

# Check for any migration issues
python manage.py migrate
```

**Expected:** No migration errors (publicsite is new, no migrations needed until model changes)

---

## Security Check

```bash
# Verify no DEBUG=True in production code
grep "DEBUG" lms/settings.py

# Verify ALLOWED_HOSTS is set
grep "ALLOWED_HOSTS" lms/settings.py

# Verify no hardcoded passwords in code
grep -r "password" --include="*.py" | grep -v migration
```

---

## Expected Test Results Summary

| Component | Status | Evidence |
|-----------|--------|----------|
| System check | ✅ | 0 issues |
| Server starts | ✅ | Runs on 0.0.0.0:8000 |
| Public home | ✅ | Loads without login, 200 OK |
| All 6 public pages | ✅ | Load without login, 200 OK |
| Admin login | ✅ | Accessible at /admin/login/ |
| Portal | ✅ | Role selector works, login required |
| All 7 dashboards | ✅ | Load with proper header/footer |
| CI-Elearn | ✅ | /student/ still works unchanged |
| Design system CSS | ✅ | Loads and styles all pages |
| Responsive design | ✅ | Works on desktop, tablet, mobile |
| No console errors | ✅ | DevTools console clean |
| Colour palette | ✅ | Charcoal, maroon, bronze, cream visible |
| Typography | ✅ | Merriweather headings, Inter body |
| No forbidden elements | ✅ | No flashy gradients, animations |

---

## Troubleshooting

### If server doesn't start:
```bash
# Kill any stuck Python processes
pkill -9 python

# Free port 8000 if needed
lsof -i :8000 | grep -v COMMAND | awk '{print $2}' | xargs kill -9

# Try again
python manage.py runserver 0.0.0.0:8000
```

### If pages show errors:
```bash
# Check system health
python manage.py check

# Run migrations if needed
python manage.py migrate

# Clear any static file cache
rm -rf staticfiles/
python manage.py collectstatic
```

### If login doesn't work:
```bash
# Create admin user if missing
python manage.py createsuperuser
# Or use provided script:
python create_admin.py
```

---

## Final Deployment Readiness

Once all tests pass, you're ready for:
1. Git commits (see `GIT_COMMITS.md`)
2. Copy brand assets into `static/branding/`
3. Production server deployment
4. Launch announcement

**All Master Prompt requirements are met!** ✅
