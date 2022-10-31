from selenium import webdriver
import threading
from selenium.webdriver.chrome.options import Options

lock = threading.Lock()
def login_search(browser, url):
    lock.acquire()
    if browser == 'Chrome':
        chrome_option = Options()
        chrome_option.add_argument('--headless')
        chrome_option.add_argument('--disable-gpu')
        executable_path = r'PO\tools\chromedriver.exe'
        dr = webdriver.Chrome(executable_path=executable_path,chrome_options=chrome_option)
    elif browser == 'FireFox':
        firefox_option = webdriver.FirefoxOptions()
        firefox_option.add_argument('--headless')
        firefox_option.add_argument('--disable-gpu')
        fire_path = r'tools\geckodriver.exe'
        dr = webdriver.Firefox(executable_path=fire_path,firefox_options=firefox_option)
    elif browser == 'Ie':
        ie_path = r'D:\Driver_browser\IEDriverServer.exe'
        dr = webdriver.Ie(executable_path=ie_path)
    dr.get(url)
    dr.maximize_window()
    lock.release()
    return dr



def threads():
    threads = []
    data = {"Chrome":"http://47.96.181.17:9090/"}
    for browser, url in data.items():
        t = threading.Thread(target=login_search, args=(browser, url))
        threads.append(t)
    for thr in threads:
        thr.start()
