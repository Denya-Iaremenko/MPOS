import unittest
from appium import webdriver
import PageObjects
import os
import time


class AppiumTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = 'iPhone Simulator'


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(60)

    def tearDown(self):
        self.driver.quit()

    def test_1_login_negative(self):
        login_field = self.driver.find_element_by_xpath(PageObjects.PageObject.login_filed)
        login_field.send_keys("fail")

        pss_field = self.driver.find_element_by_xpath(PageObjects.PageObject.password_field)
        pss_field.send_keys("fail")

        login_button = self.driver.find_element_by_xpath(PageObjects.PageObject.login_btn)
        login_button.click()

        #lgn_error = self.driver.find_element_by_xpath(PageObjects.PageObject.login_error)
        #lgn_er_atr = lgn_error.get_attribute()
        #lgn_error_text = self.driver.find_element_by_xpath(PageObjects.PageObject.login_error_text)
        #error_text = lgn_error_text.get_attribute()
        #assert (lgn_er_atr == "Login error")
        #assert (error_text == "Please check your credentials.")
        self.driver.get_screenshot_as_file("Message_login_negative.png")
        os.rename("/Users/diaremenko/PycharmProjects/new_project/Message_login_negative.png", "/Users/diaremenko/Desktop/Message_login_negative.png")

        ok_btnn = self.driver.find_element_by_xpath(PageObjects.PageObject.ok_btn)
        ok_btnn.click()

    #def test_2_login(self):

        login_field = self.driver.find_element_by_xpath(PageObjects.PageObject.login_filed)
        login_field.clear()
        login_field.send_keys("deni")


        pss_field = self.driver.find_element_by_xpath(PageObjects.PageObject.secure_password_field)

        #pss_field = self.driver.find_element_by_xpath(PageObjects.PageObject.secure_password_field)

        pss_field.clear()
        pss_field.send_keys("Test11")

        login_button = self.driver.find_element_by_xpath(PageObjects.PageObject.login_btn)
        login_button.click()

    #def test_3_add_item_to_cart(self):
        cart_icon = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[13]')
        cart_icon.click()
        searsh_bar = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIASearchBar[1]')
        searsh_bar.send_keys("item5")

        item_5 = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]')
        item_5.click()

        self.driver.hide_keyboard()

        #checkout_button = self.driver.find


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTests)
    unittest.TextTestRunner(verbosity=2).run(suite)