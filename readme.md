Goal 	Command Flag
Run in Headed Mode	pytest --headed (opens the browser window)
Specify Browser	pytest --browser firefox (options: chromium, firefox, webkit)
Run Multiple Browsers	pytest --browser chromium --browser webkit
Run a Specific File	pytest test_login.py
Slow Down Execution	pytest --slowmo 500 (adds 500ms delay between actions)
Record Video	pytest --video on
Take Screenshots	pytest --screenshot on



JavaScript/TypeScript (CamelCase)	Python (Snake_case)	What it verifies
expect(locator).toContainText()	expect(locator).to_contain_text()	Element contains specific text
expect(locator).toHaveText()	expect(locator).to_have_text()	Element matches exact text
expect(locator).toBeVisible()	expect(locator).to_be_visible()	Element is visible on screen
expect(page).toHaveTitle()	expect(page).to_have_title()	Web page title matches string



The Fix: Update your pytest.ini
The cleanest way to change this permanently for your entire framework is to add the -v (verbose) flag to your addopts string inside your pytest.ini file.

Open your pytest.ini and add -v to your existing configuration line:
addopts = -v --browser_name=chromium --headless=false --html=myreport.html



To install pytest-sugar (which shows a live progress bar and clean status lists):
pip install pytest-sugar
