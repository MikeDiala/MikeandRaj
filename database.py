import sqlite3
import csv
from values.string import db_name
from datetime import datetime, timedelta
from helpers.address_conversion import parse_address


class DB:
    def __init__(self):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.today = datetime.today()


    def write_to_db(self, data):
        print(data)
        self.cursor.execute("INSERT or IGNORE INTO usdot VALUES (:USDOT, :MC_docket, "
                            ":entity_type,:operating_status, :out_of_service,:legal_name, "
                            ":dba_name, :contact_name,:physical_address, :business_phone, "
                            ":mobile_number, :email_address, :mailing_address, :power_units, "
                            ":drivers,:mcs_150, :Mileage_Year, :operation_classification, "
                            ":carrier_operation, :cargo_carried)", data)

        self.conn.commit()

    def get_usdot(self, num):
        self.cursor.execute("SELECT * from usdot where USDOT=?", (num,))
        ret = self.cursor.fetchall()
        ret = []

    def check_if_usdot_in_db(self, num):
        self.cursor.execute("SELECT * from usdot WHERE USDOT=?", (num,))
        res = bool(self.cursor.fetchone())
        return res

    def get_last_record(self):
        self.cursor.execute("SELECT * FROM usdot ORDER BY USDOT ASC")
        ret = self.cursor.fetchall()
        max_usdot = max(ret, key=lambda x:x[0])
        return max_usdot[0]

    def get_all_records(self):
        self.cursor.execute("SELECT * from usdot")
        ret = self.cursor.fetchall()
        return ret

    def update_record_with_sms_results(self, values, usdot):
        self.cursor.execute("UPDATE usdot SET mobile_number=?, email_address=?, contact_name=? WHERE "
                            "USDOT=?", (values['mobile_number'], values['email_address'],
                                        values['contact_name'], usdot,))
        self.conn.commit()

    def get_records_w_no_sms_data(self, start_date, end_date):
        self.cursor.execute("SELECT * from usdot WHERE email_address='' AND mcs_150 BETWEEN ? and ?", (start_date, end_date,))
        ret = self.cursor.fetchall()
        return ret

    def get_records_for_state(self, state):
        self.cursor.execute("SELECT * from usdot WHERE mailnig_address LIKE ?", ('%{} %'.format(state),))
        ret = self.cursor.fetchall()
        return ret

    def get_records_date_range(self, start_date, end_date):
        self.cursor.execute("SELECT * FROM usdot WHERE mcs_150 BETWEEN ? AND ?", (start_date, end_date,))
        ret = self.cursor.fetchall()
        return ret

    def get_records_for_anhdy(self, state, days=None):
        if days:
            num_of_days = self.today - timedelta(days=days)
        else:
            num_of_days = 100000

        self.cursor.execute("SELECT * from usdot WHERE mailnig_address LIKE ? AND entity_type=? AND "
                            "(operating_status=? OR operating_status=? OR operating_status=?) "
                            "AND operation_classification=? AND (carrier_operation=? OR carrier_operation=?) "
                            "AND mcs_150 BETWEEN ? and ?",
                            ('%{} %'.format(state),'CARRIER', 'ACTIVE', 'AUTHORIZED FOR HIRE',
                             'NOT AUTHORIZED','Auth. For Hire, ', 'Interstate, ', 'Intrastate Only (Non-HM), ',
                             num_of_days.strftime('%Y-%m-%d'), self.today.strftime('%Y-%m-%d')))
        ret = self.cursor.fetchall()
        return ret

    def write_db_to_csv(self, data, file_name):
        fp = open('./data/' + file_name + '.csv', 'w')
        myFile = csv.writer(fp, lineterminator='\n')
        myFile.writerow(['USDOT',
                         'MC_no', 'MCS 150', 'Entity_type', 'Operating_status',
                         'Out_of_service', 'Legal_name', 'Dba_name',
                         'Contact_name', 'Physical_address', 'Physical_city', 'Physical_state', 'Physical_zip', 'Business_phone',
                         'Mobile_number', 'Email_address', 'Mailing_address', 'Mailing_city', 'Mailing_state',
                         'Mailing_zip', 'Power units',
                         'Drivers', 'Mileage (Year)',
                         'Operation_classification', 'Carrier_operation', 'Cargo_carried'])
        for row in data:
            line_data = [i for i in row]
            pa, pc, ps, pz = parse_address(line_data[8])
            ma, mc, ms, mz = parse_address(line_data[12])

            pz = pz.split('-')[0]
            mz = mz.split('-')[0]

            line_data[8] = pa
            line_data.insert(9, pc)
            line_data.insert(10, ps)
            line_data.insert(11, pz)


            line_data[15] = ma
            line_data.insert(16, mc)
            line_data.insert(17, ms)
            line_data.insert(18, mz)

            line_data[23] = line_data[23].replace(',' ,'')
            line_data[24] = line_data[24].replace('Only (Non-HM)', '').replace(',','')

            line_data.insert(2, line_data.pop(21))

            # parse_data.insert(14, parse_data[13].split().pop())
            myFile.writerow(line_data)
        fp.close()
