import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class MCGB_Test8(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_markAttendance(self):

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
            time.sleep(0.5)
            elem = driver.find_element_by_id("clientZone")
            mark_attendance = True
        except NoSuchElementException:
            self.fail("Login Failed")
            assert False

        if mark_attendance:
            time.sleep(0.5)
            elem = driver.find_element_by_id("clientZone").click()
            time.sleep(0.5)
            elem = driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[4]/div/a[2]').click()
            elem = driver.find_element_by_xpath('//a[text()="Update Attendance"]').click()
            elem = driver.find_element_by_id("id_attendance").click()
            elem = driver.find_element_by_xpath('/ html / body / div / form / button').click()
            try:
               elem = driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[1]/a')
               assert True
            except NoSuchElementException:
                self.fail("Mark Attendance not successfull")
                assert False


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()