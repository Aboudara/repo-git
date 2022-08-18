import time

from selenium import webdriver
import path
#Chrome driver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=path.service_obj)

name = "Rahul"
driver.get(" https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, '#name').send_keys(name)
driver.find_element(By.ID, 'alertbtn').click()

alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
alert.accept() 