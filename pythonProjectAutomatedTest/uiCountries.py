import time

from selenium import webdriver
#Chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/Gueye/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

#Open Wew page
driver.get(" https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#Click on checkbox
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

#Boucle
for checkboox in checkboxes:
    if checkboox.get_attribute("value") == "option2":
        checkboox.click()
        assert checkboox.is_selected()
        break
#Click on radioButtons
radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

#Clickl button to hide
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()




