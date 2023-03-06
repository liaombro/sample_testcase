from selenium.webdriver.common.by import By
from .checkbox_page import CheckboxPage

class ElementsPage:
    
    CHECKBOX_BUTTON = (By.ID, "item-1")

    def __init__(self, driver):
        self.driver = driver

    def click_checkbox_button(self):
        button = self.driver.find_element(*ElementsPage.CHECKBOX_BUTTON)
        button.click()
        return CheckboxPage(self.driver)
