import pytest
from selenium import webdriver
from Pages.Login import LoginPage
from Tests.conf import setUp
from Utilities.readproperties import readConfig
from Utilities.customLogger import LogGen

import time

class Test_Login:

    baseUrl = readConfig.getApplicationurl()
    username = readConfig.getUsername()
    password = readConfig.getPassword()

    logger=LogGen.loggen()

    def test_homePageTitle(self,setUp):

        self.logger.info("******"+self.test_homePageTitle.__name__+"******")
        self.logger.info("******" + self.test_homePageTitle.__name__ + "******")

        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        actual_title = self.driver.title


        if actual_title == "OrangeHRM":
            assert True
            self.logger.info(self.test_homePageTitle.__name__ + "****** Passed")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + self.test_homePageTitle.__name__+".png")
            self.logger.info(self.test_homePageTitle.__name__ + "****** Failed")
            self.driver.close()
            assert False

    def test_login(self,setUp):

        # self.logger.info("******" + self.test_login().__name__ + "******")
        # self.logger.info("******" + self.test_login().__name__ + "******")

        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        time.sleep(10)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title=self.driver.title


        if act_title=="OrangeHRM":
            assert True
            self.logger.info(self.test_login().__name__ + "****** Passed")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + self.test_login().__name__ + ".png")
            self.logger.info(self.test_login().__name__ + "****** Failed")
            self.driver.close()
            assert False


