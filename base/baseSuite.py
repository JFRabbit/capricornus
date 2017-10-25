import unittest
from base.baseLog import BaseLog


class BaseSuite(object):
    def __init__(self, run_classes):
        self.run_classes = run_classes  # type: dict
        self.log = BaseLog().log

    def run(self):
        self.log.info("\n\n Test Start \n ------------------------------------------------------------> ")

        suite = unittest.TestSuite()
        for case, is_run in self.run_classes.items():
            test = unittest.TestLoader().loadTestsFromTestCase(case)
            if is_run == 1:
                suite.addTest(test)
                self.log.info("Run Case: %s", test)
            elif is_run == 0:
                self.log.info("Not Run Case: %s", test)
                pass
            else:
                raise Exception("Wrong Arguments! 0:not run, 1:run")

        unittest.TextTestRunner().run(suite)
        self.log.info("\n\n <------------------------------------------------------------ \nTest End\n\n\n ")
