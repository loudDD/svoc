
from selenium import webdriver

browser=webdriver.Firefox()
browser.maximize_window() # 窗口最大化

browser.get('https://www.baidu.com') # 在当前浏览器中访问百度

# 新开一个窗口，通过执行js来新开一个窗口
js='window.open("https://www.sogou.com");'
browser.execute_script(js)

print (browser.current_window_handle )# 输出当前窗口句柄（百度）
handles = browser.window_handles# 获取当前窗口句柄集合（列表类型）
print (handles) # 输出句柄集合
