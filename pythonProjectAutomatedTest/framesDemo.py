import time
import path
import LogsPython
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=path.service_obj)
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
time.sleep(1)
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automated frames")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)


time.sleep(4)
driver.close()