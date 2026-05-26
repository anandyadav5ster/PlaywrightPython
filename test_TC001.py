import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

def test_has_title(page: Page):
    base_page bp = BasePage(page)
    # page.goto("https://playwright.dev/")
    base_page.open_application("https://playwright.dev/")


    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

def test_handle_new_tab(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/p/playwrightpractice.html')
    with page.context.expect_page() as newTab_info:
        page.locator('button[onclick="myFunction()"]').click()
    newTab = newTab_info.value
    newTab.wait_for_load_state() 
    title = newTab.title()
    print('Title of the page is ',title)