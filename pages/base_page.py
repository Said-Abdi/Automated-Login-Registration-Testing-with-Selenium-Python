from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def type(self, locator, value):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(value)

    def click(self, locator):
        self.find_clickable(locator).click()

    def text_of(self, locator):
        return self.find_visible(locator).text
