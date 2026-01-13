#!/bin/bash
cd /Users/akashchatake/Downloads/Chatake-Innoworks-Organization/ci-elearn-lms
python manage.py check
echo "✅ System check passed"
echo ""
echo "To start server, run:"
echo "python manage.py runserver"
