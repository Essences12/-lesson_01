from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import platform


def test_form():
    if platform.system() == "Windows":
        driver = webdriver.Edge()
    else:  # macOS
        driver = webdriver.Safari()

    wait = WebDriverWait(driver, 10)

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

        fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            # zip-code оставляем пустым
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro",
        }

        for name, value in fields.items():
            element = wait.until(
                EC.presence_of_element_located((By.NAME, name))
            )
            element.clear()
            element.send_keys(value)

        submit = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[type='submit']")
            )
        )
        submit.click()

        # Zip code должен быть красным (danger)
        zip_field = wait.until(
            EC.presence_of_element_located((By.ID, "zip-code"))
        )
        zip_class = zip_field.get_attribute("class")
        assert "alert-danger" in zip_class, (
            f"Zip code не подсвечен красным: {zip_class}"
        )

        # Остальные поля должны быть зелёными (success)
        success_ids = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company",
        ]

        for field_id in success_ids:
            element = wait.until(
                EC.presence_of_element_located((By.ID, field_id))
            )
            element_class = element.get_attribute("class")
            assert "alert-success" in element_class, (
                f"Поле {field_id} не подсвечено зелёным: {element_class}"
            )

    finally:
        driver.quit()