from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
URL = "https://tinder.com"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(URL)
wait = WebDriverWait(driver, 2)

pass_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Nope"]')))
pass_btn.click()
