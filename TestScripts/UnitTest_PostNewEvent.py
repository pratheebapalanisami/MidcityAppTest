import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class MCGB_Test5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_postEvent(self):

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
            post_event = True
        except NoSuchElementException:
            self.fail("Login Failed")
            assert False

        if post_event:
            time.sleep(0.5)
            elem = driver.find_element_by_id("clientZone").click()
            time.sleep(0.5)
            elem = driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[4]/div/a[3]').click()
            time.sleep(0.5)
            elem = driver.find_element_by_id("title")
            elem.send_keys("Employee Handbook")
            elem = driver.find_element_by_id("text")
            elem.send_keys("Help Seeds of Awareness improve transparency and accountability with clarified rights, policies, and other expectations in a new or revised employee handbook.")
            elem = driver.find_element_by_id("location")
            elem.send_keys("Omaha")
            elem = driver.find_element_by_xpath('//*[@id="event-main-form"]/div[5]/div/div/button/div/div/div').click()
            time.sleep(0.5)
            elem = driver.find_element_by_xpath('//*[@id="event-main-form"]/div[5]/div/div/div/div/ul/li[3]/a').click()
            elem = driver.find_element_by_id("validity")
            elem.send_keys("11/25/2019")
            elem = driver.find_element_by_id("volunteers_required")
            elem.send_keys("4")

            elem = driver.find_element_by_id("company_name")
            elem.send_keys("ABC")
            elem = driver.find_element_by_id("company_description")
            elem.send_keys("ABC is looking for bono professionals to donate their skills through 1-hour phone calls and/or fully fledged projects.")
            elem = driver.find_element_by_xpath('//*[@id="event-main-form"]/div[6]/div/div[6]/div/div/label/input').click()
            elem = driver.find_element_by_xpath('//*[@id="event-main-form"]/div[6]/div/div[7]/div/button').click()
            time.sleep(0.5)
            try:
               # find the 'edit' pencil icon - if post added, edit pate is displayed
               elem = driver.find_element_by_xpath('/html/body/div/section[2]/div/div/div[1]/a')
               assert True
            except NoSuchElementException:
                self.fail("Post not successfull")
                assert False


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()