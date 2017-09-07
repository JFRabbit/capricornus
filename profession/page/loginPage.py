# coding: utf-8
from base.basePage import Page


class LoginPage(Page):
    '''登录页'''

    login_url = "http://192.168.130.55:5003"

    username_input_loc = (Page.id, "username")
    password_input_loc = (Page.id, "password")
    submit_btn_loc = (Page.xpath, "//input[@value='登录']")

    TARGET_URL = 'http://192.168.130.55:5003/projects'
