import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class MCGB_Test9(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_volunteerMyEvent(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://midcity-team2.herokuapp.com/")
        elem = driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[5]/a').click()
        time.sleep(0.5)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("dfaisal@unomaha.edu")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("instructor1a")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[3]/button/i").click()
        try:
            elem = driver.find_element_by_xpath('//*[@id="clientZone"]/div/div/img')
            my_event = True
        except NoSuchElementException:
            self.fail("Login Failed")
            assert False

        if my_event:
            elem = driver.find_element_by_id('clientZone').click()
            time.sleep(0.5)
            elem = driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[4]/div/a[1]').click()
            time.sleep(0.5)
            try:
                # attempt to find the plus button - if found, logged in
                elem = driver.find_element_by_xpath('/html/body/div/section[1]/div/div/div/h1')
                assert True
            except NoSuchElementException:
                self.fail("My Event Failed")
                assert False


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()