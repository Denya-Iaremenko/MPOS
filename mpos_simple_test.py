import unittest
from appium import webdriver
import PageObjects


class AppiumTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = 'iPhone Simulator'
        # desired_caps['app'] = PATH('../../apps/UICatalog.app.zip')!!!

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

        ok_btnn = self.driver.find_element_by_xpath(PageObjects.PageObject.ok_btn)
        ok_btnn.click()

    def test_2_login(self):
        login_field = self.driver.find_element_by_xpath(PageObjects.PageObject.login_filed)
        login_field.clear()
        login_field.send_keys("deni")

        pss_field = self.driver.find_element_by_xpath(PageObjects.PageObject.secure_password_field)
        pss_field.clear()
        pss_field.send_keys("Test11")

        login_button = self.driver.find_element_by_xpath(PageObjects.PageObject.login_btn)
        login_button.click()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTests)
    unittest.TextTestRunner(verbosity=2).run(suite)