# Database Schema

## students
| Column | Type | Purpose |
|---|---|---|
| id | INTEGER PRIMARY KEY | Unique student identifier |
| name | TEXT | Student name |
| email | TEXT UNIQUE | Login email |
| phone | TEXT | Contact number |
| dob | TEXT | Date of birth |
| category | TEXT | Category supplied by student |
| mathematics | TEXT | Mathematics background |
| twelfth | TEXT | Class 12 percentage |
| graduation_course | TEXT | Graduation course |
| graduation_percentage | TEXT | Graduation percentage |
| post_graduation_course | TEXT | Postgraduate course, if any |
| post_graduation_percentage | TEXT | Postgraduate percentage |
| entrance_score | TEXT | Entrance score, if supplied |
| password | TEXT | Werkzeug password hash |
| application_status | TEXT | Pending / Approved / Rejected |

The application creates the table automatically on first run.
