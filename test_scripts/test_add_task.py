from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.duckduckgo.com/")
time.sleep(3)

# test case_001
search_item = "buy book"
search_box = driver.find_element(By.XPATH, "//input[@id='searchbox_input']")

search_box.send_keys(search_item)
search_box.send_keys(Keys.RETURN)
time.sleep(3)
results = driver.find_elements(By.CSS_SELECTOR, "a.result__a")
assert len(results) > 0, "No search results found!"
print("Test Passed: Search results are displayed")

#test case_002
driver.back()
driver.refresh()
time.sleep(3)
search_box = driver.find_element(By.XPATH, "//input[@id='searchbox_input']")
search_box.click() 
search_box.clear()
time.sleep(3)
search_item = "fiction book"

search_box.send_keys(search_item)
search_box.send_keys(Keys.RETURN)
time.sleep(3)

results = driver.find_elements(By.CSS_SELECTOR, "a.result__a")
assert len(results) > 0, "No search results found!"
print("Test Passed: Search results are displayed")

#test_case_003

driver.back()
driver.refresh()
time.sleep(3)
search_box = driver.find_element(By.XPATH, "//input[@id='searchbox_input']")
search_box.click() 
search_box.clear() 

time.sleep(3)
search_item = "asdfsdf12345nsdkj6"
search_box.send_keys(search_item)
search_box.send_keys(Keys.RETURN)

time.sleep(3)
results = driver.find_elements(By.CSS_SELECTOR, "a.result__a")
assert len(results) == 0, "Some search results found when none expected!"
print("Test Passed: Search results are displayed")

#test_case_004

driver.back()
driver.refresh()
time.sleep(3)
search_box = driver.find_element(By.XPATH, "//input[@id='searchbox_input']")
search_box.click()  
search_box.clear()   

time.sleep(3)
search_item = "@#$%^&* "
search_box.send_keys(search_item)
search_box.send_keys(Keys.RETURN)
time.sleep(3)

results = driver.find_elements(By.CSS_SELECTOR, "a.result__a")
assert len(results) == 0, "Some search results found when none expected!"
print("Test Passed: Search results are displayed")
driver.quit()
