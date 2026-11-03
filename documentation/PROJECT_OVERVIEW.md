# MCA Project Overview

## Title
AI-Enabled Smart Student Admission and Academic Guidance System

## Problem Statement
Students often need to compare higher-education pathways with their academic
background and career interests. This prototype centralises a student profile
and provides preliminary course and skill suggestions.

## Objectives
- Provide a simple student registration and login workflow.
- Store student academic profile details in SQLite.
- Present a dashboard for the logged-in student.
- Generate explainable course, career and skill suggestions.
- Demonstrate basic application-status management for an administrator.

## Modules
1. Authentication: registration, password hashing and login.
2. Student Profile: academic and personal information display.
3. Recommendation: rule-based suggestions based on percentage, Mathematics
   background and selected interest.
4. Admin Demo: list student applications and update status.
5. Database: SQLite persistence.

## Technology Stack
- Front end: HTML5, CSS3, Bootstrap 5, Jinja2
- Back end: Python, Flask
- Database: SQLite
- Security baseline: Werkzeug password hashing and parameterised SQL queries

## Recommendation Logic
The current prototype maps the selected interest to relevant courses, career
paths and skill suggestions. Percentage bands provide general study guidance.
Mathematics background adds a reminder for quantitative pathways. This is
rule-based decision support, not a trained AI model and not an eligibility check.

## Limitations and Future Scope
- Add role-based administrator authentication and CSRF protection.
- Add email verification and password reset.
- Add application document upload and application tracking.
- Integrate official institution/course data through verified sources.
- Build and evaluate an ML recommender only with an appropriate consented dataset.
- Add automated tests, audit logs and deployment hardening.
