from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 50)

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

        delay_input = wait.until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys("45")

        for button_text in ["7", "+", "8", "="]:
            button = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//span[text()='{button_text}']")
                )
            )
            button.click()

        result = wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )
        assert result, "Результат 15 не отобразился за 45 секунд"

        screen = driver.find_element(By.CSS_SELECTOR, ".screen")
        assert screen.text == "15"

    finally:
        driver.quit()