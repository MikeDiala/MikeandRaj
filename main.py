from webdriver import Driver
from objects.fmcsa import FMCSA
from database import DB
from objects.sms_results import SMSResults

def main():

    db = DB()
    # driver = Driver()
    # fmcsa = FMCSA(driver)
    # fmcsa.get_carrier_data_range_writedb(db, start=db.get_last_record())

    # smsres = SMSResults(driver)
    # smsres.get_sms_results_writedb(db)

    ret = db.get_records_for_anhdy('CA', days=30)
    db.write_db_to_csv(ret, 'CA')

    db.conn.close()

if __name__ == "__main__":
    main()
