# coding: utf-8
from base.baseAction import BaseAction
from profession.page.loginPage import LoginPage as lp


class LoginAction(BaseAction):
    def login(self, username='k2data', password='K2Data@k001'):
        self.open(lp.login_url)
        self.send_keys(*lp.username_input_loc, value=username)
        self.send_keys(*lp.password_input_loc, value=password)
        self.click(*lp.submit_btn_loc)

        self.sleep(3)
        assert self.driver.current_url == lp.TARGET_URL
