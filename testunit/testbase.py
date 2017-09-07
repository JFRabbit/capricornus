import unittest
from selenium import webdriver

from manager.manager import DriverManager


class TestBase(unittest.TestCase):
    def setUp(self):
        self.manager = DriverManager()
        self.driver = self.manager.get_driver()  # type: webdriver.Chrome

    def tearDown(self):
        self.manager.close(self.driver)
