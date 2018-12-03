from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()

driver.get("https://www.baidu.com")

try:
    a = driver.find_element_by_id("kw")
    print()
    print(a.get_attribute())
finally:
    driver.quit()

# ele = WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located(driver.find_element_by_css_selector("")))
# driver.implicitly_wait(10)


