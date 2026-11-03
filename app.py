from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os
from pathlib import Path
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-change-this-secret")
DATABASE = Path(__file__).resolve().parent / "students.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_database():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                dob TEXT,
                category TEXT,
                mathematics TEXT,
                twelfth TEXT,
                graduation_course TEXT,
                graduation_percentage TEXT,
                post_graduation_course TEXT,
                post_graduation_percentage TEXT,
                entrance_score TEXT,
                password TEXT NOT NULL,
                application_status TEXT DEFAULT 'Pending'
            )
        """)
        columns = {
            row["name"]
            for row in conn.execute("PRAGMA table_info(students)").fetchall()
        }
        if "application_status" not in columns:
            conn.execute(
                "ALTER TABLE students ADD COLUMN application_status TEXT DEFAULT 'Pending'"
            )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = (request.form.get("name") or "").strip()
        email = (request.form.get("email") or "").strip().lower()
        password = request.form.get("password") or ""
        confirm = request.form.get("confirm_password") or ""

        if not name or not email or not password:
            flash("Please fill in all required fields.", "danger")
            return render_template("register.html")
        if password != confirm:
            flash("Passwords do not match.", "danger")
            return render_template("register.html")
        if len(password) < 8:
            flash("Password must contain at least 8 characters.", "danger")
            return render_template("register.html")

        graduation_status = request.form.get("graduation_status", "Completed")
        graduation_percentage = (
            "Pursuing" if graduation_status == "Pursuing"
            else (request.form.get("graduation_percentage") or "")
        )
        values = (
            name, email, request.form.get("phone"), request.form.get("dob"),
            request.form.get("category"), request.form.get("mathematics"),
            request.form.get("twelfth"), request.form.get("graduation_course"),
            graduation_percentage,
            request.form.get("post_graduation_course"),
            request.form.get("post_graduation_percentage"),
            request.form.get("entrance_score"),
            generate_password_hash(password)
        )
        try:
            with get_connection() as conn:
                conn.execute("""
                    INSERT INTO students (
                        name, email, phone, dob, category, mathematics, twelfth,
                        graduation_course, graduation_percentage,
                        post_graduation_course, post_graduation_percentage,
                        entrance_score, password
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, values)
        except sqlite3.IntegrityError:
            flash("This email is already registered. Please log in.", "danger")
            return render_template("register.html")

        flash("Registration successful. Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = (request.form.get("email") or "").strip().lower()
        password = request.form.get("password") or ""
        with get_connection() as conn:
            student = conn.execute(
                "SELECT * FROM students WHERE email = ?", (email,)
            ).fetchone()

        if student and check_password_hash(student["password"], password):
            session.clear()
            session["student_id"] = student["id"]
            return redirect(url_for("dashboard"))

        flash("Invalid email or password.", "danger")
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    student_id = session.get("student_id")
    if not student_id:
        return redirect(url_for("login"))

    with get_connection() as conn:
        student = conn.execute(
            "SELECT * FROM students WHERE id = ?", (student_id,)
        ).fetchone()

    if student is None:
        session.clear()
        return redirect(url_for("login"))
    return render_template("dashboard.html", student=student)


@app.route("/recommendation", methods=["GET", "POST"])
def recommendation():
    if "student_id" not in session:
        flash("Please log in to access academic recommendations.", "warning")
        return redirect(url_for("login"))

    recommendations = []
    career_paths = []
    skill_suggestions = []
    profile = None

    course_catalog = {
        "Computer Science": {
            "courses": [
                "Master of Computer Applications (MCA)",
                "M.Sc. Computer Science",
                "M.Sc. Information Technology",
                "PG Diploma in Full Stack Development",
                "PG Diploma in Cyber Security"
            ],
            "careers": ["Software Developer", "Web Developer", "System Analyst"],
            "skills": ["Python or Java", "SQL and database design", "Data Structures", "Web development"]
        },
        "Data Science": {
            "courses": [
                "M.Sc. Data Science",
                "PG Diploma in Data Analytics",
                "Business Analytics",
                "Big Data Analytics",
                "Data Engineering"
            ],
            "careers": ["Data Analyst", "Business Intelligence Analyst", "Junior Data Engineer"],
            "skills": ["Python", "Statistics", "SQL", "Data visualisation"]
        },
        "Artificial Intelligence": {
            "courses": [
                "M.Sc. Artificial Intelligence",
                "PG Diploma in Artificial Intelligence",
                "Machine Learning",
                "Deep Learning",
                "Natural Language Processing"
            ],
            "careers": ["AI/ML Associate", "Junior ML Engineer", "AI Application Developer"],
            "skills": ["Python", "Linear algebra basics", "Machine learning fundamentals", "Model evaluation"]
        },
        "Business": {
            "courses": [
                "MBA",
                "M.Com",
                "Business Analytics",
                "Financial Management",
                "Human Resource Management"
            ],
            "careers": ["Business Analyst", "Operations Executive", "Marketing Associate"],
            "skills": ["Excel", "Business communication", "Presentation skills", "Basic analytics"]
        },
        "Research": {
            "courses": [
                "M.Sc. Research Programs",
                "Research Methodology",
                "PG Diploma in Research",
                "Computational Research",
                "Technology Research Programs"
            ],
            "careers": ["Research Assistant", "Project Associate", "Academic Researcher"],
            "skills": ["Research methodology", "Technical writing", "Data interpretation", "Referencing tools"]
        }
    }

    if request.method == "POST":
        graduation_status = request.form.get("graduation_status", "Completed")
        try:
            percentage = float(request.form.get("graduation_percentage", "")) if graduation_status == "Completed" else None
        except (TypeError, ValueError):
            percentage = -1

        interest = request.form.get("interest", "")
        mathematics = request.form.get("mathematics", "")

        if graduation_status not in ("Completed", "Pursuing") or (graduation_status == "Completed" and not 0 <= percentage <= 100):
            flash("Enter a valid graduation percentage, or select Pursuing.", "danger")
        elif interest not in course_catalog:
            flash("Please select a valid area of interest.", "danger")
        elif mathematics not in ("Yes", "No"):
            flash("Please select your Mathematics background.", "danger")
        else:
            selected = course_catalog[interest]
            recommendations = selected["courses"][:]
            career_paths = selected["careers"][:]
            skill_suggestions = selected["skills"][:]

            if graduation_status == "Pursuing":
                profile = "Graduation currently pursuing"
                extra_tip = "Complete your graduation and check each programme's eligibility requirements."
            elif percentage >= 75:
                profile = "Strong academic profile"
                extra_tip = "Explore advanced electives, internships and project-based learning."
            elif percentage >= 60:
                profile = "Good academic foundation"
                extra_tip = "Strengthen core subjects and build a portfolio with practical projects."
            elif percentage >= 45:
                profile = "Developing academic profile"
                extra_tip = "Focus on fundamentals, consistent practice and skill-based certifications."
            else:
                profile = "Foundation-building profile"
                extra_tip = "Review subject fundamentals and check each institution's current eligibility rules."

            if mathematics == "No" and interest in ("Data Science", "Artificial Intelligence"):
                skill_suggestions.insert(0, "Revise basic algebra, statistics and logical reasoning")
                extra_tip += " Some programmes may require Mathematics; verify eligibility with the institution."

            skill_suggestions.append(extra_tip)

    return render_template(
        "recommendation.html",
        recommendations=recommendations,
        career_paths=career_paths,
        skill_suggestions=skill_suggestions,
        profile=profile
    )

@app.route("/admin")
def admin_dashboard():
    # Demo-only page. Add proper admin authentication before public deployment.
    with get_connection() as conn:
        students = conn.execute("""
            SELECT id, name, email, graduation_course,
                   graduation_percentage, application_status
            FROM students ORDER BY id DESC
        """).fetchall()
        total_students = conn.execute(
            "SELECT COUNT(*) FROM students"
        ).fetchone()[0]

    return render_template(
        "admin.html", students=students, total_students=total_students
    )


@app.route("/admin/status/<int:student_id>", methods=["POST"])
def update_application_status(student_id):
    # Demo-only endpoint. Protect with admin login and CSRF before deployment.
    status = request.form.get("status")
    if status not in ("Pending", "Approved", "Rejected"):
        flash("Invalid application status.", "danger")
        return redirect(url_for("admin_dashboard"))

    with get_connection() as conn:
        cursor = conn.execute(
            "UPDATE students SET application_status = ? WHERE id = ?",
            (status, student_id)
        )
        if cursor.rowcount == 0:
            flash("Student record not found.", "danger")
        else:
            flash("Application status updated.", "success")

    return redirect(url_for("admin_dashboard"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


create_database()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
