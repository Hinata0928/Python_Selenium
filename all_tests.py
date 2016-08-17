# coding=utf-8
import HTMLTestRunner
import os, time, datetime
import unittest
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
# import sys
# from test_case import start_baidu, start_youdao
# import allcase_list  #调用数组文件

# 把 test_case 目录添加到 path 下，这里用的相对路径
# sys.path.append('\\test_case')

# 将用例组装数组
# alltestnames = allcase_list.caselist()

# 定义发送邮件
def sentmail(file_new):

    mail_from='1157088130@qq.com' #发信邮箱
    mail_to = '409365364@qq.com'    # 收信邮箱
    f = open(file_new, 'rb')      # 定义正文
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"自动化测试报告"   # 定义标题
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')  # 定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')  # 连接 SMTP 服务器，此处用的qq的 SMTP 服务器
    smtp.login('1157088130@126.com', 'www.0928.com.cn')       # 用户名密码
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print 'email has send out !'

# 查找测试报告，调用发邮件功能
def sendreport():
    result_dir = 'D:\\Practice\\Python+Selenium\\report'

    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn) if not os.path.isdir(result_dir + "\\" + fn) else 0)
    print (u'最新测试生成的报告：' + lists[-1])
    file_new = os.path.join(result_dir, lists[-1])   # 找到最新生成的文件
    print file_new
    sentmail(file_new)    # 调用发邮件模块

# 创建测试套件
listaa = 'D:\\Practice\\Python+Selenium\\test_case'
def creat_suite():

        testunit = unittest.TestSuite()
# discover 方法定义
        discover = unittest.defaultTestLoader.discover(listaa, pattern='start_*.py', top_level_dir=None)
        for test_suite in discover:
            for test_case in test_suite:
                testunit.addTest(test_case)
                print testunit
        return testunit

alltestnames = creat_suite()

# 循环读取数组中的用例
# for test in alltestnames:
#     testunit.addTest(unittest.makeSuite(test))


now = time.strftime("%m-%M-%H_%M", time.localtime(time.time()))

filename = 'D:\\Practice\\Python+Selenium\\report\\' + now + 'result.html'
fp = file(filename, 'wb')
# 执行测试套件
# runner = unittest.TextTestRunner()
# runner.run(testunit)

runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'百度搜索测试报告', description=u'用例执行情况:')
runner.run(alltestnames)
