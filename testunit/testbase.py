import unittest

from manager.manager import DriverManager
from base.logBase import BaseLog
from config.config import DRIVER


class TestBase(unittest.TestCase):
    def setUp(self):
        self.manager = DriverManager()
        self.driver = self.manager.get_driver()  # type: DRIVER["type"]
        self.log = BaseLog().log

    def tearDown(self):
        self.manager.close(self.driver)
