from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

# Function to calculate the answer
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Initialize the browser
browser = webdriver.Chrome()

try:
    # Open the webpage
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Wait until price is 100$
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Click the button
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Solve the CAPTCHA
    x = browser.find_element(By.ID, "input_value").text
    answer = calc(x)

    # Input the answer
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(answer)

    # Submit the form
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    # Wait to see the result
    time.sleep(5)

finally:
    # Close the browser, after seeing the result
    time.sleep(5)
    browser.quit()