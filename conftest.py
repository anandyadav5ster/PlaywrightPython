from pathlib import Path
import pytest
from slugify import slugify
from playwright.sync_api import sync_playwright

# 1. IMPORT THE NEW EXTRAS OBJECT DIRECTLY
from pytest_html import extras

def pytest_addoption(parser):
    """ Register the browser name using --browser_name flag"""
    parser.addoption(
        "--browser_name",
        action="store",
        default="chromium",
        help="Browser type to execute the tests: chromium, firefox, or webkit"
    )
    parser.addoption(
        "--headless",
        action="store",
        default='false',
        help="Run tests in a visible browser window"
    )

@pytest.fixture(scope="function")
def page(request):
    """
    Setup: Runs before each test
    """
    browser_choice = request.config.getoption("browser_name").lower()

     # 1. Launch the browser in headless/headed taking command from terminal
    headless_input = request.config.getoption("headless").lower()
    run_headless = True if headless_input == "true" else False

    print("\n -- setup-- launching browser")
    playwright = sync_playwright().start()
    # 1. Launch the browser with maximized arguments
    launch_args = ["--start-maximized"]

    if browser_choice == "firefox":
        browser = playwright.firefox.launch(headless=run_headless,args = launch_args)
    elif browser_choice == "webkit":
        browser = playwright.webkit.launch(headless=run_headless,args = launch_args)
    else:
        browser = playwright.chromium.launch(headless=run_headless,args = launch_args)
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    yield page

    print("Teardown closing browser")
    page.close()
    context.close()
    browser.close()
    playwright.stop()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Keep this line if you use other config plugins, but we won't use it for screenshots anymore
    pytest_html = item.config.pluginmanager.getplugin("html") 
    
    outcome = yield
    screen_file = ''
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    
    if report.when == "call":
        if "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            screen_file = str(screenshot_dir / f"{slugify(item.nodeid)}.png")
            
            page.screenshot(path=screen_file)
            
            # 2. USE THE NEW SYNTAX HERE
            if pytest_html:
                # Instead of 'pytest_html.extra.png()', use 'extras.png()'
                extra.append(extras.png(screen_file))
                
    report.extra = extra