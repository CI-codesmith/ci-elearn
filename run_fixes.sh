#!/bin/bash
cd /Users/akashchatake/Downloads/Chatake-Innoworks-Organization/ci-elearn-lms
python manage.py backfill_userprofiles
python manage.py check
echo "✅ All changes applied successfully"
