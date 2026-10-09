from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://www.saucedemo.com/")

        wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Добавляем товары в корзину
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie",
        ]

        for item_name in items_to_add:
            button = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        f"//div[text()='{item_name}']"
                        "/ancestor::div[@class='inventory_item']"
                        "//button",
                    )
                )
            )
            button.click()

        # Переходим в корзину
        cart = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".shopping_cart_link")
            )
        )
        cart.click()

        # Checkout
        checkout = wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout.click()

        # Заполняем форму
        wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        ).send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        driver.find_element(By.ID, "continue").click()

        # Читаем итоговую стоимость
        total_element = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".summary_total_label")
            )
        )
        total_text = total_element.text
        total_value = total_text.replace("Total: ", "").strip()

        assert total_value == "$58.29", (
            f"Ожидалось $58.29, получено {total_value}"
        )

    finally:
        driver.quit()