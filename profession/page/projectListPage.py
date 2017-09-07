# coding: utf-8
from base.basePage import Page
from selenium.webdriver.common.by import By


class ProjectListPage(Page):
    create_new_project_btn_loc = (By.CLASS_NAME, 'ProjectsPanel__create___2KeDL')
    project_name_input_loc = (By.ID, 'projName')
    project_desc_input_loc = (By.ID, 'description')
    confirm_btn_loc = (By.XPATH, "//span[text()='确 定']")

    TARGET_URL = '^http://192.168.130.55:5003/projects/1(\d){5}$'
