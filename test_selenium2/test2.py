from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

# Function to calculate the answer
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Initialize the browser
browser = webdriver.Chrome()

try:
    # Open the webpage
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # Click the button
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # Handle the alert
    alert = browser.switch_to.alert
    alert.accept()

    # Wait for the next page to load
    time.sleep(1)

    # Solve the CAPTCHA
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text  # Extract x value
    answer = calc(x)

    # Input the answer
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(answer)

    # Submit the form
    submit_button = browser.find_element(By.TAG_NAME, "button")
    submit_button.click()

    # Wait to see the result
    time.sleep(5)

finally:
    # Close the browser
    browser.quit()
