# Automated Login & Registration Testing with Selenium & Python

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green)
![Pytest](https://img.shields.io/badge/Pytest-8.x-orange)
![Tests](https://img.shields.io/badge/Tests-6%2F6%20Passed-success)
![Testing](https://img.shields.io/badge/Testing-UI%20Automation-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📌 Project Overview

This project is a **UI Test Automation framework** built with **Python, Selenium WebDriver, and Pytest** to automate and validate login and registration workflows.

The project follows the **Page Object Model (POM)** design pattern to keep test logic clean, reusable, and maintainable.

It includes both **positive and negative test scenarios**, covering successful user registration, authentication, invalid input, incorrect credentials, and required-field validation.

> **Current Test Result: 6/6 tests passed successfully.**

---

## 🎯 Project Objectives

The main objectives of this project are to:

* Automate web application login and registration workflows
* Practice UI test automation using Selenium WebDriver
* Implement automated testing with Pytest
* Apply the Page Object Model design pattern
* Validate positive and negative user scenarios
* Use explicit waits instead of unnecessary hard-coded delays
* Build a clean and maintainable QA automation structure
* Demonstrate practical Software Quality Engineering skills

---

## 🛠️ Tech Stack

| Technology              | Purpose                     |
| ----------------------- | --------------------------- |
| **Python 3.13**         | Programming language        |
| **Selenium WebDriver**  | Browser automation          |
| **Pytest**              | Test framework              |
| **Chrome**              | Test browser                |
| **Page Object Model**   | Test architecture           |
| **HTML/CSS/JavaScript** | Local demo application      |
| **Git/GitHub**          | Version control & portfolio |

---

## 🧪 Testing Scope

The project covers the following functionality:

### Registration Testing

* Successful registration with valid information
* Password confirmation validation
* Invalid email validation
* Required-field validation

### Login Testing

* Successful login with valid credentials
* Login with incorrect password
* Login with empty fields

---

## 📋 Test Cases

| Test ID | Test Scenario                      | Expected Result                | Status |
| ------- | ---------------------------------- | ------------------------------ | ------ |
| REG-001 | Register with valid information    | Registration succeeds          | ✅ PASS |
| REG-002 | Register with mismatched passwords | Validation message displayed   | ✅ PASS |
| REG-003 | Register with invalid email        | Validation message displayed   | ✅ PASS |
| LOG-001 | Login with valid credentials       | Login succeeds                 | ✅ PASS |
| LOG-002 | Login with incorrect password      | Authentication error displayed | ✅ PASS |
| LOG-003 | Login with empty fields            | Required-field error displayed | ✅ PASS |

### Test Execution Result

```text
6 tests collected
6 passed
0 failed
```

**Pass Rate: 100%**

---

## 🏗️ Project Architecture

The project uses the **Page Object Model (POM)** pattern.

```text
selenium_login_registration_project/
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   └── register_page.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_login.py
│   └── test_registration.py
│
├── test_data/
│   └── users.json
│
├── webapp/
│   ├── login.html
│   ├── register.html
│   └── styles.css
│
├── .gitignore
├── PROJECT_PROMPT.md
├── README.md
├── pytest.ini
└── requirements.txt
```

---

## 📂 Project Structure Explained

### `pages/`

Contains reusable Page Object classes.

**`base_page.py`**

Provides common Selenium functionality such as:

* Finding elements
* Clicking elements
* Entering text
* Waiting for elements
* Reading element text

**`login_page.py`**

Contains locators and actions related to the login page.

**`register_page.py`**

Contains locators and actions related to the registration page.

---

### `tests/`

Contains automated test cases.

**`test_login.py`**

Tests login functionality including:

* Successful login
* Wrong password
* Empty login fields

**`test_registration.py`**

Tests registration functionality including:

* Successful registration
* Password mismatch
* Invalid email

**`conftest.py`**

Contains Pytest fixtures responsible for:

* Starting the local web server
* Creating the Selenium WebDriver
* Cleaning up the browser after tests

---

### `test_data/`

Contains sample test data used by the project.

```text
users.json
```

This keeps test information separate from the test implementation.

---

### `webapp/`

Contains the small local demo web application used as the system under test.

It includes:

* Registration page
* Login page
* CSS styling
* Client-side validation
* Browser localStorage for demo authentication

> The application is intentionally simple because the primary purpose of this repository is demonstrating **QA automation**, not full-stack development.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/selenium-login-registration-testing.git
```

Move into the project:

```bash
cd selenium-login-registration-testing
```

---

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv .venv
```

Activate it in **Git Bash**:

```bash
source .venv/Scripts/activate
```

Or in **Command Prompt**:

```cmd
.venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

### 4. Verify Selenium Installation

```bash
python -c "import selenium; print(selenium.__version__)"
```

---

## ▶️ Running the Tests

Run all tests:

```bash
python -m pytest -v
```

Run only login tests:

```bash
python -m pytest tests/test_login.py -v
```

Run only registration tests:

```bash
python -m pytest tests/test_registration.py -v
```

---

## 📊 Expected Test Output

A successful test execution should look similar to:

```text
================ test session starts ================

collected 6 items

tests/test_login.py::test_successful_login PASSED
tests/test_login.py::test_login_wrong_password PASSED
tests/test_login.py::test_login_empty_fields PASSED
tests/test_registration.py::test_successful_registration PASSED
tests/test_registration.py::test_password_mismatch PASSED
tests/test_registration.py::test_invalid_email PASSED

================ 6 passed ================
```

---

## 🔍 Testing Approach

The project demonstrates several important QA concepts.

### Functional Testing

Validates that login and registration features behave according to expected requirements.

### Positive Testing

Examples:

* Valid registration data
* Valid login credentials

### Negative Testing

Examples:

* Invalid email
* Wrong password
* Password mismatch
* Empty login fields

### Regression Testing

The automated suite can be executed repeatedly after application changes to ensure existing functionality continues to work.

### UI Automation

Selenium WebDriver interacts with the browser like a real user by:

* Opening pages
* Entering information
* Clicking buttons
* Reading validation messages
* Verifying expected results

---

## 🧩 Page Object Model

Instead of writing Selenium selectors directly inside every test, the project separates page behavior into Page Object classes.

For example:

```python
login = LoginPage(driver)

login.open(login_url)
login.login("saciid@example.com", "StrongPass123")

assert login.get_message() == "Login successful!"
```

This approach improves:

* Maintainability
* Reusability
* Readability
* Test organization

If a locator changes, it can be updated inside the Page Object rather than across multiple tests.

---

## ⏱️ Explicit Waits

The framework uses Selenium's `WebDriverWait` and expected conditions.

Example:

```python
self.wait.until(
    EC.visibility_of_element_located(locator)
)
```

This is preferred over unnecessary fixed delays such as:

```python
time.sleep(5)
```

Explicit waits make automation more reliable and efficient.

---

## 🔐 Test Data

Example test data:

```json
{
  "valid_user": {
    "name": "Saciid Joof",
    "email": "saciid@example.com",
    "password": "StrongPass123"
  }
}
```

The project uses demo credentials only.

**Do not commit real passwords, API keys, tokens, or production credentials to GitHub.**

---

## 🚀 Future Improvements

The framework can be extended with:

* [ ] Automatic screenshots on test failure
* [ ] HTML test reports
* [ ] Allure reporting
* [ ] GitHub Actions CI/CD
* [ ] Cross-browser testing
* [ ] Firefox and Edge support
* [ ] Data-driven testing
* [ ] API testing with Postman or Python Requests
* [ ] Environment configuration
* [ ] Parallel test execution
* [ ] Test categorization with Pytest markers
* [ ] Integration with a defect tracking system

---

## 📈 Future Automation Architecture

A larger version of this project could evolve into:

```text
                    QA Automation Framework
                              │
             ┌────────────────┼────────────────┐
             │                │                │
         UI Testing       API Testing      Test Data
             │                │                │
         Selenium         Requests         JSON/CSV
             │                │                │
             └────────────────┼────────────────┘
                              │
                           Pytest
                              │
                       Test Reporting
                              │
                    GitHub Actions / CI
```

---

## 💡 Skills Demonstrated

This project demonstrates practical experience with:

* Software Testing
* Quality Assurance
* Test Automation
* Selenium WebDriver
* Python
* Pytest
* Page Object Model
* Functional Testing
* Positive Testing
* Negative Testing
* Regression Testing
* Test Case Design
* Test Data Management
* Explicit Waits
* Web UI Testing
* Git & GitHub

---

## 👨‍💻 Portfolio Value

This project was created as a practical demonstration of **Software Testing and Quality Engineering** concepts.

It demonstrates the ability to move from:

```text
Requirement
     ↓
Test Scenario
     ↓
Test Case
     ↓
Automation
     ↓
Test Execution
     ↓
Validation
     ↓
Test Result
```

---

## 📌 Project Status

**Status:** Completed — Initial Version

**Test Automation:** ✅ Implemented

**Test Cases:** 6

**Passed:** 6

**Failed:** 0

**Pass Rate:** 100%

---

## 📄 License

This project is available under the MIT License.

---

## ⭐ Acknowledgment

Built as a hands-on Software Testing & Quality Engineering project using Python, Selenium WebDriver, and Pytest.
# Automated-Login-Registration-Testing-with-Selenium-Python
