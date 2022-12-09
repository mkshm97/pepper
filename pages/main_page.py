from .base_page import BasePage
from .locators import MainPageLocators
import time


class MainPage(BasePage):
    def catch_deer(self):
        login = 'cor4agin.maksim@yandex.ru'
        password = '26091997max'
        self.browser.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        time.sleep(2)
        self.browser.find_element(*MainPageLocators.LOGIN).send_keys(login)
        self.browser.find_element(*MainPageLocators.PASSWORD).send_keys(password)
        self.browser.find_element(*MainPageLocators.LOGIN_CONFIRM_BUTTON).click()
        time.sleep(5)
        while True:
            if self.is_appeared(*MainPageLocators.DEER):
                time.sleep(2)
                self.browser.find_element(*MainPageLocators.DEER).click()
                time.sleep(5)
                self.refresh_window()
            else:
                self.refresh_window()
                # time.sleep(5)
                # assert self.is_element_present(*MainPageLocators.USER_ICON)
