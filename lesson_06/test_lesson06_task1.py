from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Открываем страницу
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        # 2. Находим и нажимаем кнопку Start
        start_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
        )
        start_button.click()

        # 3. Ждём появления текста Hello World!
        hello_text = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )

        # 4. Скриншот страницы
        driver.save_screenshot("dynamic_loading_result.png")

        # 5. Проверяем текст
        assert hello_text.text == "Hello World!"
    finally:
        driver.quit()