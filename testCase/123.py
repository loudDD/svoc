
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.common.by import By
driver  = webdriver.Chrome()

driver.get("https://pre.svocloud.com")
a = driver.get_cookies()
print(a)
driver.find_element_by_css_selector("[formcontrolname='username']").send_keys(18600929870)
driver.find_element_by_css_selector("[formcontrolname='password']").send_keys(123456)
driver.find_element_by_css_selector("button").click()
#提交操作；submit可以提交内容，来达到clike的作用
#driver.find_element_by_css_selector("a[herf='#/page/meeting/conference-management']").submit()
sleep(5)
a = driver.find_element_by_css_selector("a > span").text
print(a)
