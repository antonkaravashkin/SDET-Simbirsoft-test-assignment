from .locators import CalculatePageLocators
import Variables.data
from .landing_page import LandingPage
from selenium.webdriver.common.keys import Keys



class CalculatePage(LandingPage):
    def calculate_first_expression(self):
        calculate = self.driver.find_element(*CalculatePageLocators.CALCULATE_FIELD)
        calculate.send_keys(*Variables.data.EXPRESSION1 + Keys.RETURN)
        self.equals = self.driver.find_element(*CalculatePageLocators.MEMORY_FIELD).text
        self.answer = self.driver.find_element(*CalculatePageLocators.ANSWER_FILED).text


    def assert_correct_expression_first(self):
        assert self.equals == Variables.data.CORRECTEXPRESSION1, "Expressions aren't equals"

    def assert_correct_answer_first(self):
        assert self.answer == Variables.data.ANSWER1, "answer isn't correct"

    def calculate_second_expression(self):
        calculate = self.driver.find_element(*CalculatePageLocators.CALCULATE_FIELD)
        calculate.send_keys(*Variables.data.EXPRESSION2 + Keys.RETURN)
        self.equals = self.driver.find_element(*CalculatePageLocators.MEMORY_FIELD).text
        self.answer = self.driver.find_element(*CalculatePageLocators.ANSWER_FILED).text


    def assert_correct_expression_second(self):
        assert self.equals == Variables.data.CORRECTEXPRESSION2, "Expressions aren't equals"

    def assert_correct_answer_second(self):
        assert self.answer == Variables.data.ANSWER2, "answer isn't correct"

    def calculate_third_expression(self):
        calculate = self.driver.find_element(*CalculatePageLocators.CALCULATE_FIELD)
        calculate.send_keys(*Variables.data.EXPRESSION3 + Keys.RETURN)
        self.equals = self.driver.find_element(*CalculatePageLocators.MEMORY_FIELD).text
        self.answer = self.driver.find_element(*CalculatePageLocators.ANSWER_FILED).text


    def assert_correct_expression_third(self):
        assert self.equals == Variables.data.CORRECTEXPRESSION3, "Expressions aren't equals"

    def assert_correct_answer_third(self):
        assert self.answer == Variables.data.ANSWER3, "answer isn't correct"