import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# Change these URLs to your actual registration forms
FORM1_URL = "http://suninjuly.github.io/registration1.html"
FORM2_URL = "http://suninjuly.github.io/registration2.html"

@pytest.fixture()
def browser():
    options = Options()
    # options.add_argument("--headless")  # Uncomment if you want headless mode

    service = Service(ChromeDriverManager().install())
    print("\nStarting browser for test...")
    time.sleep(2)
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    print("\nQuitting browser...")
    time.sleep(2)
    driver.quit()

class TestRegistrationForms:

    def test_registration_form1(self, browser):
        browser.get(FORM1_URL)
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Name")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Surname")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("email@example.com")
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Wait until the <h1> success message is visible
        success_message_element = WebDriverWait(browser, 7).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )
        success_message = success_message_element.text
        assert "Congratulations! You have successfully registered!" in success_message

    def test_registration_form2(self, browser):
        browser.get(FORM2_URL)
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Name")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("email@example.com")
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Wait until the <h1> success message is visible
        success_message_element = WebDriverWait(browser, 7).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )
        success_message = success_message_element.text
        assert "Congratulations! You have successfully registered!" in success_message
