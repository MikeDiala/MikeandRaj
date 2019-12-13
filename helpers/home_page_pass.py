from values.xpaths import fmcsa_front_page
from values.string import default_usdot
from values.string import fmcsa_home_page
from values.string import insurance_home_page
from values.xpaths import insurance_xpath
from time import sleep


def pass_fmcsa(driver, usdot_num= None):
    driver.navigate(fmcsa_home_page)
    entry_box = driver.instance.find_element_by_xpath(fmcsa_front_page['usdot_value'])
    entry_box.clear()
    if usdot_num:
        entry_box.send_keys(usdot_num)
    else:
        entry_box.send_keys(default_usdot)
    driver.instance.find_element_by_xpath(fmcsa_front_page['search_button']).click()


def pass_insurance(driver):
    driver.navigate(insurance_home_page)
    driver.instance.find_element_by_xpath(insurance_xpath['carrier_search']).click()
    sleep(1)
    driver.instance.find_element_by_xpath(insurance_xpath['go_button']).click()
