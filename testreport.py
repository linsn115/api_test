import unittest
import HTMLTestRunner
class testadd(unittest.TestCase):
    def setUp(self):
        pass
    def test_add1(self):
        self.assertEqual(2 + 3 + 10,15)
    def test_add2(self):
        self.assertEqual(10 + 150,160)
    def test_add3(self):
        #一处出错，查看测试结果
        self.assertEqual(10 + 150,160)
    def tearDown(self):
        pass
def suite():
    suiteTest=unittest.TestSuite()
    suiteTest.addTest(testadd("test_add1"))
    suiteTest.addTest(testadd("test_add2"))
    suiteTest.addTest(testadd("test_add3"))
    return suiteTest
if __name__=="__main__":
   # 存放路径在E盘目录下
   filepath='D:\\pyresult.html'
   print(filepath)
   fp=open(filepath,'wb')
   print("dayin")
   #定义测试报告的标题与描述
   runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'我是风起怨江南的测试报告标题',description=u'我是风起怨江南的测试报告描述')
   runner.run(suite())
   fp.close()