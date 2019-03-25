from page.basepage import POM
from time import sleep
import string
import random
import json




class LoginPage(POM):
    """
    登录测试：根据error返回判定登录结果
    有错误信息：信息对比
    无错误信息：登录成功
    TODO:登录页其他功能
    """

    with open(r"C:\Users\loudDD\GitProject\svoc\svoc\Locator\locator.json", "r", encoding="utf-8") as f:
        # login
        userlocator = f["Loginin"]["userlocator"]
        pwdlocator = f["Loginin"]["pwdlocator"]
        loginlocator = f["Loginin"]["loginlocator"]
        #sigin
        signinbutton = f["Signin"]["signinbutton"]
        accountinput = f["Signin"]["accountinput"]
        pwdinput = f["Signin"]["pwdinput"]
        phoneinput = f["Signin"]["phoneinput"]
        vericodeinput = f["Signin"]["vericodeinput"]
        siginbutton = f["Signin"]["siginbutton"]
        e_username = []
        for i in range(5):
            e_username.append(random.choice([string.ascii_letters]))
        username = "".join(e_username)
        e_phone = [186,]
        for i in range(8):
            e_phone.append(random.randrange(0,9))
        phone = "".join([str(x) for x in e_phone])
        #匿名加入会议
        joinmeetingButton = f["joinmeetingAna"]["joinmeetingButton"]
        meetingnumber = f["joinmeetingAna"]["meetingnumber"]
        connectionButton = f["joinmeetingAna"]["connectionButton"]
        #forgetbutton = ["linkText","忘记密码？"]
        #forgetaccout = ["name","account"]

    def login(self,user,password):
        try:
            self.findelement(self.userlocator).clear()
            self.findelement(self.userlocator).send_keys(user)
            self.findelement(self.pwdlocator).click()
            self.findelement(self.pwdlocator).send_keys(password)
            self.findelement(self.loginlocator).click()
            sleep(10)
        except Exception as e:
            print(e)

    def forgetpwd(self,):
        #验证码暂无法获取
        pass

    def sigin(self):
        try:
            self.findelement(self.signinbutton).click()
            self.findelement(self.accountinput).send_keys(self.username)
            self.findelement(self.pwdinput).send_keys(123456)
            self.findelement(self.phoneinput).send_keys(self.phone)
            self.findelement(self.vericodeinput).send_keys(906882)
            self.findelement(self.signinbutton).click()
        except Exception as e:
            print ("注册发生错误",e)

    def joinmeetingAna(self,meetingNum):
        #卡住，授权摄像头
        try:
            self.findelement(self.joinmeetingButton).click()
            self.findelement(self.meetingnumber).send_keys(meetingNum)
            self.findelement(self.connectionButton).click()
        except Exception as e:
            print(e)

