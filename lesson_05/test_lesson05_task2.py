from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    initial_url = driver.current_url

    # Находим поле custname и вводим имя
    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Ivan")

    # Находим кнопку Submit и кликаем
    submit_button = driver.find_element(
        By.XPATH, "//button[text()='Submit']"
    )
    submit_button.click()

    # Проверяем, что URL изменился
    assert driver.current_url != initial_url

    driver.quit()