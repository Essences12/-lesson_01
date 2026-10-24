"""Page Object для страницы медленного калькулятора."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """Класс для взаимодействия со страницей калькулятора."""

    URL = ("https://bonigarcia.dev/selenium-webdriver-java/"
           "slow-calculator.html")

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    RESULT = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы.

        :param driver: экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self) -> "CalculatorPage":
        """Открыть страницу калькулятора.

        :return: текущий экземпляр страницы
        """
        self.driver.get(self.URL)
        return self

    def set_delay(self, seconds: int) -> "CalculatorPage":
        """Установить задержку вычисления.

        :param seconds: задержка в секундах
        :return: текущий экземпляр страницы
        """
        delay_field = self.driver.find_element(*self.DELAY_INPUT)
        delay_field.clear()
        delay_field.send_keys(str(seconds))
        return self

    def click_button(self, label: str) -> "CalculatorPage":
        """Нажать кнопку калькулятора по тексту.

        :param label: текст кнопки (например, "7", "+", "=")
        :return: текущий экземпляр страницы
        """
        locator = (By.XPATH, f"//span[text()='{label}']")
        self.driver.find_element(*locator).click()
        return self

    def wait_for_result(self, expected_text: str) -> "CalculatorPage":
        """Дождаться появления ожидаемого результата.

        :param expected_text: ожидаемый текст результата
        :return: текущий экземпляр страницы
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.RESULT, expected_text)
        )
        return self

    def get_result(self) -> str:
        """Получить текст результата.

        :return: текст результата
        """
        return self.driver.find_element(*self.RESULT).text