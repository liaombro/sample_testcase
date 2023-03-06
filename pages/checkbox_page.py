from selenium.webdriver.common.by import By

class CheckboxPage:

    HOME_FOLDER_TOGGLE = (By.XPATH, "//*[text()='Home']/parent::*/preceding-sibling::button")
    DOWLOADS_FOLDER_TOGGLE = (By.XPATH, "//*[text()='Downloads']/parent::*/preceding-sibling::button")
    FILE_CHECKBOX = (By.XPATH, "//*[text()='Word File.doc']/parent::*/*[@class='rct-checkbox']/*")
    RESULT_PROMPT = (By.CSS_SELECTOR, "#result span:nth-of-type(1)")
    RESULT_SELECTED_FILES = (By.CSS_SELECTOR, "#result .text-success")

    def __init__(self, driver):
        self.driver = driver

    def open_home_folder(self):
        element = self.driver.find_element(*CheckboxPage.HOME_FOLDER_TOGGLE)
        element.click()
        return self
    
    def open_downloads_folder(self):
        element = self.driver.find_element(*CheckboxPage.DOWLOADS_FOLDER_TOGGLE)
        element.click()
        return self
    
    def select_file_checkbox(self):
        element = self.driver.find_element(*CheckboxPage.FILE_CHECKBOX)
        element.click()
        return self
    
    def check_if_text_prompt_appeared(self):
        prompt = self.driver.find_element(*CheckboxPage.RESULT_PROMPT)
        selected_files = self.driver.find_element(*CheckboxPage.RESULT_SELECTED_FILES)
        expected = 'You have selected : wordFile'
        actual = prompt.text + " " + selected_files.text
        assert expected == actual, "expected %s, got %s" % (expected, actual)

