import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):

    def fill_form_and_submit(self, browser, link):
        browser.get(link)

        # Fill required fields
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Name")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Surname")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("email@example.com")
        time.sleep(3)
        # Submit the form
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Wait for the result page to load

        # Get success text
        success_text = browser.find_element(By.TAG_NAME, "h1").text
        return success_text

    def test_registration1(self):
        browser = webdriver.Chrome()
        
        try:
            text = self.fill_form_and_submit(browser, "http://suninjuly.github.io/registration1.html")
            self.assertEqual(text, "Congratulations! You have successfully registered!", "Should pass on registration1")
        finally:
            time.sleep(3)
            browser.quit()

    def test_registration2(self):
        browser = webdriver.Chrome()
        try:
            text = self.fill_form_and_submit(browser, "http://suninjuly.github.io/registration2.html")
            time.sleep(2)
            self.assertEqual(text, "Congratulations! You have successfully registered!", "Should fail on registration2")
        finally:
            time.sleep(3)
            browser.quit()

if __name__ == "__main__":
    unittest.main()
