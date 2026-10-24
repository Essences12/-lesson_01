"""Тесты для калькулятора с разметкой Allure."""

import allure
from selenium import webdriver

from calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка медленного калькулятора: 7 + 8 = 15")
@allure.description(
    "Открывает страницу калькулятора, устанавливает задержку 45 секунд, "
    "выполняет сложение 7 + 8 и проверяет результат."
)
def test_slow_calculator():
    """Проверка работы калькулятора с задержкой."""
    driver = webdriver.Chrome()
    try:
        page = CalculatorPage(driver)

        with allure.step("Открыть страницу калькулятора"):
            page.open()

        with allure.step("Установить задержку 45 секунд"):
            page.set_delay(45)

        with allure.step("Нажать кнопки: 7, +, 8, ="):
            page.click_button("7")
            page.click_button("+")
            page.click_button("8")
            page.click_button("=")

        with allure.step("Дождаться результата 15"):
            page.wait_for_result("15")

        with allure.step("Проверить, что результат равен 15"):
            assert page.get_result() == "15"
    finally:
        driver.quit()