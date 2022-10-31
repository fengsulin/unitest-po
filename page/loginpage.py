from basepage.homebase import *
from selenium.webdriver.common.by import By


class LoginPage(HomePage):
    '''页面对象类，定义页面的定位元素，和操作流程'''
    username = (By.ID, 'userName')
    passoword = (By.ID, 'password')
    loginbtn = (By.XPATH, '//span/a')
    assertlogin = (By.CSS_SELECTOR,'span.form-control')
    outlogin = (By.CSS_SELECTOR,'.nav.navbar-top-links.navbar-right li:nth-child(4) a')
    pwdnull = (By.ID,'alertMessage')

    def openLoginPage(self):
        self.dr.get(self.url)
        self.dr.refresh()
        self.dr.maximize_window()

    def input_username(self, uname):
        self.findElement(*self.username).clear()
        self.findElement(*self.username).send_keys(uname)

    def input_password(self, pwd):
        self.findElement(*self.passoword).clear()
        self.findElement(*self.passoword).send_keys(pwd)

    def click_Btn(self):
        self.findElement(*self.loginbtn).click()

    def out_login(self):
        self.findElement(*self.outlogin).click()

    def get_assertText(self):
        return self.findElement(*self.assertlogin).text
    def password_null(self):
        return self.findElement(*self.pwdnull).text

    def login_pro(self, uname, pwd):
        self.input_username(uname)
        self.input_password(pwd)
        self.click_Btn()
