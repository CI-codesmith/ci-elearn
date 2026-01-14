# 🚀 Render Deployment Setup for `ci-elearn-lms`

## ✅ Corrected Configuration (January 15, 2026)

This guide corrects the start command error in previous instructions.

---

## 1. **Create New Web Service on Render**

1. Go to: [https://dashboard.render.com](https://dashboard.render.com)
2. Click: `New > Web Service`
3. Choose: **Connect GitHub repo**
   - Select: `CI-codesmith/ci-elearn`

---

## 2. **Service Settings (CORRECTED)**

| Field             | Value                                         |
| ----------------- | --------------------------------------------- |
| **Name**          | `ci-elearn-lms`                               |
| **Runtime**       | Python 3                                      |
| **Build Command** | `pip install -r requirements.txt`             |
| **Start Command** | `gunicorn lms.wsgi:application` ✅ **CORRECT** |
| **Region**        | Singapore or closest to India                 |
| **Branch**        | `main`                                        |
| **Auto Deploy**   | ✅ Enable                                      |

### ⚠️ **Important Note:**
- ❌ **WRONG:** `gunicorn ci_elearn.wsgi:application`
- ✅ **CORRECT:** `gunicorn lms.wsgi:application`

The project is named `lms`, not `ci_elearn`. Your `Procfile` already has the correct command.

---

## 3. **Environment Variables** (Required for Render)

Paste these into Render dashboard → Environment:

| Key             | Value                                                    | Notes |
| --------------- | -------------------------------------------------------- | ----- |
| `DEBUG`         | `False`                                                  | Always `False` in production |
| `SECRET_KEY`    | Generate one [here](https://djecrety.ir/)               | Must be unique & secret |
| `ALLOWED_HOSTS` | `ci-elearn-lms.onrender.com`                             | Will auto-add RENDER_EXTERNAL_HOSTNAME |
| `DATABASE_URL`  | `postgresql://...` (Render will provide if using PostgreSQL) | Optional - defaults to SQLite for now |

### Example SECRET_KEY Generation:
```bash
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 4. **Deploy Steps**

1. ✅ Click **Create Web Service**
2. ⏳ Wait 3–5 minutes for build to complete
3. 🌍 Get your public URL: `https://ci-elearn-lms.onrender.com`

### Build Output to Expect:
```
ⓘ Running build command: pip install -r requirements.txt
✓ Build successful
✓ Deployed successfully at https://ci-elearn-lms.onrender.com
```

---

## 5. **Verify Deployment**

Once deployed, test these URLs:

- ✅ Home: `https://ci-elearn-lms.onrender.com/`
- ✅ Courses: `https://ci-elearn-lms.onrender.com/courses/`
- ✅ Student Login: `https://ci-elearn-lms.onrender.com/student/login/`
- ✅ Admin: `https://ci-elearn-lms.onrender.com/admin/`

---

## 6. **Add Custom Domain (Optional)**

Once the default URL works:

### In Render Dashboard:
1. Select your service → **Settings** → **Domains**
2. Add custom domain: `lms.chatakeinnoworks.com`

### In Your Domain Provider (Cloudflare/GoDaddy):
1. Add CNAME record:
   - **Name:** `lms`
   - **Value:** `ci-elearn-lms.onrender.com`
2. Wait 5–15 minutes for DNS propagation

---

## 7. **Production Checklist**

- [x] `DEBUG = False` in environment variables
- [x] `SECRET_KEY` is unique and secret
- [x] `ALLOWED_HOSTS` includes your domain
- [x] `requirements.txt` is complete
- [x] `Procfile` has correct gunicorn command
- [x] `lms/wsgi.py` is properly configured
- [x] `lms/settings.py` reads environment variables
- [x] GitHub repo is public/connected to Render
- [ ] Database migration runs (via `release` command in Procfile)
- [ ] Static files collected (via `release` command in Procfile)

---

## 8. **Troubleshooting**

### Error: `ModuleNotFoundError: No module named 'lms'`
- ❌ Check Start Command is `gunicorn lms.wsgi:application` (not `ci_elearn`)
- ✅ Verify `lms/wsgi.py` exists and is correct

### Error: `ModuleNotFoundError: No module named 'dj_database_url'`
- ✅ Already fixed: `dj_database_url` is in `requirements.txt`

### 502 Bad Gateway Error
- Check Render logs: Dashboard → Service → Logs
- Verify environment variables are set correctly
- Ensure `SECRET_KEY` is not empty

### Static Files Not Loading
- ✅ `Procfile` includes: `python manage.py collectstatic --no-input`
- ✅ This runs automatically on deploy via `release` command

---

## 9. **Files Already Configured for Render**

Your project is **production-ready** for Render:

| File | Purpose | Status |
|------|---------|--------|
| `Procfile` | Render deployment config | ✅ Correct |
| `lms/wsgi.py` | WSGI application entry point | ✅ Correct |
| `lms/settings.py` | Environment variable support | ✅ Correct |
| `requirements.txt` | All dependencies | ✅ Complete |
| `render.yaml` | Advanced deployment config | ✅ Optional backup |

---

## 10. **Next Steps**

1. **Generate a SECRET_KEY:**
   ```bash
   python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

2. **On Render Dashboard:**
   - Create Web Service from `CI-codesmith/ci-elearn`
   - Set Start Command: `gunicorn lms.wsgi:application`
   - Add environment variables (DEBUG, SECRET_KEY, ALLOWED_HOSTS)
   - Click Deploy

3. **Monitor Deployment:**
   - Watch build logs in Render dashboard
   - Test public URL when ready
   - Check admin at `/admin/` if needed

---

**✅ Ready to deploy!** Your codebase is correctly configured for Render.
