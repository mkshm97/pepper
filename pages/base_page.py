from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from .locators import MainPageLocators
# from .locators import SettingsPageLocators
# from .locators import LoginPageLocators
# from .locators import UsersPageLocators
# from .locators import ResourcePageLocators
# from .locators import CertificatePageLocators
# from .locators import JournalsPageLocators
# from .locators import LicensePageLocators
# from .locators import ServerPageLocators
# from .locators import DocumentationPageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        try:
            self.browser.get(self.url)
        except (WebDriverException):
            return False

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_elements_present(self, how, what):
        try:
            self.browser.find_elements(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=3):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_appeared(self, how, what, timeout=360):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def open_new_window(self):
        self.browser.execute_script("window.open('')")
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)

    def switch_to_window(self, window_number):
        window = self.browser.window_handles[window_number]
        self.browser.switch_to.window(window)

    def refresh_window(self):
        self.browser.refresh()