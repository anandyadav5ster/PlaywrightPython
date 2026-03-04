import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.usefixtures("browser_context")
class TestPlaywright:

    def test_page_navigation(self,browser_context):
        page = browser_context
        expect(page).to_have_title("Automation Testing Practice: PlaywrightPractice")

    def test_enter_input(self,browser_context):
        page = browser_context
        # Note: Using 'textbox' role for input fields
        textbox = page.get_by_role("textbox", name="Name:")
        textbox.fill("test")
        getInputValue = textbox.input_value()
        expect(textbox,'Input value should be present').to_have_value('test')

    def test_click_on_checkbox(self,browser_context):
        page = browser_context
        checkbox = page.get_by_role('checkbox',name = 'Accept term')
        checkbox.check()
        expect(checkbox, 'Checkbox should be checked').to_be_checked()