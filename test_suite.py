import unittest
from test import TestMathFunc
from HwTestReport import HTMLTestReport
# 英文 English
from HwTestReport import HTMLTestReportEN

if __name__ == '__main__':
    suite = unittest.TestSuite()
    #测试
    #使用这种方法可以对测试用例排序
    #tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    #suite.addTests(tests)

    #使用TestLoader的方法传入TestCase
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

    #在同目录下生成txt格式的测试报告
    #with open('UnittestTextReport.txt', 'a') as f:
        #runner = unittest.TextTestRunner(stream=f, verbosity=2)
        #runner.run(suite)

    with open('./HwTestReport.html', 'wb') as report:
        runner = HTMLTestReportEN(stream=report,
                                verbosity=2,
                                title='Test Report',
                                description='chart，with detail',
                                tester='Wei')
        runner.run(suite)
