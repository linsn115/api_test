import unittest
import HTMLTestRunner
import time
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from config import readConfig #为自定义读取配置文件方法
from interface_test import test_baidu
# 用例路径
case_path = "D:\\PycharmProjects\\interface_test"
print(case_path)

# 报告存放路径
report_path = os.path.join(os.getcwd(),'report')
print(report_path)

#定义发送邮件
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport+'\\'+fn)) #获取一个文件中的最近访问时间的文件
    file_new = os.path.join(testreport,lists[-1])
    print("==========获取最近时间生成的报告文件路径===========>"+file_new)
    return file_new

def send_mail(new_report,filename):
    sender = readConfig.getConfig("EMAIL","sender") #读取配置文件中发件人
    sendpwd = readConfig.getConfig("EMAIL","mail_pass") #读取配置文件中发件人密码
    receiver = readConfig.getConfig("EMAIL","receiver") #读取配置文件中收件人
    print("发件人：%s"%sender)
    print("授权码：%s" % sendpwd)
    print("收件人：%s" % receiver)
    f = open(new_report,'rb') #获取报告文件mail_host
    body_main = f.read()

    # 邮件标题
    msg = MIMEMultipart()
    msg['Subject'] = Header('接口自动化测试报告','utf-8')
    msg['From'] = sender
    msg['To'] = receiver

    #邮件内容
    text = MIMEText(body_main,'html','utf-8')
    msg.attach(text)

    #发送邮件
    att = MIMEApplication(open(filename,'rb').read())
    att['Content-Type'] = 'application/octet-stream'
    att.add_header('Content-Disposition','attachment',filename = filename)
    msg.attach(att)

    try:
        smtp = smtplib.SMTP()
        smtp.connect(readConfig.getConfig("EMAIL","mail_host"))
        smtp.login(sender,sendpwd)
        smtp.sendmail(sender,receiver.split(","),msg.as_string())
        print('mail has been send successfully')
    except Exception as e:
        print(e)


def creatsuite():  #创建测试用例集
    # testSuite = unittest.TestSuite()
    # testSuite.addTest(test_baidu.MyTest("test_baidu"))
    testsuite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(
        start_dir=case_path,
        pattern="test*.py",
        top_level_dir=None,
    )
    for allcase in discover:
        for case in allcase:
            print(case)
            testsuite.addTests(case)
    return testsuite

if __name__ == "__main__":
    # 1、按照一定格式获取当前时间
    now = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))

    # 2、html报告文件路径
    filename = os.path.join(report_path,now+"result.html")
    print("测试报告路径==========================>",filename)

    # 3、打开一个文件，将result写入此file中
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                            title="chen测试用例",
                            description="测试情况，如下：",
                            verbosity=2)
    # 4、调用add_case函数返回值
    runner.run(creatsuite())
    fp.close()

    # 5、执行发送邮件
    new_report = new_report(report_path)
    send_mail(new_report,filename)
