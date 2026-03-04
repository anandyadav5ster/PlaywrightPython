import pytest
import base64
from playwright.sync_api import sync_playwright

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    # Capture at the end of the test execution ('call' phase)
    if report.when == "call":
        # Make sure this matches the fixture name in your test file
        fixture_name = "browser_context" 
        
        if fixture_name in item.funcargs:
            page = item.funcargs[fixture_name]
            screenshot = page.screenshot(type="png")
            
            # Encode for HTML embedding
            encoded = base64.b64encode(screenshot).decode("ascii")
            
            # Label based on status
            label = "Final State (Pass)" if report.passed else "Failure Screenshot"
            
            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html:
                # Add image to the report
                image_html = f'<div><b>{label}:</b><br><img src="data:image/png;base64,{encoded}" style="width:600px;"></div>'
                extra.append(pytest_html.extras.html(image_html))
                report.extra = extra

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