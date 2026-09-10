from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option= webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_option)
driver.get("https://www.python.org/")

#
# price_dollar=driver.find_element(By.CLASS_NAME,value="a-price-whole")
# print(price_dollar.text)

# search_bar = driver.find_element(By.NAME,value="q")
# print(search_bar.tag_name)
#
# button=driver.find_element(By.NAME,value="submit")
# print(button.size)
#
# documentation_link=driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")
# print(documentation_link.text)
#
# bug_link=driver.find_element(By.XPATH,value='//*[@id="content"]/div/section/div[1]/div[4]/p[2]/a')
# print(bug_link.text)

# Finding multiple elements
tier_1 = driver. find_elements(By.CLASS_NAME, value="tier-1")

# Challenge: Print the event dates from python.org
event_times = driver. find_elements(By. CSS_SELECTOR, value=".event-widget time")
event_names = driver. find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print (events)

# driver.close()
driver.quit()
# driver.quit()
# driver.close()

