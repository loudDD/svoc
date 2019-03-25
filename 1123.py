from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
try:
    # option = Options().add_argument("media.navigator.permission.disabled=true" )
    # d = webdriver.Firefox(options=option)
    # file =webdriver.FirefoxProfile()#r"C:\Users\loudDD\AppData\Roaming\Mozilla\Firefox\Profiles\97tpz030.default"
    # file.set_preference('media.navigator.permission.disabled', True)
    # file.update_preferences()
    d =webdriver.Firefox()#firefox_profile=file
    d.get("https://vip.svocloud.com")
    print(d.title)
    sleep(5)
    d.find_element_by_css_selector("a:nth-child(2)").click()
    # print(d.page_source)
    print("handlers", d.window_handles)

    d.switch_to.window(d.window_handles[1])
    sleep(5)
    d.find_element_by_id("conference-alias").send_keys(3007561)

    d.find_element_by_css_selector(".alert-actions > div > .btn").click()

    sleep(3)
    d.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div/form/div[2]/div/button").click()
    sleep(10)
    # d.find_element_by_css_selector(".alert-actions > div > .btn").click()
    d.switch_to.window(d.window_handles[1])
    print("title:",d.title)
    print("=="*20)
    print("curent_url:",d.current_url)
    print("=="*20)
    print("current window_handle:",d.current_window_handle)
    print("=="*20)
    print(d.window_handles)
    # print("capabilities:",d.capabilities)
    # print("deseired_capabilities:",d.desired_capabilities)
    print("=="*20)
    print("name",d.name)
    print("=="*20)
    print("orientation",d.orientation)
    print("=="*20)
    print(d.page_source)
    d.quit()
except Exception as e:
    raise e
    # print(e)
    # d.quit()
