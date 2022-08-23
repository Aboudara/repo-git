import time
import path
import LogsPython

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=path.service_obj)
driver.implicitly_wait(5)

name = "Rahul"
driver.get(" https://www.val-doise.gouv.fr/booking/create/11343")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "input#condition.condition").click()
#driver.find_element(By.CSS_SELECTOR, "input#.Bbutton").click()

