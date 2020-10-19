from selenium import webdriver
import unittest,time
import HTMLTestRunner
class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url ="http://www.baidu.com"

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url +"/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()




if __name__=="__main__":
    # testSuite = unittest.TestSuite()
    # testSuite.addTest(MyTest("test_baidu"))
    #
    # now = time.strftime('%Y-%m-%d %H_%M_%S')  # 获取当前时间，并且格式化为字符串
    # filename = './' + now + 'result.html'  # 重构文件名
    # fp = open(filename, 'wb')  # 定义测试报告存放路径
    # runner = HTMLTestRunner(stream=fp, title='百度搜索测试报告', description='用例执行情况')  # 定义测试报告
    # runner.run(testSuite)
    # fp.close()
    testSuite = unittest.TestSuite()
    testSuite.addTest(MyTest("test_baidu"))
    Html = "test1.html"
    fp = open(Html, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'百度搜索测试报告', description=u'用例执行情况：')
    print(runner)
    runner.run(testSuite)
    fp.close()