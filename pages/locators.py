from selenium.webdriver.common.by import By

ADDRESS = "https://www.pepper.ru/"


class MainPageLocators():
    DEER = (By.CSS_SELECTOR,
                     "body > div.mc-notification.zIndex--fixed > div > div > div > span")
    USER_ICON = (By.CSS_SELECTOR,
            "#main > div:nth-child(1) > header > div > div > div.lbox--v-9.vue-rendered > div:nth-child(4) > button > img")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#main > div:nth-child(1) > header.width--all-12.forceLayer.zIndex--fixed.js-sticky > div > div > div.lbox--v-9.vue-rendered > button.btn.btn--mode-header.btn--toW5-square.space--ml-2")
    LOGIN = (By.CSS_SELECTOR, "#loginModalForm-identity")
    PASSWORD = (By.CSS_SELECTOR, "#loginModalForm-password")
    LOGIN_CONFIRM_BUTTON = (By.CSS_SELECTOR, "body > section > div.popover-content.popover-content--expand > div > div > div > div:nth-child(3) > div:nth-child(2) > ul > li > div > button")