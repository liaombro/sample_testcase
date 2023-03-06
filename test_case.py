import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from .pages.main_page import MainPage
import time 

@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    return driver


def test_checkbox(driver):
       
    page = MainPage(driver)
    (page.open()
     .click_elements_button()
     .click_checkbox_button()
     .open_home_folder()
     .open_downloads_folder()
     .select_file_checkbox()
     .check_if_text_prompt_appeared())

