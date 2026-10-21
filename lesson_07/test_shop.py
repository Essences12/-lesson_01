from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_shop_checkout_total():
    driver = webdriver.Firefox()
    try:
        LoginPage(driver).open().login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_to_cart("Sauce Labs Backpack")
        inventory.add_to_cart("Sauce Labs Bolt T-Shirt")
        inventory.add_to_cart("Sauce Labs Onesie")
        inventory.go_to_cart()

        CartPage(driver).checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_form("Иван", "Иванов", "123456")

        total = checkout.get_total()
        assert total == "Total: $58.29"
    finally:
        driver.quit()
        