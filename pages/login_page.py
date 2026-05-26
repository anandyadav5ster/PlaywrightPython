from pages.base_page import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.url = "https://www.saucedemo.com/"
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.loginButton = page.locator('#login-button')
        self.app_logo = page.locator("div.app_logo")


    def launch_application(self):
        self.open_application(self.url)

    def login(self):
        self.username.fill('standard_user')
        self.password.fill('secret_sauce')
        self.loginButton.click()
        expect(self.app_logo).to_contain_text('Swag Labs')


