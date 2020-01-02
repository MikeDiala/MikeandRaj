from values.xpaths import sms_xpath
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime, timedelta
from values.string import sms_date_search_range


class SMSResults:
    def __init__(self, driver):
        self.driver = driver
        self.link = 'https://ai.fmcsa.dot.gov/SMS/Carrier/{}/Overview.aspx?FirstView=True'
        self.waittime = 1
        self.today = datetime.today()

    def get_sms_result_one(self, usdot):
        try:
            self.driver.navigate(self.link.format(usdot))
            self.driver.instance.find_element_by_xpath(sms_xpath['carrier_details']).click()
            sleep(self.waittime)
            elems = self.driver.instance.find_elements_by_xpath(sms_xpath['company_details'])

            ret = {}
            for i in elems:
                line_item = i.text.splitlines()
                if line_item[0] == 'Telephone:':
                    if len(line_item) > 1:
                        ret['mobile_number'] = line_item[1]
                    else:
                        ret['mobile_number'] = ''
                elif line_item[0] == 'Email:':
                    if len(line_item) > 1:
                        ret['email_address'] = line_item[1]
                    else:
                        ret['email_address'] = ''
                elif line_item[0] == 'Legal Name:':
                    if len(line_item) > 1:
                        ret['contact_name'] = line_item[1]
                    else:
                        ret['contact_name'] = ''
            return ret
        except NoSuchElementException:
            return False

    def get_sms_results_writedb(self, db):
        num_of_days = self.today - timedelta(days=sms_date_search_range)

        all_records = db.get_records_w_no_sms_data(num_of_days.strftime('%Y-%m-%d'), self.today.strftime('%Y-%m-%d'))

        for i, rec in enumerate(all_records):
            ret = self.get_sms_result_one(rec[0])
            if ret:
                db.update_record_with_sms_results(ret, rec[0])
                print("updating record " + str(i) + " / " + str(len(all_records)))
            else:
                print("updating record but no data " + str(i) + " / " + str(len(all_records)))
                pass
