import pytest

from pages.calculate_page import CalculatePage
from pages.landing_page import LandingPage


@pytest.mark.need_review
class TestCalculation():
    @pytest.mark.calculate_first_expression
    def test_calculate_first_expression(self, driver):
        landing_page = LandingPage(driver)
        landing_page.search_key_word()
        landing_page.button_click()

        calc_page = CalculatePage(driver)
        calc_page.calculate_first_expression()

        calc_page.assert_correct_expression_first()
        calc_page.assert_correct_answer_first()

    @pytest.mark.calculate_second_expression
    def test_calculate_second_expression(self, driver):
        landing_page = LandingPage(driver)
        landing_page.search_key_word()
        landing_page.button_click()

        calc_page = CalculatePage(driver)
        calc_page.calculate_second_expression()

        calc_page.assert_correct_expression_second()
        calc_page.assert_correct_answer_second()

    @pytest.mark.calculate_third_expression
    def test_calculate_third_expression(self, driver):
        landing_page = LandingPage(driver)
        landing_page.search_key_word()
        landing_page.button_click()

        calc_page = CalculatePage(driver)
        calc_page.calculate_third_expression()

        calc_page.assert_correct_expression_third()
        calc_page.assert_correct_answer_third()
