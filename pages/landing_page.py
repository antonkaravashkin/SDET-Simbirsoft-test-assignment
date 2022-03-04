import Variables.data

from .locators import LandingPageLocators


class LandingPage():
    def __init__(self, driver):
        self.driver = driver

    def search_key_word(self):
        find_field = self.driver.find_element(*LandingPageLocators.SEARCH_FIELD)
        find_field.send_keys(*Variables.data.KEY_WORD)

    def button_click(self):
        click_search = self.driver.find_element(*LandingPageLocators.SEARCH_BUTTON)
        click_search.click()
