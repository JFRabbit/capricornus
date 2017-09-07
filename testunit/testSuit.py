import unittest
from base.logBase import BaseLog
from testcase.testcasedemo import TestDemo

if __name__ == "__main__":
    demo_test = unittest.TestLoader().loadTestsFromTestCase(TestDemo)
    log = BaseLog().log
    log.info("\n\n Test Start \n ------------------------------------------------------------> ")
    try:
        unittest.TextTestRunner().run(demo_test)
    except Exception as e:
        log.exception(e)
        raise
    finally:
        log.info("\n\n <------------------------------------------------------------ \nTest End\n\n\n ")
