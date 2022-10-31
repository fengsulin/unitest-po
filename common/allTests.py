import unittest
from HTMLTestRunner import HTMLTestRunner
from common.sendmail import *
import os
import time


def makeReports():
    testpath = os.path.dirname(os.path.abspath('.')) + '/testcases/'
    suite = unittest.defaultTestLoader.discover(start_dir=testpath, pattern='test*.py')
    reportdir = os.path.dirname(os.path.abspath('.')) + '/reports/' + time.strftime(
        '%Y_%m_%d_%H_%M_%S') + '_report.html'
    fp = open(reportdir, 'wb')
    runner = HTMLTestRunner(stream=fp, title='python自动化测试报告', description='测试结果描述', verbosity=2)
    runner.run(suite)
    fp.close()


if __name__ == '__main__':
    makeReports()
    test_dir = os.path.dirname(os.path.abspath('.')) + '/reports/'
    send_path = new_file(test_dir)
    send_mail(send_path)
