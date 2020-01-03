from webdriver import Driver
from objects.fmcsa import FMCSA
from database import DB
from objects.sms_results import SMSResults
from helpers.email import email
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sms_res", help="runs SMS Results", action='store_true')
    parser.add_argument("--fmcsa", help="runs FMCSA", action='store_true')
    parser.add_argument("--email_records", help="2 arguments, first is num of days, second is the email", nargs=2)
    args = parser.parse_args()

    if args.fmcsa:
        fmcsa()
    if args.sms_res:
        get_sms()
    if args.email_records:
        get_records(args.email_records[0], args.email_records[1])

def fmcsa():
    db = DB()
    driver = Driver()
    fmcsa = FMCSA(driver)
    fmcsa.get_carrier_data_range_writedb(db, start=db.get_last_record())
    db.conn.close()

def get_sms():
    db = DB()
    driver = Driver()
    smsres = SMSResults(driver)
    smsres.get_sms_results_writedb(db)
    db.conn.close()


def get_records(days, email_name):
    days = int(days)
    db = DB()
    ret = db.get_records_for_anhdy('CA', days=days)
    db.write_db_to_csv(ret, 'CA')
    ret = db.get_records_for_anhdy('AZ', days=days)
    db.write_db_to_csv(ret, 'AZ')
    ret = db.get_records_for_anhdy('TX', days=days)
    db.write_db_to_csv(ret, 'TX')

    email("./data/AZ.csv", email_name)
    email("./data/CA.csv", email_name)
    email("./data/TX.csv", email_name)

    db.conn.close()

if __name__ == "__main__":
    main()
