from pages.register_page import RegisterPage


def test_successful_registration(driver, base_url):
    page = RegisterPage(driver)
    page.open(f"{base_url}/register.html")
    page.register(
        "Saciid Joof",
        "saciid@example.com",
        "StrongPass123",
        "StrongPass123",
    )

    assert page.get_message() == "Registration successful!"


def test_password_mismatch(driver, base_url):
    page = RegisterPage(driver)
    page.open(f"{base_url}/register.html")
    page.register(
        "Saciid Joof",
        "saciid@example.com",
        "StrongPass123",
        "DifferentPass123",
    )

    assert page.get_message() == "Passwords do not match."


def test_invalid_email(driver, base_url):
    page = RegisterPage(driver)
    page.open(f"{base_url}/register.html")
    page.register(
        "Saciid Joof",
        "not-an-email",
        "StrongPass123",
        "StrongPass123",
    )

    assert page.get_message() == "Enter a valid email address."
