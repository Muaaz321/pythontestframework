import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setUp():
    serv_obj=Service(".\\Drivers\\chromedriver_win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    return driver