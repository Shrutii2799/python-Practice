from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Keep Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

# Wait for page to load
time.sleep(5)

# Select English language
lang = driver.find_element(By.CLASS_NAME, "langSelectButton")
lang.click()

time.sleep(5)

# Find the big cookie
cookie = driver.find_element(By.ID, "bigCookie")

# Click the cookie continuously
while True:
    cookie.click()


