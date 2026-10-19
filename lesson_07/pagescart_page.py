from selenium.webdriver.common.by import By


class CartPage:
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#checkout")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")

    def __init__(self, driver):
        self.driver = driver

    def get_item_names(self):
        names = self.driver.find_elements(
            By.CSS_SELECTOR, ".inventory_item_name"
        )
        return [item.text for item in names]

    def checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
        return self