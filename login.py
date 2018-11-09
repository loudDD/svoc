from selenium import webdriver

<<<<<<< HEAD
driver = webdriver.Chrome()
=======
driver = webdriver.Firefox()
>>>>>>> 18e09ec6ee5064675d078c4efa307a9bd20baf60

driver.get("https://vip.svocloud.com")

driver.find_element_by_xpath("//input[@formcontrolname='username']").send_keys("18600000000")

driver.find_element_by_xpath("//input[@placeholder='密 码']").send_keys(123456)
driver.find_element_by_xpath("//button[@class='btn btn-svoc login-btn']").click()
<<<<<<< HEAD
driver.implicitly_wait(10)
driver.find_element_by_xpath("//a[contains(.,'个人控制台')]").click()
=======
driver.find_element_by_xpath("//a[contains(.,'个人控制台')]").click()
>>>>>>> 18e09ec6ee5064675d078c4efa307a9bd20baf60
