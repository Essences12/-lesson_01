"""Page Object для страницы авторизации SauceDemo."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Класс для авторизации на сайте магазина."""

    URL = "https://www.saucedemo.com/"

    USERNAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы.

        :param driver: экземпляр WebDriver
        """
        self.driver = driver

    def open(self) -> "LoginPage":
        """Открыть страницу авторизации.

        :return: текущий экземпляр страницы
        """
        self.driver.get(self.URL)
        return self

    def login(self, username: str, password: str) -> "LoginPage":
        """Выполнить вход с указанными учётными данными.

        :param username: имя пользователя
        :param password: пароль
        :return: текущий экземпляр страницы
        """
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self