# Chatake Innoworks Rapid Deployment Guide

**Goal:** Deploy the complete Chatake Innoworks platform (Webflow main site + Django portals) within 8 hours.

**Status:** Code preparation COMPLETE ✅ | Next: GitHub Push → Render Deployment → DNS Configuration

---

## 📋 Phase 1: Codebase Preparation (✅ COMPLETED)

### What Was Done:
✅ Updated `settings.py` for production deployment
✅ Added environment variable support (SECRET_KEY, DEBUG, ALLOWED_HOSTS, DATABASE_URL)
✅ Integrated WhiteNoise middleware for static file serving
✅ Configured static/media file paths
✅ Added production security settings (HTTPS, HSTS, XSS protection)
✅ Generated `requirements.txt` with all dependencies
✅ Added production packages:
  - gunicorn==22.0.0 (WSGI server)
  - whitenoise==6.6.0 (static file serving)
  - dj-database-url==2.1.0 (environment DB config)
  - psycopg2-binary==2.9.9 (PostgreSQL support)
  - python-decouple==3.8 (env var management)

✅ Updated `.gitignore` to exclude sensitive files (db.sqlite3, .env, media/, staticfiles/)
✅ Created `render.yaml` for automated Render deployment
✅ Created `Procfile` for process management
✅ Created `static/css/chatake-brand.css` with complete design system:
  - Color tokens (Charcoal, Maroon, Bronze, Cream)
  - Typography system (Merriweather serif, Inter sans)
  - Button styles (primary, secondary, tertiary)
  - Responsive grid system
  - Component styles (cards, alerts, forms)

### Files Modified/Created:
```
lms/settings.py           ← Production-ready configuration
requirements.txt          ← All dependencies + production packages
.gitignore               ← Excludes sensitive files
render.yaml              ← Automated Render deployment config
Procfile                 ← Process definitions
static/css/chatake-brand.css ← Brand design system
```

---

## 🚀 Phase 2: Push to GitHub (IMMEDIATE NEXT STEP)

### Step 1: Commit All Changes
```bash
cd /Users/akashchatake/Downloads/Chatake-Innoworks-Organization/ci-elearn-lms

# Stage all changes
git add .

# Commit with message
git commit -m "Prepare for production deployment: add gunicorn, whitenoise, production settings, brand CSS"

# Verify status
git status
```

### Step 2: Create GitHub Repository
If not already created:
1. Go to https://github.com/new
2. Create repository: `ci-elearn-lms` (or similar)
3. Set to Private (recommended for educational platform)
4. Do NOT initialize with README (we already have one)

### Step 3: Push to GitHub
```bash
# Add remote (replace with your GitHub username/repo)
git remote add origin https://github.com/<YOUR-USERNAME>/ci-elearn-lms.git

# Push to main branch
git branch -M main
git push -u origin main

# Verify
git remote -v  # Should show GitHub URL
```

**Expected Output:**
```
origin  https://github.com/<your-username>/ci-elearn-lms.git (fetch)
origin  https://github.com/<your-username>/ci-elearn-lms.git (push)
```

---

## 🌐 Phase 3: Set Up Webflow Main Site (60–90 minutes)

### Step 1: Create Webflow Project
1. Go to https://webflow.com
2. Sign in or create account
3. Click "Create new" → "Blank site"
4. Choose a template or start blank
5. Name it: "Chatake Innoworks"

### Step 2: Design Main Site Sections
Use the following structure and content:

#### **Hero Section**
- Background: Gradient (Charcoal #2E2E2E to Maroon #7A1F2B)
- Heading: "Engineering Ideas. Empowering Innovation."
- Subheading: "Bridging academia and industry through innovative technology solutions"
- CTA Buttons:
  - "Explore Divisions" (Primary button - Maroon)
  - "Learn More" (Secondary button - Bronze)

#### **About Us Section**
- Title: "About Chatake Innoworks"
- Content: (from your company PDF)
  - Mission statement
  - Vision
  - Core values (family-oriented, innovation-focused, etc.)
- Add company logo/banner

#### **Divisions Section (Grid of 4 Cards)**
Each card should have:
- Division name
- Icon or color accent
- 3-4 line description

**1. EduSphere (Academic Blue #1F7A8A)**
- K–12 and college-level educational programs
- Coaching for 8th–12th grade
- Student & teacher portals
- CTA: "Explore EduSphere"

**2. MindforgeAI (Tech Blue #4A90E2)**
- Advanced AI/ML courses and research
- Industry collaborations
- Research project management
- CTA: "Explore MindforgeAI"

**3. GreenWorks (Green #2ECC71)**
- Agriculture and sustainability innovation
- Apollo (AgriTech), AgriVerse (Farm AI)
- Sustainable solutions for farming
- CTA: "Explore GreenWorks"

**4. CodeSmith Systems (Dark Slate #34495E)**
- Software development & IT services
- Internship programs
- Project collaboration
- CTA: "Explore CodeSmith"

#### **Key Projects/Initiatives Section**
- Brief showcase of major projects (Apollo, AgriVerse, ArchLang, etc.)
- Could be cards or a timeline
- Link to relevant portals

#### **Contact Section**
- Contact form (basic)
- Company info
  - Email: admin@chatakeinnoworks.com
  - Address: (from your profile)
  - Phone: (if available)
- Social media links (if any)

### Step 3: Apply Branding
- **Logo:** Upload Chatake Innoworks logo (use consistently in header)
- **Colors:** Define design tokens in Webflow
  - Primary: Maroon #7A1F2B
  - Secondary: Bronze #B08D57
  - Accent: Charcoal #2E2E2E
  - Background: Cream #F7F6F3
- **Typography:**
  - Headings: Merriweather (serif) or similar elegant serif
  - Body: Inter or Segoe UI (sans-serif)
  - Font sizes: H1 (2.5rem), H2 (2rem), Body (1rem)
- **Spacing & Layout:** Consistent padding/margins, responsive design
- **Footer:** Copyright, company name, links to portals

### Step 4: Navigation
- Header menu:
  - Home
  - About Us
  - Divisions
  - Projects
  - Contact
- Portal links (can be disabled temporarily if portals not live yet):
  - Student Login → `/student/login/`
  - Admin Panel → `/admin/`
  - Faculty Portal → `/portal/`

### Step 5: Test in Webflow
- Use Webflow's preview to test all pages
- Check responsiveness on mobile (Webflow does this automatically)
- Verify all links work (test with external links to GitHub, etc.)
- Check form submission (Webflow will email you submissions)

### Step 6: Publish to Staging
- In Webflow, click "Publish" → "Publish to staging domain"
- Get the staging URL (e.g., chatake-innoworks-v1.webflow.io)
- Share this with stakeholders for review before going live

---

## 🌍 Phase 4: Connect Domain & DNS (15 minutes)

### Step 1: Point Domain to Webflow
1. **In Webflow project:**
   - Go to Project Settings → Hosting
   - Click "Add custom domain"
   - Enter: `chatakeinnoworks.com`
   - Webflow will provide DNS records to add

2. **In Cloudflare DNS** (or your domain registrar):
   - Log in to Cloudflare dashboard
   - Go to chatakeinnoworks.com domain
   - DNS → Records
   - Add the records Webflow provides:
     ```
     Type: CNAME
     Name: www
     Value: cdn.webflow.com
     Proxy: DNS only (disable proxy)
     
     Type: A
     Name: @
     Value: 198.202.211.1 (or Webflow's provided IP)
     Proxy: DNS only (disable proxy)
     ```
   - Save all records
   - Set SSL/TLS to "Full" mode in Cloudflare
   - Wait for DNS propagation (~5–15 min)

### Step 2: Publish Webflow Site
- In Webflow, click "Publish" → confirm to publish to custom domain
- Webflow will provision SSL (Let's Encrypt)
- Status will show "Provisioning SSL" then "Live"

### Step 3: Test Main Site
```bash
# In terminal, test the domain
curl -I https://www.chatakeinnoworks.com
# Should return 200 OK

# Open in browser
# https://www.chatakeinnoworks.com should load the site
```

**Expected:** Site is live with custom domain and SSL. All pages accessible.

---

## 🎯 Phase 5: Deploy Django to Render (60 minutes)

### Step 1: Create Render Account & Link GitHub
1. Go to https://render.com
2. Sign up with GitHub (recommended for easy repo connection)
3. Authorize Render to access your GitHub repos

### Step 2: Create Web Service
1. Click "New +" → "Web Service"
2. Select the `ci-elearn-lms` repository (from your GitHub)
3. Choose branch: `main`
4. **Settings:**
   - Name: `chatake-lms`
   - Environment: Python
   - Region: Oregon (or closest to users)
   - Plan: **Free** (starts here, upgrade later if needed)
   - Build Command:
     ```
     pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --no-input
     ```
   - Start Command:
     ```
     gunicorn lms.wsgi:application
     ```

### Step 3: Set Environment Variables
In Render dashboard, go to your web service → Environment:

Add the following variables:

| Key | Value | Type |
|-----|-------|------|
| `SECRET_KEY` | Generate a strong key (see below) | Secret |
| `DEBUG` | False | Standard |
| `ALLOWED_HOSTS` | `.chatakeinnoworks.com,localhost,127.0.0.1` | Standard |
| `DJANGO_SUPERUSER_USERNAME` | admin | Standard |
| `DJANGO_SUPERUSER_EMAIL` | admin@chatakeinnoworks.com | Standard |
| `DJANGO_SUPERUSER_PASSWORD` | (strong password) | Secret |

**Generate SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**Generate strong password:**
```bash
openssl rand -base64 32
```

### Step 4: Add PostgreSQL Database (Recommended)
1. In Render, click "New +" → "PostgreSQL"
2. Name: `chatake-db`
3. Database: `chatake_lms`
4. Region: Oregon
5. Plan: **Free**
6. Create
7. Once created, Render will show `DATABASE_URL`
8. Copy the `DATABASE_URL` value and add it to your Web Service env vars

### Step 5: Deploy
1. Click "Create Web Service"
2. Render will automatically start building (watch the logs)
3. Expected output:
   ```
   Building: pip install -r requirements.txt
   Building: python manage.py migrate
   Building: python manage.py collectstatic --no-input
   Starting: gunicorn lms.wsgi:application
   ```
4. Once complete, Render provides a URL like: `chatake-lms.onrender.com`
5. Test it: Open https://chatake-lms.onrender.com in browser
6. Should see Django homepage or login page

**If errors occur:**
- Check build logs in Render dashboard
- Common issues:
  - Missing environment variables → Add them
  - Migration errors → Check database setup
  - Static files not loading → Ensure `collectstatic` ran
  - Import errors → Check requirements.txt completeness

---

## 🎓 Phase 6: Launch EduSphere Portal (30 minutes)

### Step 1: Add Domain to Render
1. In Render Web Service settings → Custom Domains
2. Click "Add Custom Domain"
3. Enter: `edusphere.chatakeinnoworks.com`
4. Render will ask to add a DNS record
5. Copy the provided CNAME value

### Step 2: Configure Cloudflare DNS
1. Go to Cloudflare → chatakeinnoworks.com → DNS
2. Add CNAME record:
   ```
   Type: CNAME
   Name: edusphere
   Value: <Render-provided CNAME or onrender.com URL>
   Proxy: Off (DNS only)
   ```
3. Save
4. Wait for propagation (~5 min)

### Step 3: Verify SSL Certificate
1. Back in Render, the domain status should change to "Verifying"
2. Once SSL is issued, status shows "Live"
3. May take 5–10 minutes

### Step 4: Test EduSphere Portal
```bash
# Test domain resolution
curl -I https://edusphere.chatakeinnoworks.com

# Open in browser
# https://edusphere.chatakeinnoworks.com should load
```

**Expected:** EduSphere portal loads with login page.

### Step 5: Create Test Student Account
Since Django admin is available:
1. Visit: `https://edusphere.chatakeinnoworks.com/admin/`
2. Log in with superuser credentials (from env vars: admin / password)
3. Go to Students → Add Student
4. Create test account:
   - Username: `test.student`
   - Password: (any strong password)
   - User: (create new user first if needed)
5. Save

### Step 6: Test Student Login
1. Go to: `https://edusphere.chatakeinnoworks.com/student/login/`
2. Log in with test credentials
3. Should redirect to student dashboard
4. Verify courses/content displays

---

## 🌐 Phase 7: Set Up Additional Portals DNS (15 minutes)

### Step 1: Add Custom Domains to Render (Alternative: Wildcard)

**Option A: Individual Subdomains (4 separate custom domains)**
1. In Render Web Service → Custom Domains
2. Add each subdomain one by one:
   - `mindforge.chatakeinnoworks.com`
   - `interns.chatakeinnoworks.com`
   - `projects.chatakeinnoworks.com`
   - (Optional) `greenworks.chatakeinnoworks.com`

**Option B: Wildcard Domain (Recommended)**
1. In Render Web Service → Custom Domains
2. Add: `*.chatakeinnoworks.com`
3. Render will provide verification records
4. This covers ALL subdomains with one custom domain slot

### Step 2: Configure Cloudflare DNS
Add CNAME records for each subdomain:

```
mindforge    CNAME → <Render-URL or wildcard>
interns      CNAME → <Render-URL or wildcard>
projects     CNAME → <Render-URL or wildcard>
greenworks   CNAME → <Render-URL or wildcard> (optional)
```

Or if using wildcard in Render:
```
*            CNAME → <Render-wildcard-URL>
```

### Step 3: Test Each Domain
```bash
curl -I https://mindforge.chatakeinnoworks.com
curl -I https://interns.chatakeinnoworks.com
curl -I https://projects.chatakeinnoworks.com
```

All should return 200 OK (even if showing the same content as EduSphere for now – that's fine).

---

## 🎨 Phase 8: Apply Branding Across Portals (30 minutes)

### Step 1: Update Base Django Template
Open `templates/base.html` (or main template):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatake Innoworks - {% block title %}{% endblock %}</title>
    
    <!-- Chatake Brand CSS -->
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/chatake-brand.css' %}">
    
    <!-- Add any other stylesheets -->
    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- Header -->
    <header>
        <div class="navbar">
            <div class="navbar-brand">
                <img src="{% static 'images/chatake-logo.png' %}" alt="Chatake Innoworks">
                Chatake Innoworks
            </div>
            <ul class="navbar-menu">
                <li><a href="https://www.chatakeinnoworks.com">Home</a></li>
                <li><a href="https://www.chatakeinnoworks.com#about">About</a></li>
                <li><a href="/student/login/">Student Portal</a></li>
                <li><a href="/admin/">Admin</a></li>
            </ul>
        </div>
    </header>
    
    <!-- Main Content -->
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <!-- Footer -->
    <footer>
        <div class="footer-content">
            <div class="footer-section">
                <h4>Chatake Innoworks</h4>
                <p>Engineering Ideas. Empowering Innovation.</p>
            </div>
            <div class="footer-section">
                <h4>Quick Links</h4>
                <a href="https://www.chatakeinnoworks.com">Main Site</a>
                <a href="/admin/">Admin Panel</a>
                <a href="/student/login/">Student Login</a>
            </div>
            <div class="footer-section">
                <h4>Contact</h4>
                <p>Email: <a href="mailto:admin@chatakeinnoworks.com">admin@chatakeinnoworks.com</a></p>
            </div>
        </div>
        <div class="footer-bottom">
            &copy; 2026 Chatake Innoworks Pvt. Ltd. All rights reserved.
        </div>
    </footer>
    
    {% block extra_js %}{% endblock %}
</body>
</html>
```

### Step 2: Add Company Logo
1. Save your company logo as: `static/images/chatake-logo.png` (or .svg)
2. Commit and push to GitHub
3. On Render redeploy (or auto-deploys after push)

### Step 3: Test Branding
1. Visit each portal:
   - https://edusphere.chatakeinnoworks.com
   - https://mindforge.chatakeinnoworks.com
   - https://interns.chatakeinnoworks.com
2. Verify:
   - Logo appears in header
   - Colors match brand (Maroon buttons, Bronze accents)
   - Typography is consistent
   - Footer has company info

---

## ✅ Phase 9: Final Launch Checklist

### Pre-Launch Testing (30 minutes)

**Main Website:**
- [ ] https://www.chatakeinnoworks.com loads
- [ ] All pages accessible (About, Divisions, Contact, etc.)
- [ ] Navigation links work
- [ ] Forms submit successfully
- [ ] Contact form works
- [ ] Mobile responsive (test on phone/tablet)
- [ ] SSL certificate valid (no warnings)

**EduSphere Portal:**
- [ ] https://edusphere.chatakeinnoworks.com loads
- [ ] Student login works with test account
- [ ] Dashboard displays after login
- [ ] Can view course content
- [ ] Logout works
- [ ] Static files load (CSS, JS, images)
- [ ] Branding consistent with main site

**Other Portals (Basic):**
- [ ] https://mindforge.chatakeinnoworks.com → 200 OK
- [ ] https://interns.chatakeinnoworks.com → 200 OK
- [ ] https://projects.chatakeinnoworks.com → 200 OK
- [ ] Each has SSL certificate

**Database & Security:**
- [ ] Superuser account works (/admin/)
- [ ] DEBUG = False (no debug toolbar)
- [ ] HTTPS redirect active (http → https)
- [ ] No sensitive data in logs

### Launch Steps

1. **Announce Soft Launch**
   - Email to stakeholders: "Chatake Innoworks platform is now live for beta testing"
   - Provide URLs:
     - Main site: https://www.chatakeinnoworks.com
     - EduSphere: https://edusphere.chatakeinnoworks.com
     - Test credentials: username / password
   - Request feedback

2. **Monitor Systems**
   - Check Render logs for errors
   - Monitor uptime (Render provides uptime dashboard)
   - Check student login attempts (Django admin → Users)

3. **Iterate & Refine**
   - Fix any bugs from beta testing
   - Add missing content to portals
   - Expand to other divisions as ready

---

## 📊 Deployment Timeline Summary

| Phase | Duration | Status |
|-------|----------|--------|
| 1. Codebase Prep | 30 min | ✅ DONE |
| 2. GitHub Push | 15 min | ⏳ NEXT |
| 3. Webflow Main Site | 90 min | ⏳ NEXT |
| 4. Domain + DNS (Main) | 15 min | ⏳ NEXT |
| 5. Render Deployment | 60 min | ⏳ NEXT |
| 6. EduSphere Portal | 30 min | ⏳ NEXT |
| 7. DNS (Other Portals) | 15 min | ⏳ NEXT |
| 8. Branding Alignment | 30 min | ⏳ NEXT |
| 9. Final Testing & Launch | 30 min | ⏳ NEXT |
| **TOTAL** | **~315 min (~5.5 hours)** | ✅ Within 8-hour goal |

---

## 🔗 Quick Reference: Key URLs (After Launch)

**Public-Facing:**
- Main Site: https://www.chatakeinnoworks.com
- About Page: https://www.chatakeinnoworks.com#about
- Divisions: https://www.chatakeinnoworks.com#divisions

**Portals:**
- EduSphere: https://edusphere.chatakeinnoworks.com
- MindforgeAI: https://mindforge.chatakeinnoworks.com
- Internship: https://interns.chatakeinnoworks.com
- Projects: https://projects.chatakeinnoworks.com

**Admin:**
- Django Admin: https://edusphere.chatakeinnoworks.com/admin/
- Student Login: https://edusphere.chatakeinnoworks.com/student/login/

---

## 📞 Troubleshooting Quick Guide

**Problem: Webflow domain not resolving**
- Solution: Wait 15 min for DNS propagation. Verify Cloudflare records match Webflow requirements.

**Problem: Render app shows "502 Bad Gateway"**
- Solution: Check build logs for errors. Likely missing env var or migration failure. Add SECRET_KEY and DATABASE_URL.

**Problem: Static files not loading on Render**
- Solution: Ensure `collectstatic` ran. Check STATIC_ROOT and STATICFILES_STORAGE settings. May need to run manually:
  ```bash
  python manage.py collectstatic --no-input
  ```

**Problem: SSL certificate not issuing on Render**
- Solution: Wait 10 min for Let's Encrypt provisioning. Verify DNS is pointing to Render. Check Render domain status.

**Problem: Can't log in to Django admin**
- Solution: Verify DJANGO_SUPERUSER_PASSWORD env var is set. May need to create superuser manually:
  ```bash
  python manage.py createsuperuser
  ```

---

## 🎉 Success Metrics

You'll know everything is working when:

✅ **www.chatakeinnoworks.com** → Webflow site loads with all sections  
✅ **edusphere.chatakeinnoworks.com** → Student login works, dashboard accessible  
✅ **mindforge.chatakeinnoworks.com** → Domain resolves with SSL  
✅ **All subdomains** → Respond with 200 OK  
✅ **Database** → Student/user data persists  
✅ **Branding** → Consistent colors, logos, fonts across all pages  
✅ **Security** → No DEBUG messages, HTTPS enforced  
✅ **Forms** → Contact forms, logins, submissions work  

---

## 📚 Next Steps After Launch (Phase 4 Improvements)

- [ ] Populate course content for each division portal
- [ ] Invite actual students/teachers to test
- [ ] Set up email notifications (SendGrid or Mailgun)
- [ ] Configure S3 for media storage (for persistent file uploads)
- [ ] Add analytics (Google Analytics for main site, Django logging for portals)
- [ ] Set up backup strategy for database
- [ ] Create detailed user documentation/guides
- [ ] Implement mobile app (if needed)
- [ ] Scale infrastructure based on actual user load

---

**Last Updated:** January 14, 2026  
**Prepared for:** Chatake Innoworks Pvt. Ltd.  
**Platform Status:** Ready for Deployment ✅
