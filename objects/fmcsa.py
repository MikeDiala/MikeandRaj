from values.xpaths import carrier_xpath, all_tables_xpath
from helpers.home_page_pass import pass_fmcsa
from helpers.find_x import find_x
from helpers.date_conversion import convert_date
from values.string import default_usdot
from values.xpaths import fmcsa_carrier_page
from selenium.common.exceptions import NoSuchElementException


class FMCSA:
    def __init__(self, driver):
        self.driver = driver
        pass_fmcsa(self.driver)
        self.empty_count = 0

    def goto_usdot(self, usdot):
        entry_box = self.driver.instance.find_element_by_xpath(fmcsa_carrier_page['usdot_box'])
        entry_box.clear()
        entry_box.send_keys(usdot)
        self.driver.instance.find_element_by_xpath(fmcsa_carrier_page['search_button']).click()

    def get_carrier_data(self, usdot_num=None):
        try:
            self.goto_usdot(usdot_num)
            all_tables = {}
            carrier_data = {'USDOT': usdot_num}
            for k, v in all_tables_xpath.items():
                all_tables[k] = self.driver.instance.find_element_by_xpath(v).text.splitlines()

            for k, v in carrier_xpath.items():
                carrier_data[k] = self.driver.instance.find_element_by_xpath(v).text.strip()
                if k == 'mcs_150':
                    carrier_data[k] = convert_date(carrier_data[k])

            carrier_data['operation_classification'] = find_x(all_tables['table1'][14:25])
            carrier_data['carrier_operation'] = find_x(all_tables['table1'][26:29])
            carrier_data['cargo_carried'] = find_x(all_tables['table1'][30:])
            carrier_data['mobile_number'] = ''
            carrier_data['email_address'] = ''
            carrier_data['contact_name'] = ''

            return carrier_data
        except NoSuchElementException:
            return False

    def get_carrier_data_range(self, db=None, start=None, stop=None):
        if start is None:
            start = default_usdot
        if stop is None:
            stop = default_usdot + 10

        range_carrier_data = []
        for num in range(start, stop+1):
            ret_carrier_data = {}
            ret_carrier_data = self.get_carrier_data(num)

            if ret_carrier_data:
                range_carrier_data.append(ret_carrier_data)
            else:
                pass_fmcsa(self.driver)
        return range_carrier_data

    def get_carrier_data_range_writedb(self, db, start=None, stop=None):
        if start is None:
            start = default_usdot
        if stop is None:
            stop = start + 40000

        for num in range(start, stop+1):
            ret_carrier_data = {}
            if not db.check_if_usdot_in_db(num):
                ret_carrier_data = self.get_carrier_data(num)
                if ret_carrier_data:
                    self.empty_count = 0
                    db.write_to_db(ret_carrier_data)
                else:
                    pass_fmcsa(self.driver)
                    self.empty_count += 1

                if self.empty_count > 10:
                    return
            else:
                print("This record already in DB", num)
