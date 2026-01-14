# Chatake Innoworks LMS Platform

Modern Django-based Learning Management System powering the Chatake Innoworks education ecosystem.

## 🚀 Quick Start

### Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

### Deployment
See [docs/deployment/REFERENCE_CARD.md](docs/deployment/REFERENCE_CARD.md) for quick start.

## 📁 Project Structure

```
ci-elearn-lms/
├── lms/                    # Django project settings
├── students/               # Student management app
├── courses/                # Course content app
├── assessments/            # Assessments/quizzes
├── publiccatalog/          # Public course catalog
├── publicsite/             # Public website
├── portal/                 # Student portal
├── edusphere/              # EduSphere division
├── internship/             # Internship management
├── projects/               # Project collaboration
├── accounts/               # User accounts
├── templates/              # Django templates
├── static/                 # Static files (CSS, JS, images)
├── media/                  # User uploads
├── docs/
│   ├── deployment/         # 📍 Deployment documentation
│   │   ├── REFERENCE_CARD.md           (one-page quick start)
│   │   ├── QUICK_START_CHECKLIST.md    (5-step fast track)
│   │   ├── DEPLOYMENT_GUIDE_COMPLETE.md (full walkthrough)
│   │   └── IMPLEMENTATION_SUMMARY.md   (technical details)
│   └── guides/             # Additional guides
├── requirements.txt        # Python dependencies
├── manage.py              # Django management
├── render.yaml            # Render deployment config
├── Procfile               # Process definitions
└── README.md              # This file
```

## 📚 Documentation

### For Deployment
- **[Reference Card](docs/deployment/REFERENCE_CARD.md)** ⭐ **START HERE** — One-page quick reference
- **[Quick Start Checklist](docs/deployment/QUICK_START_CHECKLIST.md)** — 5-step fast track with timing
- **[Complete Guide](docs/deployment/DEPLOYMENT_GUIDE_COMPLETE.md)** — Detailed 9-phase walkthrough
- **[Implementation Summary](docs/deployment/IMPLEMENTATION_SUMMARY.md)** — Technical decisions & details

### Features
- **File-based Course System**: Reads from `/subjects/machine-learning/` on disk
- **Student Portal**: Login, dashboard, course access
- **Podcast Integration**: Spotify episode embeddings
- **Public Access**: Course browsing without login
- **Admin Dashboard**: Manage users, content, assessments
- **Responsive Design**: Mobile-friendly interface

## 🎨 Branding
- Color Scheme: Charcoal, Maroon, Bronze, Cream
- Typography: Merriweather (headings), Inter (body)
- Design System: `static/css/chatake-brand.css`

## 🔒 Security
- Production settings with environment variables
- HTTPS/SSL support
- CSRF protection
- Secure session handling
- Database credentials in env vars (never committed)

## 📦 Technology Stack
- **Backend**: Django 4.2
- **Database**: PostgreSQL (prod) / SQLite (dev)
- **Static Files**: WhiteNoise
- **Server**: Gunicorn
- **Frontend**: Django Templates + Bootstrap/Tailwind
- **Hosting**: Render.com

## 🌐 Live Sites
- **Main Site**: https://www.chatakeinnoworks.com (Webflow)
- **EduSphere**: https://edusphere.chatakeinnoworks.com
- **MindforgeAI**: https://mindforge.chatakeinnoworks.com
- **Internship**: https://interns.chatakeinnoworks.com
- **Projects**: https://projects.chatakeinnoworks.com

## 📋 Requirements
- Python 3.11+
- Django 4.2
- PostgreSQL 12+
- See `requirements.txt` for full list

## 🚀 Deployment
This project is configured for deployment on [Render](https://render.com):
- Auto-deploys from GitHub
- PostgreSQL included
- Environment variables via Render dashboard
- SSL/HTTPS automatic

See [docs/deployment/](docs/deployment/) for detailed deployment instructions.

## 🤝 Contributing
1. Create a feature branch
2. Make changes
3. Test locally: `python manage.py test`
4. Commit with clear messages
5. Push to GitHub
6. Create Pull Request

## 📝 License
© 2026 Chatake Innoworks Pvt. Ltd.

## 📞 Support
For deployment issues, see [docs/deployment/DEPLOYMENT_GUIDE_COMPLETE.md](docs/deployment/DEPLOYMENT_GUIDE_COMPLETE.md#-common-pitfalls-to-avoid).

---

**Status**: ✅ Production Ready | **Last Updated**: January 15, 2026
