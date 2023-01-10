from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage():

    username_txtbox = "username"
    password_txtbox = "password"
    submit_button   = "//button"

    def __init__(self,driver):
        self.driver = driver

    def setUsername(self,usernm):
        self.ele = self.driver.find_element(By.NAME, self.username_txtbox)
        self.ele.send_keys(usernm)

    def setPassword(self,pwd):
        self.ele = self.driver.find_element(By.NAME, self.password_txtbox)
        self.ele.send_keys(pwd)

    def clickLogin(self):
        self.element = self.driver.find_element(By.XPATH, self.submit_button)
        self.element.click()