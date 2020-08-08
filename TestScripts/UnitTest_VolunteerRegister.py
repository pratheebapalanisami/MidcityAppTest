import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class MCGB_Test1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_signup(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://midcity-team2.herokuapp.com/")
        elem = driver.find_element_by_id("pages").click()
        elem = driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[4]/div/a[1]').click()
        time.sleep(0.5)
        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys("Pratheeba")
        elem = driver.find_element_by_id("id_last_name")
        elem.send_keys("Nalligounder Palanisami")
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("pnalligounderpalan@unomaha.edu")
        elem = driver.find_element_by_id("id_password1")
        elem.send_keys("maverick")
        elem = driver.find_element_by_id("id_password2")
        elem.send_keys("maverick")
        elem = driver.find_element_by_id("female").click()
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[7]/button").click()
        try:
            # attempt to find the plus button - if found, logged in
            elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[3]/button")
            assert True
        except NoSuchElementException:
            self.fail("Signup Failed")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()