from selenium import webdriver

#Chrome driver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Users/Gueye/Documents/chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.udemy.com/")
driver.maximize_window()
message = driver.title
print(message)

#driver.close()