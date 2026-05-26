import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_login(page: Page):
    login_page = LoginPage(page)
    login_page.launch_application()
    login_page.login()
