# Master Prompt — Automated Login & Registration Testing

Use this prompt with ChatGPT whenever you want to rebuild or extend this portfolio project.

## Prompt

You are a Software QA Automation Engineer.

Build a beginner-friendly but professional portfolio project named:

**Automated Login & Registration Testing with Selenium & Python**

### Goal
Create automated UI tests for a small login and registration web application.

### Tech Stack
- Python
- Selenium WebDriver
- Pytest
- Chrome
- Page Object Model (POM)
- HTML/CSS/JavaScript demo application

### Requirements

1. Create a small local web application with:
   - Registration page
   - Login page
   - Name, email, password and confirm-password fields
   - Client-side validations
   - Browser localStorage for a demo user

2. Create automated tests for:
   - Successful registration
   - Password mismatch
   - Invalid email
   - Successful login
   - Wrong password
   - Empty login fields

3. Use Page Object Model:
   - BasePage
   - RegisterPage
   - LoginPage

4. Use explicit waits with Selenium WebDriverWait.
   Avoid unnecessary time.sleep() calls.

5. Use pytest fixtures for:
   - Chrome WebDriver setup/teardown
   - Local HTTP server

6. Keep the project structure simple and suitable for GitHub.

7. Include:
   - requirements.txt
   - pytest.ini
   - .gitignore
   - README.md
   - test data example
   - clear run instructions

8. Tests must be independent and readable.

9. Explain each major file briefly.

10. Add ideas for future improvements such as:
   - screenshots on failure
   - HTML reports
   - GitHub Actions CI
   - cross-browser testing
   - data-driven testing
   - API testing

Return complete file contents and commands needed to run the project.
