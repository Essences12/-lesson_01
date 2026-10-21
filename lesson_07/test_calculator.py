from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Page Object для страницы калькулятора."""

    URL = ("https://bonigarcia.dev/selenium-webdriver-java/"
           "slow-calculator.html")

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    RESULT = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get(self.URL)
        return self

    def set_delay(self, seconds):
        delay_field = self.driver.find_element(*self.DELAY_INPUT)
        delay_field.clear()
        delay_field.send_keys(str(seconds))
        return self

    def click_button(self, label):
        locator = (By.XPATH, f"//span[text()='{label}']")
        self.driver.find_element(*locator).click()
        return self

    def wait_for_result(self, expected_text):
        self.wait.until(
            EC.text_to_be_present_in_element(self.RESULT, expected_text)
        )
        return self

    def get_result(self):
        return self.driver.find_element(*self.RESULT).text