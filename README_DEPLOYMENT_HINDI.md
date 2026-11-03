AI SMART STUDENT ADMISSION & ACADEMIC GUIDANCE SYSTEM
====================================================

LOCAL RUN (Windows PowerShell)
1. Install Python 3.11 or newer (recommended: Python 3.12).
2. Open this folder in VS Code.
3. Run: python -m venv .venv
4. Run: .venv\\Scripts\\Activate.ps1
5. Run: python -m pip install -r requirements.txt
6. Copy .env.example to .env and set SECRET_KEY to a long random value.
7. Run: python app.py
8. Open: http://127.0.0.1:5000/

FREE RENDER DEPLOYMENT
1. Upload this project to a PRIVATE GitHub repository. Do not upload .env or students.db.
2. Sign in to Render and choose New > Blueprint.
3. Connect the repository containing render.yaml.
4. Deploy. Render will install requirements and run Gunicorn.
5. Open the HTTPS URL Render assigns to the service.

IMPORTANT LIMITATIONS / SECURITY
- This project uses SQLite. The database file is local to the app and may not persist across
  redeploys or instance replacement on free hosting. For real persistent records, configure
  a managed persistent database such as PostgreSQL before real use.
- /admin and /admin/status are demonstration routes without administrator authentication.
  Do not expose them publicly with real student data until proper authentication and CSRF
  protection have been implemented.
- The course recommendation engine is rule-based, not a trained machine-learning model.
- College/course examples are illustrative. Verify current admission rules and fees with
  the institution before relying on them.
- Set SECRET_KEY in the hosting environment. Never publish secrets or API keys in source code.
- This is an academic demo, not a production-ready admissions platform.

FEATURES IN THIS PACKAGE
- Student registration and login with password hashing
- Student dashboard
- Rule-based course, career and skill recommendations
- Demonstration admin dashboard and application status update
- SQLite database auto-initialization
