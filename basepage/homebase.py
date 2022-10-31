
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.logset import LogTests

#  调用日志类
logger = LogTests().makeLog()

class HomePage(object):
    def __init__(self,dr):
        self.dr = dr
        # self.url = url

    def findElement(self, *loca):
        try:
            element = WebDriverWait(self.dr, 20).until(EC.presence_of_element_located(loca))
            return element
        except Exception as e:
            logger.info(f'元素定位失败，因为:{e}')

    def back_page(self):
        self.dr.back()





