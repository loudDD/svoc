from selenium import webdriver
from svoc.config.readconfig import readConfig
url = readConfig().getconfigvalue("url", "ucUrl")


class POM(object):
    """
    根据POM封装basepage：定位方法，操作（目前操作主要是send_keys,click
    """
    def __init__(self):
        try:
            self.driver = webdriver.Chrome()
            self.driver.get(url)
        except Exception:
            raise NameError("Doesn't support well")

    def findelement(self, typ, data):
        """ 使用try来判断元素是否可识别；
            使用if来判断元素内容，以此确定查找元素方式
        """
        try:
            if typ == "id":
                element = self.driver.find_element_by_id(data)
            elif typ == "class":
                element = self.driver.find_element_by_class_name(data)
            elif typ == "name":
                element = self.driver.find_element_by_name(data)
            elif typ == "link_text":
                element = self.driver.find_element_by_link_text(data)
            elif typ == "partial_link_text":
                element = self.driver.find_element_by_partial_link_text(data)
            elif typ == "xpath":
                element = self.driver.find_element_by_xpath(data)
            elif typ == "css":
                element = self.driver.find_element_by_css_selector(data)
            else:
                raise NameError("无法识别的定位方式", typ)
        except Exception:
            raise NameError("请重新输入！")
        return element

    def click(self, element):
        """点击操作"""
        element.click()

    def send_keys(self, element, text):
        """发送内容"""
        element.send_keys(text)
    def clear(self,element):
        element.clear()


    # def Act(self,element,action,value=None):
    #     if action=="send_keys":
    #         element.send_keys(value);
    #     if action=="click":
    #         element.click()
    #     if action=="enter":
    #         element.send_keys(Keys.RETURN)

    def display(self):
        """判断元素是否显示，需根据实际结果更改"""
        js = 'documnet.getElementById(list[id]).style.display="block"'
        self.driver.execute_script(js)

    def quit(self):
        """关闭浏览器"""
        self.driver.quit()
