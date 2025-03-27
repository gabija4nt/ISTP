from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

browser=None
link="http://suninjuly.github.io/simple_form_find_task.html"

chromedriver_path = "/usr/local/bin/chromedriver"
service = Service(chromedriver_path)

options = webdriver.ChromeOptions()
browser = webdriver.Chrome()

try:
    browser.get(link)

    # Find and fill the form fields
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Gabija")

    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Antanaviciute")

    input3 = browser.find_element(By.NAME, "firstname")
    input3.send_keys("Vilnius")

    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Lithuania")

    # Click the submit button (if available)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    

finally:
    if browser is not None:
        time.sleep(5)
        browser.quit()
