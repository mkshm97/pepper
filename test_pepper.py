from pages.main_page import MainPage
from pages.locators import ADDRESS
import pytest


@pytest.mark.pepper_catch_deer
def test_pepper_catch_deer(browser):
    link = ADDRESS
    page = MainPage(browser, link)
    page.open()
    page.catch_deer()
