import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class MCGB_Test7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_organizationDashboard(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://midcity-team2.herokuapp.com/")
        elem = driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[5]/a').click()
        time.sleep(0.5)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("mdc@gmail.com")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("maverick")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[3]/button/i").click()
        try:
            # attempt to find the plus button - if found, logged in
            time.sleep(0.5)
            elem = driver.find_element_by_id("clientZone")
            organization_dashboard = True
        except NoSuchElementException:
            self.fail("Login Failed")
            assert False

        if organization_dashboard:
            time.sleep(0.5)
            elem = driver.find_element_by_id("clientZone").click()
            time.sleep(0.5)
            elem = driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[4]/div/a[1]').click()

            try:
               elem = driver.find_element_by_xpath('/html/body/div/section[1]/div/div/div/h1')
               assert True
            except NoSuchElementException:
                self.fail("Organization dashboard not successfull")
                assert False


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()