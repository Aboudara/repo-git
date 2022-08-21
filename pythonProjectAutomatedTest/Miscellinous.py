import time
import path
import LogsPython
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=path.service_obj, options=chrome_options)
driver.implicitly_wait(5)

driver.get(" https://rahulshettyacademy.com/AutomationPractice")
driver.maximize_window()

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")


time.sleep(3)
driver.close()