import unittest

from base.baseLog import BaseLog
from testcase.demo.testcase1 import TestDemo

if __name__ == "__main__":
    demo_test = unittest.TestLoader().loadTestsFromTestCase(TestDemo)
    log = BaseLog().log
    log.info("\n\n Test Start \n ------------------------------------------------------------> ")
    unittest.TextTestRunner().run(demo_test)
    log.info("\n\n <------------------------------------------------------------ \nTest End\n\n\n ")
