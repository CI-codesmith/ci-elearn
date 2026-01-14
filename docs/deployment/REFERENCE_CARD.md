# 📌 Chatake Innoworks Deployment: One-Page Reference

## 🎯 MISSION: Deploy platform in 8 hours
**Status:** ✅ Code ready | ⏳ Deployment in progress

---

## 📍 CURRENT STATE
- ✅ Django app production-ready (settings.py configured)
- ✅ All dependencies in requirements.txt
- ✅ Brand CSS system created
- ✅ Deployment guides written
- ✅ All changes committed to git
- ⏳ Not yet pushed to GitHub

**Repo Status:** Ready to push to GitHub

---

## 🚀 5-STEP FAST TRACK

### 1️⃣ GITHUB (15 min)
```bash
cd ci-elearn-lms
git remote add origin https://github.com/YOUR-USERNAME/ci-elearn-lms.git
git push -u origin main
```
✅ **Then:** Code on GitHub, ready for Render

### 2️⃣ WEBFLOW (90 min)
- Create account → New site
- Design: Hero, About, Divisions (4 cards), Projects, Contact
- Colors: Maroon #7A1F2B, Bronze #B08D57, Charcoal #2E2E2E
- Add logo, fonts (Merriweather + Inter), footer
- Publish to staging → Review

✅ **Then:** Main site designed, ready for domain

### 3️⃣ RENDER (60 min)
- Sign in with GitHub
- Create Web Service from ci-elearn-lms repo
- Build: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --no-input`
- Start: `gunicorn lms.wsgi:application`
- Add env vars: SECRET_KEY, DEBUG=False, ALLOWED_HOSTS, DJANGO_SUPERUSER_PASSWORD
- Add PostgreSQL database
- Deploy

✅ **Then:** App live at chatake-lms.onrender.com

### 4️⃣ DOMAINS (30 min)
**Cloudflare DNS:**
```
www           CNAME → cdn.webflow.com
@             A     → 198.202.211.1 (Webflow IP)
edusphere     CNAME → chatake-lms.onrender.com
mindforge     CNAME → chatake-lms.onrender.com
interns       CNAME → chatake-lms.onrender.com
projects      CNAME → chatake-lms.onrender.com
```

**Webflow:** Publish to custom domain

**Render:** Add custom domains (edusphere, mindforge, interns, projects)

✅ **Then:** All domains live with SSL

### 5️⃣ TEST & LAUNCH (30 min)
- [ ] https://www.chatakeinnoworks.com → Webflow site loads
- [ ] https://edusphere.chatakeinnoworks.com → Django login loads
- [ ] Test login with admin account
- [ ] Check CSS/images load
- [ ] All domains have 🔒 SSL
- [ ] Announce to stakeholders

✅ **LAUNCH COMPLETE!**

---

## 🔑 CRITICAL INFO

### Environment Variables for Render
```
SECRET_KEY                  = <generate new one>
DEBUG                       = False
ALLOWED_HOSTS               = .chatakeinnoworks.com,localhost
DATABASE_URL                = postgresql://...@...
DJANGO_SUPERUSER_USERNAME   = admin
DJANGO_SUPERUSER_EMAIL      = admin@chatakeinnoworks.com
DJANGO_SUPERUSER_PASSWORD   = <strong password>
```

### Key URLs (After Launch)
```
Main:        https://www.chatakeinnoworks.com
EduSphere:   https://edusphere.chatakeinnoworks.com
MindforgeAI: https://mindforge.chatakeinnoworks.com
Internship:  https://interns.chatakeinnoworks.com
Projects:    https://projects.chatakeinnoworks.com
Admin:       https://edusphere.chatakeinnoworks.com/admin/
Login:       https://edusphere.chatakeinnoworks.com/student/login/
```

### Brand Colors
```
Charcoal:   #2E2E2E (primary text)
Maroon:     #7A1F2B (buttons, headers)
Bronze:     #B08D57 (accents)
Cream:      #F7F6F3 (backgrounds)
```

---

## 📊 TIMELINE (Total: ~330 min = 5.5 hours)

| Phase | Time | Status |
|-------|------|--------|
| GitHub push | 15 min | ⏳ Now |
| Webflow design | 90 min | ⏳ After GitHub |
| Render deploy | 60 min | ⏳ Parallel with Webflow |
| Domain/DNS | 30 min | ⏳ After Render |
| Test & launch | 30 min | ⏳ Final |
| **TOTAL** | **~330 min** | ✅ Under 8 hours |

---

## ⚠️ DO NOT FORGET

- ✅ Set SECRET_KEY env var (app will crash without it)
- ✅ Set DEBUG=False (security issue if True)
- ✅ Add DATABASE_URL for Postgres (or use SQLite fallback)
- ✅ Create superuser in Django admin (DJANGO_SUPERUSER_PASSWORD)
- ✅ Point Cloudflare DNS correctly (both A and CNAME records)
- ✅ Wait for SSL cert provisioning (~10 min after DNS points)
- ✅ Test domains before announcing

---

## 🆘 QUICK FIXES

| Problem | Fix |
|---------|-----|
| 502 Bad Gateway | Check Render logs, verify env vars, restart |
| CSS not loading | Run collectstatic, check STATIC_ROOT, clear cache |
| Login not working | Verify DATABASE_URL set, create superuser |
| Domain not resolving | Wait 15 min for DNS, verify Cloudflare records |
| SSL cert not issuing | Wait 10 min, verify DNS pointing to Render |
| DEBUG errors showing | Set DEBUG=False in Render env vars |

---

## 🎯 SUCCESS CHECKLIST

By end of deployment, you should have:

✅ www.chatakeinnoworks.com → Webflow site (polished, branded)  
✅ edusphere.chatakeinnoworks.com → Django login (working)  
✅ All subdomains responding with 200 OK  
✅ SSL certificates valid (🔒 in browser)  
✅ Static files loading (CSS, images visible)  
✅ Database working (can log in, data persists)  
✅ Admin panel accessible (/admin/)  
✅ No DEBUG mode information leaking  
✅ Branding consistent across all sites  
✅ Stakeholders notified & able to test  

---

## 📚 FULL DOCUMENTATION

For complete details, see:
- **DEPLOYMENT_GUIDE_COMPLETE.md** — Full 9-phase walkthrough
- **QUICK_START_CHECKLIST.md** — Prioritized action list
- **IMPLEMENTATION_SUMMARY.md** — Technical decisions & overview
- **lms/settings.py** — Production configuration
- **static/css/chatake-brand.css** — Design tokens

---

## 💡 KEY DECISIONS ALREADY MADE

| Decision | Choice | Why |
|----------|--------|-----|
| Frontend | Webflow | Fast, no-code, professional |
| Backend | Django | Existing code, scalable, secure |
| Hosting | Render + Postgres | Easy, free tier available, git integration |
| DNS | Cloudflare | Free, fast, SSL, caching |
| Static files | WhiteNoise | No extra server needed |
| Media storage | Local (then S3) | Simple start, plan scalability |

---

## 📞 BEFORE YOU START

Confirm you have:
- [ ] GitHub account ready
- [ ] Webflow account ready
- [ ] Render account ready
- [ ] Cloudflare account (likely already set up)
- [ ] Company logo (.png or .svg)
- [ ] Company description/content for website
- [ ] Contact email & info
- [ ] Strong password for superuser

---

## 🎬 BEGIN NOW

**Next action:** Follow the 5-Step Fast Track above, starting with GitHub push.

**Estimated completion:** ~5.5 hours (leaves 2.5-hour buffer for troubleshooting)

**Support:** See DEPLOYMENT_GUIDE_COMPLETE.md for detailed troubleshooting

---

**Ready? Let's launch! 🚀**
