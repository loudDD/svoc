from selenium import webdriver
from config.readconfig import readConfig

url=readConfig().getconfigvalue("url","ucUrl")


class POM(object):
    def __init__(self):
        try:
            self.driver = webdriver.Chrome()
            self.driver.get(url)
        except Exception:
            raise NameError("Doesn't support well")

    def findelement(self,typ,data):
        try:
            if typ == "id" :
                element = self.driver.find_element_by_id(data)
            elif typ == "class":
                element = self.driver.find_element_by_class_name(data)
            elif typ == "name" :
                element = self.driver.find_element_by_name(data)
            elif typ == "link_text" :
                element = self.driver.find_element_by_link_text(data)
            elif typ == "partial_link_text":
                element = self.driver.find_element_by_partial_link_text(data)
            elif typ == "xpath":
                element = self.driver.find_element_by_xpath(data)
            elif typ == "css":
                element = self.driver.find_element_by_css_selector(data)
            else:
                raise NameError("无法识别的定位方式" , typ)
        except Exception:
            raise NameError("请重新输入！")
        return element

    def click(self,element):
        element.click()

    def send_keys(self,element,text):
        element.send_keys(text)


    # def Act(self,element,action,value=None):
    #     if action=="send_keys":
    #         element.send_keys(value);
    #     if action=="click":
    #         element.click()
    #     if action=="enter":
    #         element.send_keys(Keys.RETURN)

    def display(self,data):
        js = 'documnet.getElementById(list[id]).style.display="block"'
        self.driver.execute_script(js)

    def quit(self):
        self.driver.quit()
