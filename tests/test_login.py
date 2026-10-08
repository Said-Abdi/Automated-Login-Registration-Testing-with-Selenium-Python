from pages.register_page import RegisterPage
from pages.login_page import LoginPage


def create_user(driver, base_url):
    register = RegisterPage(driver)
    register.open(f"{base_url}/register.html")
    driver.execute_script("localStorage.clear();")
    register.register(
        "Saciid Joof",
        "saciid@example.com",
        "StrongPass123",
        "StrongPass123",
    )
    assert register.get_message() == "Registration successful!"


def test_successful_login(driver, base_url):
    create_user(driver, base_url)

    login = LoginPage(driver)
    login.open(f"{base_url}/login.html")
    login.login("saciid@example.com", "StrongPass123")

    assert login.get_message() == "Login successful!"


def test_login_wrong_password(driver, base_url):
    create_user(driver, base_url)

    login = LoginPage(driver)
    login.open(f"{base_url}/login.html")
    login.login("saciid@example.com", "WrongPassword")

    assert login.get_message() == "Invalid email or password."


def test_login_empty_fields(driver, base_url):
    login = LoginPage(driver)
    login.open(f"{base_url}/login.html")
    login.click(login.LOGIN_BUTTON)

    assert login.get_message() == "Email and password are required."
