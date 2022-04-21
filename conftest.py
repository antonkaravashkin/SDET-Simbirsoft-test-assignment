import pytest

from Variables.data import LANDING_PAGE_URL

from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080')
    _driver = webdriver.Chrome(options=chrome_options)
    _driver.implicitly_wait(3)
    _driver.get(LANDING_PAGE_URL)
    yield _driver
    _driver.quit()
