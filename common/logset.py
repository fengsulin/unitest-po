import logging
import os
import time
class LogTests():
    def makeLog(self):
        '''创建日志方法'''
        # 创建一个日志对象
        logger = logging.getLogger('log_test')
        # 设置日志等级
        logger.setLevel(logging.INFO)
        # 判断日志对象中是否有Handler
        if not logger.handlers:
            # 定义日志文件
            fe = time.strftime("%Y_%m_%d_%H_%M_%S")+'logTest.log'
            filename = os.path.dirname(os.path.abspath('.')) +'/logs/' +fe
            ft = logging.FileHandler(filename,'a',encoding='utf-8')
            # 创建日志格式器
            fmt = logging.Formatter(fmt='%(asctime)s-%(filename)s-%(levelname)s-%(message)s',datefmt='%Y_%m_%d_%H-%M-%S')
            ft.setFormatter(fmt)
            logger.addHandler(ft)
            return logger

        return logger



