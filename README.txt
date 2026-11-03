AI-ENABLED SMART STUDENT ADMISSION AND ACADEMIC GUIDANCE SYSTEM
MCA Academic Project Prototype

FEATURES
1. Student registration and login with hashed passwords.
2. Student dashboard and academic profile.
3. Personalised course, career-path and skill suggestions.
4. Admin demo dashboard for viewing applications and updating status.
5. SQLite database created automatically.

REQUIREMENTS
- Python 3.10 or later
- Internet connection for Bootstrap CDN styling (optional; pages still work without styling)
- VS Code or another Python editor

RUN ON WINDOWS
1. Extract this ZIP.
2. Open the AI_Student_Guidance folder in VS Code.
3. Open Terminal in VS Code.
4. Run: python -m venv venv
5. Run: .\venv\Scripts\activate
6. Run: python -m pip install -r requirements.txt
7. Run: python app.py
8. Open http://127.0.0.1:5000/

RECOMMENDATION MODULE
Click Dashboard > Get AI Recommendations. Enter graduation percentage,
Mathematics background and interest area. The system displays course ideas,
possible career paths and skill-building suggestions.

IMPORTANT ACADEMIC NOTE
The recommendation module currently uses transparent rule-based logic. It is
not a trained machine-learning model. For an actual AI/ML extension, collect a
lawfully obtained, consented and anonymised dataset, define evaluation metrics,
train and test a model, and document its limitations. Do not claim this prototype
uses trained AI.

SECURITY / DEPLOYMENT
This is an academic local prototype. The Admin Demo route is not protected by
admin authentication and must not be exposed publicly. Before deployment add
admin roles, CSRF protection, secure environment-based secret key, HTTPS,
input validation, rate limiting, logging, backups and production server settings.
Never use debug=True in production.

TESTING CHECKLIST
- Register a new student.
- Try registering the same email again.
- Log in with correct and incorrect passwords.
- Open Dashboard.
- Click Get AI Recommendations and submit each interest option.
- Check invalid percentages (negative and above 100).
- Log out and verify protected pages redirect to login.
- Open Admin Demo locally and update a sample status.

DATABASE
SQLite file: students.db (created automatically in the project folder).
Do not delete it if you want to preserve registered student records.

Deployment files added:
- Procfile and render.yaml for Render deployment
- README_DEPLOYMENT_HINDI.md for setup instructions
- .env.example for local secret configuration

See README_DEPLOYMENT_HINDI.md for deployment steps and important limitations.
