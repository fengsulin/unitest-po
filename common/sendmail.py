import yagmail
from common.logset import *

logger = LogTests().makeLog()


def send_mail(newpath):
    '''yagmail实现自动发送邮件'''
    yagindex = yagmail.SMTP(user='1811443663@qq.com', password='vuhaarydsleteefd', host='smtp.qq.com')
    yag_contents = 'python自动化测试报告'
    yagindex.send('18311705272@163.com', 'yagmail自动化测试报告附件', yag_contents, [newpath])
    logger.info('发送邮件成功！')


def new_file(test_dir):
    '''获取最新生成的报告的路径'''
    lists = os.listdir(test_dir)
    lists.sort()
    file = [x for x in lists if x.endswith('.html')]
    file_path = os.path.join(test_dir, file[-1])
    return file_path
