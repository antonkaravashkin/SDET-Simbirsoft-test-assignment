import pytest

from Variables.data import LANDING_PAGE_URL

from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(LANDING_PAGE_URL)
    yield driver
    driver.quit()
