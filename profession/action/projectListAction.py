# coding: utf-8
import re

from base.baseAction import BaseAction
from profession.page.projectListPage import ProjectListPage as plp


class ProjectAction(BaseAction):
    def create_new_project(self, project_name, project_desc=""):
        self.click(*plp.create_new_project_btn_loc)
        self.sleep(2)
        self.send_keys(*plp.project_name_input_loc, value=project_name)
        self.send_keys(*plp.project_desc_input_loc, value=project_desc)
        self.click(*plp.confirm_btn_loc)

        self.sleep(3)
        assert re.match(plp.TARGET_URL, self.driver.current_url) != None
