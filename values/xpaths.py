all_tables_xpath = {
    'table1' : '/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[1]',
    'table2' : '/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[3]',
    'table3' : '/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[4]',
    'table4' : '/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[6]',
    'table5' : '/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[7]',
    'table6' : '/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[9]'
}
carrier_xpath = {
    'entity_type' : '/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[1]/table/tbody/tr[2]/td',
    'operating_status' : '/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[1]/table/tbody/tr[3]/td[1]',
    'out_of_service' : '/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[1]/table/tbody/tr[3]/td[2]',
    'legal_name' : '/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[1]/table/tbody/tr[4]/td',
    'dba_name' : '/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[1]/table/tbody/tr[5]/td',
    'physical_address' : '/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[1]/table/tbody/tr[6]/td',
    'business_phone' : '/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[1]/table/tbody/tr[7]/td',
    'mailing_address' : '/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[1]/table/tbody/tr[8]/td',
    'power_units' : '/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[1]/table/tbody/tr[11]/td[1]',
    'drivers' : '/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[1]/table/tbody/tr[11]/td[2]',
    'MC_docket' : '/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[1]/table/tbody/tr[10]/td[1]',
    'mcs_150'  : '/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[1]/table/tbody/tr[12]/td[1]',
    'Mileage_Year': '/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[1]/table/tbody/tr[12]/td[2]'
}
fmcsa_front_page = {
    'usdot_value': '//*[@id="4"]',
    'search_button': '/html/body/form/p/table/tbody/tr[4]/td/input'
}
fmcsa_carrier_page = {
    'usdot_box': '//*[@id="4"]',
    'search_button': '/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/form/p/table/tbody/tr[4]/td/input'
}
sms_xpath = {
    'contact_name'    : '//*[@id="regBox"]/ul[1]/li[1]/span',
    'carrier_details' : '//*[@id="CarrierRegistration"]/a[1]',
    'company_details' : '//*[@id="regBox"]/ul[1]/li'
}
insurance_xpath = {
    'drop_down': '//*[@id="menu"]',
    'carrier_search': '//*[@id="menu"]/option[4]',
    'go_button': '/html/body/font/table[1]/tbody/tr/td/div/div/table/tbody/tr/td/form/input[1]',
    'captcha': '//html/body/font/center[1]/form/table[2]/tbody/tr/td/div'


}