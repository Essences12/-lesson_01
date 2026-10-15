from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # Cookie пользователя 1 (получить заранее из реального аккаунта)
    user1_cookies = [
        {"name": "sessionid", "value": "USER1_SESSION_VALUE", "domain": ".gitflic.ru"},
        # ... остальные нужные cookie
    ]

    # Cookie пользователя 2 (получить заранее из реального аккаунта)
    user2_cookies = [
        {"name": "sessionid", "value": "USER2_SESSION_VALUE", "domain": ".gitflic.ru"},
        # ... остальные нужные cookie
    ]

    try:
        # 1. Открываем главную страницу
        driver.get("https://gitflic.ru/")

        # 2. Устанавливаем cookie пользователя 1
        for cookie in user1_cookies:
            driver.add_cookie(cookie)

        # 3. Обновляем страницу
        driver.refresh()

        # 4. Переходим на страницу пользователя 1
        driver.get("https://gitflic.ru/user/USER1_LOGIN")
        wait.until(lambda d: d.current_url != "https://gitflic.ru/")
        user1_url = driver.current_url

        # 5. Разлогиниваемся — очищаем cookie
        driver.delete_all_cookies()

        # 6. Устанавливаем cookie пользователя 2
        driver.get("https://gitflic.ru/")
        for cookie in user2_cookies:
            driver.add_cookie(cookie)

        # 7. Обновляем страницу
        driver.refresh()

        # 8. Переходим на страницу пользователя 2
        driver.get("https://gitflic.ru/user/USER2_LOGIN")
        wait.until(lambda d: d.current_url != "https://gitflic.ru/")
        user2_url = driver.current_url

        # 9. Проверяем, что URL различаются
        assert user1_url != user2_url
    finally:
        driver.quit()