import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class MCGB_Test6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_volunteerEventRegister(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://midcity-team2.herokuapp.com/")
        elem = driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[5]/a').click()
        time.sleep(0.5)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("pnalligounderpalan@unomaha.edu")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("maverick")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[3]/button/i").click()
        try:
            # attempt to find the plus button - if found, logged in
            elem = driver.find_element_by_xpath('//*[@id="clientZone"]/div/div/img')
            event_Register = True
        except NoSuchElementException:
            self.fail("Login Failed")
            assert False

        if event_Register:
            time.sleep(1)
            elem = driver.find_element_by_xpath('//a[text()="Employee Handbook"]').click()
            time.sleep(0.5)
            elem = driver.find_element_by_xpath('//input[@value="Sign up for this event"]').click()
            try:
                # attempt to find the plus button - if found, logged in
                elem = driver.find_element_by_xpath('/html/body/div/section[2]/div/div/div[1]/div/input')
                assert True
            except NoSuchElementException:
                self.fail("Event Signup Failed")
                assert False


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()