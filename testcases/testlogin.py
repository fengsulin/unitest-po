import unittest
from common.ownUnit import MyUnit
from common.read_data import *
import time
from common.cutscreen import *
from ddt import data, ddt, unpack


# @ddt
class TestLogin(MyUnit, Helper):
    '''用例对象类，'''

    # @data()
    # @unpack
    @getImage
    def test_login(self):
        '''正确的用户名和密码---登陆成功'''
        # self.loginpage.openLoginPage()
        self.loginpage.login_pro(self.read_user(1), self.read_pwd(1))
        self.assertEqual(self.loginpage.get_assertText(), self.read_text(1), msg='登陆失败')
        self.loginpage.back_page()

    @getImage
    def test_pwd_null(self):
        '''正确用户名，密码为空---登陆失败'''
        self.loginpage.login_pro(self.read_user(2), self.read_pwd(2))
        self.assertEqual(self.read_text(2), self.loginpage.password_null(), msg='请输入密码')

    @getImage
    def test_user_null(self):
        '''正确密码，用户名为空---登陆失败'''
        self.loginpage.login_pro(self.read_user(3), self.read_pwd(3))
        self.assertEqual(self.read_text(3), self.loginpage.password_null(), msg='请输入用户名')

    @getImage
    def test_all_null(self):
        '''用户名和密码为空---登陆失败'''
        self.loginpage.login_pro(self.read_user(4), self.read_pwd(4))
        self.assertEqual(self.read_text(4), self.loginpage.password_null(), msg='请输入用户名')


if __name__ == '__main__':
    unittest.main
