# coding = utf-8
from selenium import webdriver
import time

from config.config import *
from base.logBase import BaseLog


class DriverManager(object):
    def __init__(self):
        self.log = BaseLog().log

    def get_driver(self):
        '''get WebDriver'''
        self.log.info(">>> init driver ")

        switcher = {"LOCAL_CHROME": self.__create_chrome_driver()}

        driver = switcher.get(DRIVER["type"])
        self.log.info("<<< init done ")
        return driver

    def close(self, driver):
        '''close WebDriver'''
        self.log.info("close driver: %s", driver)
        if driver != None: driver.quit()

    def __set_basic_web_property(self, driver):
        self.log.info("__WINDOW: max")
        driver.maximize_window()
        self.log.info("__DEFAULT_FIND_ELEMENT_TIMEOUT: %ds", DEFAULT_FIND_ELEMENT_TIMEOUT)
        driver.implicitly_wait(DEFAULT_FIND_ELEMENT_TIMEOUT)
        self.log.info("__DEFAULT_PAGE_LOAD_TIMEOUT: %ds", DEFAULT_PAGE_LOAD_TIMEOUT)
        driver.set_page_load_timeout(DEFAULT_PAGE_LOAD_TIMEOUT)
        return driver

    def __create_chrome_driver(self):
        self.log.info("create Chrome Driver")
        options = webdriver.ChromeOptions()
        options.add_argument('disable-infobars')
        driver = webdriver.Chrome(chrome_options=options)  # type: webdriver.Chrome
        return self.__set_basic_web_property(driver)


if __name__ == "__main__":
    manager = DriverManager()
    driver = manager.get_driver()

    time.sleep(3)

    manager.close(driver)
