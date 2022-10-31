from functools import wraps
from common.logset import *
import traceback
import time
import os


def getImage(function):
    '''定义修饰器，获取运行失败界面图片'''
    @wraps(function)
    def get_ErrImage(self, *args, **kwargs):
        try:
            result = function(self, *args, **kwargs)
            self.logger.info(function.__name__ + '脚本运行正常')
        except Exception as e:
            imagepath = os.path.dirname(os.path.abspath('.')) + '/image/' + time.strftime(
                '%Y_%m_%d_%H_%M_%S') + 'erroimage.png'
            self.dr.get_screenshot_as_file(imagepath)
            traceback.print_exc(e)

    return get_ErrImage
