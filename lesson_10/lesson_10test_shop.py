"""Тесты для интернет-магазина с разметкой Allure."""

import allure
from selenium import webdriver

from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Оформление заказа: проверка итоговой стоимости")
@allure.description(
    "Авторизуется как standard_user, добавляет три товара, "
    "переходит в корзину, оформляет заказ и проверяет итоговую сумму."
)
def test_shop_checkout_total():
    """Проверка оформления заказа и итоговой стоимости."""
    driver = webdriver.Firefox()
    try:
        with allure.step("Открыть сайт и авторизоваться"):
            LoginPage(driver).open().login(
                "standard_user", "secret_sauce"
            )

        inventory = InventoryPage(driver)

        with allure.step("Добавить Sauce Labs Backpack в корзину"):
            inventory.add_to_cart("Sauce Labs Backpack")

        with allure.step("Добавить Sauce Labs Bolt T-Shirt в корзину"):
            inventory.add_to_cart("Sauce Labs Bolt T-Shirt")

        with allure.step("Добавить Sauce Labs Onesie в корзину"):
            inventory.add_to_cart("Sauce Labs Onesie")

        with allure.step("Перейти в корзину"):
            inventory.go_to_cart()

        with allure.step("Нажать Checkout"):
            CartPage(driver).checkout()

        with allure.step("Заполнить форму оформления"):
            CheckoutPage(driver).fill_form("Иван", "Иванов", "123456")

        checkout = CheckoutPage(driver)

        with allure.step("Прочитать итоговую стоимость"):
            total = checkout.get_total()

        with allure.step("Проверить, что итоговая сумма равна $58.29"):
            assert total == "Total: $58.29"
    finally:
        driver.quit()