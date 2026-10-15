from selenium import webdriver
from pages.calculator_page import CalculatorPage


def test_slow_calculator():
    driver = webdriver.Chrome()
    try:
        page = CalculatorPage(driver).open()
        page.set_delay(45)
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

        result = page.get_result()
        assert result == "15"
    finally:
        driver.quit()