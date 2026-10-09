from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    # Открываем главную страницу
    driver.get("https://httpbin.qa-territory.online")
    initial_url = driver.current_url

    # Кликаем на ссылку "HTML Form"
    driver.find_element(By.LINK_TEXT, "HTML Form").click()

    # Проверяем, что URL изменился на /forms/post
    assert "/forms/post" in driver.current_url

    # Возвращаемся назад
    driver.back()

    # Проверяем, что вернулись на исходный URL
    assert driver.current_url == initial_url

    driver.quit()