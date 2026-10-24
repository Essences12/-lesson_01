"""Page Object для страницы оформления заказа."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """Класс для оформления заказа."""

    FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#continue")
    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы.

        :param driver: экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_name: str, last_name: str,
                  postal_code: str) -> "CheckoutPage":
        """Заполнить форму оформления заказа.

        :param first_name: имя
        :param last_name: фамилия
        :param postal_code: почтовый индекс
        :return: текущий экземпляр страницы
        """
        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        ).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        return self

    def get_total(self) -> str:
        """Получить итоговую стоимость.

        :return: текст с итоговой стоимостью
        """
        element = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_LABEL)
        )
        return element.text