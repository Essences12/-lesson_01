"""Page Object для главной страницы магазина."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    """Класс для работы с каталогом товаров."""

    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы.

        :param driver: экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, product_name: str) -> "InventoryPage":
        """Добавить товар в корзину по названию.

        :param product_name: название товара
        :return: текущий экземпляр страницы
        """
        locator = (
            By.XPATH,
            f"//div[text()='{product_name}']"
            "/ancestor::div[@class='inventory_item']//button"
        )
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        return self

    def go_to_cart(self) -> "InventoryPage":
        """Перейти в корзину.

        :return: текущий экземпляр страницы
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()
        return self