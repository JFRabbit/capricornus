# coding = utf-8
import time

from config.baseConfig import *
from base.logBase import BaseLog


class DriverManager(object):
    def __init__(self):
        self.log = BaseLog().log

    def get_driver(self):
        '''get WebDriver'''
        self.log.info(">>> init driver ")

        driver = self.__init_driver(DRIVER["type"])

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

    def __init_driver(self, driver_type):
        if driver_type == webdriver.Chrome:
            self.log.info("Create Chrome Driver...")
            options = webdriver.ChromeOptions()
            self.log.info("Set disable-infobars")
            options.add_argument('disable-infobars')
            driver = webdriver.Chrome(chrome_options=options)  # type: webdriver.Chrome
            return self.__set_basic_web_property(driver)
        elif driver_type == webdriver.Firefox:
            # TODO Firefox
            pass

        pass


if __name__ == "__main__":
    manager = DriverManager()
    driver = manager.get_driver()

    time.sleep(3)

    manager.close(driver)