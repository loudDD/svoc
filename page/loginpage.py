from page.basepage import POM
from time import sleep
import string
import random
class LoginPage(POM):
    """
    登录测试：根据error返回判定登录结果
    有错误信息：信息对比
    无错误信息：登录成功
    TODO:登录页其他功能
    """
    #login
    userlocator = ["css","[formcontrolname='username']"]
    pwdlocator  = ["css","[formcontrolname='password']"]
    loginlocator= ["css","button"]
    #sigin
    signinbutton = ['link_text','立即注册']
    accountinput = ["css",'.ng-dirty:nth-child(2)']
    pwdinput = ['css','.pw-group > .form-control']
    phoneinput = ['css',"[formcontrolname='mobile']"]
    vericodeinput = ['css',"[maxlength='6']"]
    siginbutton = ['class',"btn btn-svoc login-btn"]
    e_username = []
    for i in range(5):
        e_username.append(random.choice([string.ascii_letters]))
    username = "".join(e_username)
    e_phone = [186,]
    for i in range(8):
        e_phone.append(random.randrange(0,9))
    phone = "".join([str(x) for x in e_phone])

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
            raise ValueError("cannot find the locator",e)
            self.driver.quit()

    def forgetpwd(self,):
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
            raise ("注册发生错误",e)
