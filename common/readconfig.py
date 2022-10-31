import configparser
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from common.logset import LogTests

logger = LogTests().makeLog()


class ConfigDreiver():
    '''通读读取配置文件中的浏览器和url，创建驱动对象，打开首页'''

    def readConfig(self):
        conf = configparser.ConfigParser()
        filename = os.path.dirname(os.path.abspath('.')) + '/config/' + 'configs.txt'
        conf.read(filename, encoding='utf-8')
        browser = conf.get('BrowserType', 'browserName')
        logger.info('浏览器为：%s' % (browser))
        url = conf.get('TestUrl', 'url')
        logger.info('地址为：%s' % url)
        if browser == 'Chrome':
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            # executable_path = r'D:\Driver_browser\chromedriver.exe'
            self.dr = webdriver.Chrome(chrome_options=chrome_options)
        elif browser == 'IE':
            self.dr = webdriver.Ie()
        elif browser == 'Firefox':
            fire_option = webdriver.FirefoxOptions()
            fire_option.add_argument('--headless')
            fire_option.add_argument('--disable-gpu')
            self.dr = webdriver.Firefox( firefox_options=fire_option)
        self.dr.maximize_window()
        self.dr.get(url)
        return self.dr
