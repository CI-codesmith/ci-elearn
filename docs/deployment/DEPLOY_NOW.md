# 🚀 RENDER DEPLOYMENT - QUICK START GUIDE

**Status:** Ready to Deploy ✅  
**Date:** January 15, 2026  
**Repository:** `https://github.com/CI-codesmith/ci-elearn`

---

## ⏱️ Expected Time: 5-10 minutes

---

## 📋 PRE-DEPLOYMENT CHECKLIST

Before starting, have these ready:

- [ ] Browser with Render dashboard open: https://dashboard.render.com
- [ ] GitHub account connected to Render
- [ ] Secret key generated: https://djecrety.ir (generate a new one, copy it)
- [ ] This guide open for reference

---

## 🎯 DEPLOYMENT STEPS (Copy & Paste Ready)

### STEP 1: Create New Web Service (1 min)

1. Open: https://dashboard.render.com
2. Click: **"New +"** button
3. Select: **"Web Service"**
4. Click: **"Connect account"** or **"Select repository"**
5. Find and select: `CI-codesmith/ci-elearn`
6. Click: **"Connect"**

---

### STEP 2: Configure Service Settings (2 min)

Fill in the form with these exact values:

| Field | Value | Copy-Paste |
|-------|-------|-----------|
| **Name** | `ci-elearn-lms` | ✅ |
| **Runtime** | Python 3 | ✅ |
| **Build Command** | `pip install -r requirements.txt` | ✅ |
| **Start Command** | `gunicorn lms.wsgi:application` | ✅ **CRITICAL** |
| **Branch** | `main` | ✅ |
| **Auto Deploy** | Toggle to ✅ ON | ✅ |

**Copy-Paste for easy input:**
```
Build Command:
pip install -r requirements.txt

Start Command:
gunicorn lms.wsgi:application
```

---

### STEP 3: Add Environment Variables (2 min)

Scroll down to **"Environment Variables"** section.

**Add three variables:**

#### Variable 1: DEBUG
- **Key:** `DEBUG`
- **Value:** `False`

#### Variable 2: SECRET_KEY
- **Key:** `SECRET_KEY`
- **Value:** Generate at https://djecrety.ir
  - Go to the link
  - Copy the generated key (long string)
  - Paste into Render
- **Copy-Paste Example:**
  ```
  # Don't use this - generate your own!
  your_super_secret_key_here_from_djecrety_ir
  ```

#### Variable 3: ALLOWED_HOSTS
- **Key:** `ALLOWED_HOSTS`
- **Value:** `ci-elearn-lms.onrender.com`

**After adding all three variables, you should see:**
```
DEBUG                    = False
SECRET_KEY              = [your-generated-key]
ALLOWED_HOSTS           = ci-elearn-lms.onrender.com
```

---

### STEP 4: Deploy! (1 min)

1. Scroll down to bottom
2. Click: **"Create Web Service"** (blue button)
3. Wait for build to start...

---

## ⏳ DEPLOYMENT IN PROGRESS (2-4 minutes)

You'll see:

```
ⓘ Building...
↳ pip install -r requirements.txt
↳ Collecting packages...
↳ Installing...
✓ Build successful

ⓘ Deploying...
↳ Starting application...
✓ Deployed successfully
```

Once you see the ✓ green checkmarks, your app is live!

---

## 🌐 TEST YOUR DEPLOYMENT

Once deployment completes, you'll get a public URL:

```
https://ci-elearn-lms.onrender.com
```

**Test these URLs:**

| URL | Expected Result | Check |
|-----|-----------------|-------|
| `https://ci-elearn-lms.onrender.com/` | Home page loads | ✓ |
| `https://ci-elearn-lms.onrender.com/courses/` | Course listing page | ✓ |
| `https://ci-elearn-lms.onrender.com/student/login/` | Login page appears | ✓ |
| `https://ci-elearn-lms.onrender.com/static/css/chatake-brand.css` | CSS file loads | ✓ |

**Optional: Test Login**
```
Username: 2026IFML3601
Password: 316316
```

---

## 🎉 SUCCESS INDICATORS

When deployment is complete, you'll see:

✅ Service status shows **"Live"** (green)  
✅ URL working: `https://ci-elearn-lms.onrender.com`  
✅ Pages loading without 502 errors  
✅ Static files (CSS/JS) loading  
✅ Logs show no critical errors  

---

## 🔧 TROUBLESHOOTING (If Something Goes Wrong)

### 502 Bad Gateway Error
**Check:** Render dashboard → Logs  
**Look for:** Error messages about gunicorn or Django  
**Fix:** Verify Start Command = `gunicorn lms.wsgi:application`

### ModuleNotFoundError: No module named 'ci_elearn'
**Cause:** Wrong Start Command used  
**Fix:** Delete service, recreate with `gunicorn lms.wsgi:application`

### Secret Key Error
**Check:** Environment Variables  
**Verify:** SECRET_KEY is set and not empty  
**Fix:** Generate new key at https://djecrety.ir, update variable

### Build Fails
**Check:** Build logs in Render dashboard  
**Common causes:**
- Typo in Build Command
- Missing requirements.txt
- Python version compatibility

---

## 📱 NEXT STEPS (After Deployment)

### Immediate (Same day)
- [ ] Test all URLs listed above
- [ ] Share public URL with team
- [ ] Monitor logs for errors

### Soon (Optional)
- [ ] Add custom domain: `lms.chatakeinnoworks.com`
- [ ] Set up PostgreSQL database (replace SQLite)
- [ ] Enable auto-scaling if traffic increases

### Later (If needed)
- [ ] Add SSL certificate (Render provides free)
- [ ] Set up monitoring & alerts
- [ ] Configure backups for database

---

## 💾 IMPORTANT NOTES

1. **Auto-Deploy Enabled:** Every time you push to `main` branch, Render will automatically redeploy
2. **SQLite Database:** Uses local SQLite for now - data persists on Render
3. **Static Files:** Collected automatically during deployment (via Procfile release command)
4. **Logs:** Always check Render dashboard logs if something seems wrong

---

## 🎓 LEARNING RESOURCES

- Render Docs: https://render.com/docs
- Django on Render: https://render.com/docs/deploy-django
- Gunicorn: https://gunicorn.org
- Procfile reference: https://devcenter.heroku.com/articles/procfile

---

## ✨ YOU'RE ALL SET!

Everything is configured and ready. The deployment process is straightforward:

1. Fill in the form (copy-paste values provided)
2. Add 3 environment variables
3. Click "Create Web Service"
4. Wait 2-4 minutes
5. Your app is live! 🚀

---

**Questions?** Check the detailed guides in `docs/deployment/` folder

- `RENDER_DEPLOYMENT_READY.md` — Full checklist & reference
- `RENDER_SETUP_CORRECTED.md` — Detailed walkthrough
- `RENDER_CRITICAL_CORRECTION.md` — Common mistakes to avoid
