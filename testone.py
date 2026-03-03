import pytest
from playwright.sync_api import sync_playwright, expect

# Change scope to "module" to run setup ONLY ONCE for this file
@pytest.fixture(scope="module")
def browser_context():
    print("\n[Setup] Launching browser once for the module...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        # Create the page and navigate ONCE
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
        
        yield page 
        
        print("\n[Teardown] Closing browser after all tests...")
        browser.close()

def test_page_navigation(browser_context):
    page = browser_context
    expect(page).to_have_title("Automation Testing Practice: PlaywrightPractice")

def test_enter_input(browser_context):
    page = browser_context
    # Note: Using 'textbox' role for input fields
    page.get_by_role("textbox", name="Name:").fill("test")