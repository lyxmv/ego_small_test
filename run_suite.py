import time
import unittest
import app
from lib import HTMLTestRunner
from script.test_ego import TestEgo
# 创建测试套件
suite = unittest.TestSuite()
# 将测试用例添加到测试套件中
suite.addTest(unittest.makeSuite(TestEgo))
# 定义测试报告的名称
reportname = app.BASE_DIR + "/report/mini_ego-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

#使用html生成测试报告
with open(reportname, mode = "wb") as f:
    # 实例化HTMLRunner
    runner = HTMLTestRunner.HTMLTestRunner(f, verbosity=2, title = "ego商城的接口测试报告")
    runner.run(suite)