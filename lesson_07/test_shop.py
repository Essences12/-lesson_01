from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop_checkout_total():
    driver = webdriver.Firefox()
    try:
        login = LoginPage(driver).open()
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_to_cart("Sauce Labs Backpack")
        inventory.add_to_cart("Sauce Labs Bolt T-Shirt")
        inventory.add_to_cart("Sauce Labs Onesie")
        inventory.go_to_cart()

        cart = CartPage(driver)
        cart.checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_form("Иван", "Иванов", "123456")

        total = checkout.get_total()
        assert total == "Total: $58.29"
    finally:
        driver.quit()