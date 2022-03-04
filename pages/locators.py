from selenium.webdriver.common.by import By


class LandingPageLocators():
    SEARCH_FIELD = (By.XPATH, "//input[@title='Поиск']")
    SEARCH_BUTTON = (By.XPATH, "(//input[@name='btnK'])[2]")


class CalculatePageLocators():
    CALCULATE_FIELD = (By.CSS_SELECTOR, ".jlkklc")
    ANSWER_FILED = (By.CSS_SELECTOR, ".jlkklc")
    MEMORY_FIELD = (By.XPATH, "//span[@class='vUGUtc']")
    EQUALS_BUTTON = (By.XPATH, "//div[@aria-label='равно']")
