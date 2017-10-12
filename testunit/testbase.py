import unittest
from selenium import webdriver

from manager.manager import DriverManager
from base.logBase import BaseLog


class TestBase(unittest.TestCase):
    def setUp(self):
        self.manager = DriverManager()
        self.driver = self.manager.get_driver()  # type: webdriver.Chrome
        self.log = BaseLog().log

    def tearDown(self):
        self.manager.close(self.driver)
