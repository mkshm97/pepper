import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    caps = webdriver.DesiredCapabilities.CHROME.copy()
    caps['acceptInsecureCerts'] = True
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--window-size=1920,1080')
        browser = webdriver.Chrome(options=options, executable_path="C:\chromedriver\chromedriver.exe",
                                   desired_capabilities=caps)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        browser = webdriver.Firefox(firefox_profile=fp, executable_path="C:\chromedriver\geckodriver.exe")
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nrestore factory configuration..")
    # придумать способ сброса к заводским
    print("\nquit browser..")
    browser.quit()
