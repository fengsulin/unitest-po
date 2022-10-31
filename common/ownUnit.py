import unittest
from common.readconfig import *
from page.loginpage import *
from common.logset import *

class MyUnit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dr = ConfigDreiver().readConfig()
        cls.loginpage = LoginPage(cls.dr)
        cls.logger = LogTests().makeLog()
        # self.url = 'http://47.96.181.17:9090/'
        # self.dr = webdriver.Chrome(r'D:\Driver_browser\chromedriver.exe')
        # self.dr.implicitly_wait(20)
        # self.loginpage = LoginPage(self.dr,self.url)

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()
