from svoc.page.basepage import POM

class Login(POM):
    """
    登录测试：根据error返回判定登录结果
    有错误信息：信息对比
    无错误信息：登录成功
    TODO:登录页其他功能
    """
    userlocator = "css","[formcontrolname='username']"
    pwdlocator  = "css","[formcontrolname='password']"
    loginlocator= "css","button"
    def login(self,user,password):
        try:
            self.findelement(self.userlocator).clear()
            self.findelement(self.userlocator).send_keys(user)
            self.findelement(self.pwdlocator).click()
            self.findelement(self.pwdlocator).send_keys(password)
            self.findelement(self.loginlocator).click()
        except Exception:
            raise ValueError("cannot find the locator")

    def forgetPws(self,):
        pass