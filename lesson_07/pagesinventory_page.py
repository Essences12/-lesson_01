from selenium.webdriver.common.by import By


class InventoryPage:
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        """Добавить товар в корзину по его названию."""
        locator = (By.XPATH,
                   f"//div[text()='{product_name}']"
                   "/ancestor::div[@class='inventory_item']"
                   "//button")
        self.driver.find_element(*locator).click()
        return self

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
        return self