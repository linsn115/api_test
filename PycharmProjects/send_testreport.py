import HTMLTestRunner
import os
import unittest
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def report():
     # 设置报告文件保存路径

    report_path = os.path.dirname(os.path.abspath('')) + 'test_report/'
    # 获取系统当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

        # 设置报告名称格式
    HtmlFile = "HTMLtemplate.html"
    fp = open(HtmlFile, "ab+")
    return fp,HtmlFile


# 发送到邮箱
def send_mail(HtmlFile):
    #邮箱服务器
    smtpserver = 'smtp.163.com'
    #发送邮箱
    sender = 'username@163.com'
    #发送邮箱的账号密码
    username = 'username@163.com'
    password = 'password'
    #发送邮件主题
    subject = '自动化测试报告'
    #接收邮箱
    receiver = 'username@163.com'
    #文件内容
    f = open(HtmlFile, 'rb')
    mail_body = f.read()
    mail_body=mail_body.decode('utf8')
    f.close()
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header(subject,'utf-8')

    msg['from'] = 'username@163.com'
    msg['to'] = 'username@163.com'

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()

# 构建suite

listaa = os.path.dirname(os.getcwd())


def creatsuite1():
    testunit = unittest.TestSuite()
    # discover 方法定义
    discover = unittest.defaultTestLoader.discover(listaa, pattern='test_baidu_search1.py', top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)

    return testunit



if __name__ == '__main__':
    fp = report()
    HtmlFile1 = report()
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"某某项目测试报告", description=u"用例测试情况")
    # 开始执行测试套件
    alltestnames = creatsuite1()
    print(type(alltestnames))
    runner.run(alltestnames)
    fp.close()
    send_mail(HtmlFile1)


