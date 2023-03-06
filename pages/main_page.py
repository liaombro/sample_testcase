from selenium.webdriver.common.by import By
from .elements_page import ElementsPage

class MainPage:
    URL = "https://demoqa.com/"
    
    ELEMENTS_BUTTON = (By.CSS_SELECTOR, ".top-card:nth-of-type(1)")


    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(MainPage.URL)
        return self
    
    def click_elements_button(self):
        elements_button = self.driver.find_element(*MainPage.ELEMENTS_BUTTON)
        elements_button.click()
        return ElementsPage(self.driver)