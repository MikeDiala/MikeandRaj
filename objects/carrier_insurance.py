from values.xpaths import insurance_xpath
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from helpers.home_page_pass import pass_insurance


class Insurance:
    def __init__(self, driver):
        self.driver = driver
        pass_insurance(self.driver)

    def get_recaptcha_id(self):
        recaptcha = self.driver.instance.find_element_by_xpath(insurance_xpath['captcha']).click()
        ret = recaptcha.get_attribute("data-sitekey")





