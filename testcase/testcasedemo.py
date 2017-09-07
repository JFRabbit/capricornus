import time


from testunit.testbase import TestBase

from profession.action.loginAction import LoginAction
from profession.action.projectListAction import ProjectAction



class TestDemo(TestBase):
    def test(self):
        login_action = LoginAction(self.driver)
        login_action.login()

        project_action = ProjectAction(self.driver)
        project_action.create_new_project('demo')
        time.sleep(3)
