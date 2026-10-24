"""Page Object для страницы корзины."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Класс для работы с корзиной."""

    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#checkout")

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы.

        :param driver: экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def checkout(self) -> "CartPage":
        """Нажать кнопку Checkout.

        :return: текущий экземпляр страницы
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()
        return self