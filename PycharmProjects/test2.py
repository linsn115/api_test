# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# from time import sleep
#
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://192.168.2.73:999/business/?tid=HwV/YUaXg4JGjlV0acBlVg==#/user/login")
#
#
# login_Name=driver.find_element_by_xpath("//input[@placeholder='请输入账号']")
# login_Name.clear()
# login_Name.send_keys("ceshi")
#
# login_Pwd=driver.find_element_by_xpath("//input[@placeholder='请输入密码']")
# login_Pwd.clear()
# login_Pwd.send_keys("123456qwer")
#
# login_Btn=driver.find_element_by_xpath("//button[@class='el-button form-submit el-button--default el-button--large']")
# login_Btn.click()
# sleep(3)
# current_url = driver.current_url
# print(current_url)
# if current_url == "http://192.168.2.73:999/business/?tid=HwV/YUaXg4JGjlV0acBlVg==#/signUp1":
#     print("登陆成功")
#     btn = driver.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small el-button--primary ']")
#     print(btn.text)
#     btn.click()
#     anchor_Name = driver.find_element_by_xpath("//input[@placeholder='主播名称']").text
#     print("主播名称%s"%anchor_Name)
#     choose_Date = driver.find_element_by_xpath("//input[@placeholder='选择日期']")
#     choose_Date.click()
#     #choose = driver.find_elements_by_class_name("available")[28]
#     choose = driver.find_element_by_xpath("//td[@class='available today']")
#     #choose = driver.find_element_by_xpath('//span[contains(text(),"20"]')
#     print(choose.text)
#     choose.click()
#     driver.find_element_by_xpath("//button[@class='el-button el-button--warning']").click()
#     sleep(1)
#     driver.find_element_by_xpath("//button[@class='el-button el-button--default is-round'").click()
# else:
#     print("登陆失败")

from selenium import webdriver
import unittest,time
import HTMLTestRunner
class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def test_login(self):
        self.driver.get("http://192.168.2.73:999/business/?tid=HwV/YUaXg4JGjlV0acBlVg==#/user/login")
        login_Name = self.driver.find_element_by_xpath("//input[@placeholder='请输入账号']")
        login_Name.clear()
        login_Name.send_keys("ceshi")

        login_Pwd = self.driver.find_element_by_xpath("//input[@placeholder='请输入密码']")
        login_Pwd.clear()
        login_Pwd.send_keys("123456qwer")

        login_Btn = self.driver.find_element_by_xpath(
            "//button[@class='el-button form-submit el-button--default el-button--large']")
        login_Btn.click()
        time.sleep(3)
        current_url = self.driver.current_url
        print(current_url)
        if current_url == "http://192.168.2.73:999/business/?tid=HwV/YUaXg4JGjlV0acBlVg==#/signUp1":
            print("登陆成功")
            btn = self.driver.find_element_by_xpath(
                "//button[@class='el-button el-button--default el-button--small el-button--primary ']")
            print(btn.text)
            btn.click()
            anchor_Name = self.driver.find_element_by_xpath("//input[@placeholder='主播名称']").text
            print("主播名称%s" % anchor_Name)
            choose_Date = self.driver.find_element_by_xpath("//input[@placeholder='选择日期']")
            choose_Date.click()
            # choose = driver.find_elements_by_class_name("available")[28]
            choose = self.driver.find_element_by_xpath("//td[@class='available today']")
            # choose = driver.find_element_by_xpath('//span[contains(text(),"20"]')
            print(choose.text)
            choose.click()
            # self.driver.find_element_by_xpath("//button[@class='el-button el-button--warning']").click()
            # time.sleep(1)
            # self.driver.find_element_by_xpath("//button[@class='el-button el-button--default is-round'").click()
        else:
            print("登陆失败")
    def tearDown(self):
        self.driver.quit()
#driver.quit()
if __name__=="__main__":
    testSuite=unittest.TestSuite()
    testSuite.addTest(LoginTest("test_login"))
    Html="test1.html"
    fp=open(Html,'wb')

    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'百度搜索测试报告',description=u'用例执行情况：')
    print(runner)
    runner.run(testSuite)
    fp.close()