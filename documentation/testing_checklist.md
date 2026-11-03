# Manual Testing Checklist

| Test | Expected result |
|---|---|
| Register with valid details | Student account is created |
| Register same email twice | Duplicate registration is rejected |
| Passwords do not match | Validation message appears |
| Login with valid credentials | Dashboard opens |
| Login with wrong credentials | Error message appears |
| Open dashboard without login | Redirect to login |
| Click Get AI Recommendations | Recommendation form opens |
| Submit valid profile | Courses, careers and skills appear |
| Submit percentage below 0 or above 100 | Validation message appears |
| Logout | Session is cleared |
| Update status in Admin Demo | Status is updated in database |

For a formal MCA submission, add screenshots of actual test execution and
record the browser, operating system and test date.
