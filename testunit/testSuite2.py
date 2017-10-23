import unittest

from testcase.testcase2 import *

Test_Data = {
    TestCase1: 1,
    TestCase2: 1,
    TestCase3: 0,
    TestCase4: 2,
}

if __name__ == "__main__":

    suite = unittest.TestSuite()
    for case, is_run in Test_Data.items():
        test = unittest.TestLoader().loadTestsFromTestCase(case)
        if is_run == 1:
            suite.addTest(test)
            print("Run case: %s" % test)
        elif is_run == 0:
            print("Not run case: %s" % test)
            pass
        else:
            raise Exception("Wrong Arguments! 0:not run, 1:run")

    unittest.TextTestRunner().run(suite)
