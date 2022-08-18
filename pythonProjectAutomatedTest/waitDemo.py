import time
import path
import LogsPython

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=path.service_obj)
driver.implicitly_wait(5)

name = "Rahul"
driver.get(" https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
if count > 0:
    LogsPython.log.info("test passe")
    for result in results:
        result.find_element(By.XPATH, "div/button").click()
else:
    LogsPython.log.error("test failed")

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

