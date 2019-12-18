import time
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

options = Options()
driver = webdriver.Chrome(chrome_options=options)
sleep_time = 1
path = 'https://www.yellowpages.com/search?search_terms=semi%20car%20wash&geo_location_terms=TX&page='

xpath = {
	'title': '//*[@id="main-header"]/article/div',
	'address' : '//*[@id="main-header"]/article/section[2]/div[1]/h2',
	'phone'   :  '//*[@id="main-header"]/article/section[2]/div[1]/p',
	'years_in_biz' : '//*[@id="main-header"]/article/section[2]/div[2]/div/div'
}

f  = open('./data/clients/car_wash_TX.csv', 'w')
writer = csv.DictWriter(f, fieldnames=['title', 'address','phone','years_in_biz','email','website'], lineterminator = '\n')
writer.writeheader()


def run(page):
	driver.get(path+str(page))
	time.sleep(sleep_time)
	elements = driver.find_elements_by_class_name('result')
	
	for i in range(0,len(elements)):
		record  = {}
		try:
			elements = driver.find_elements_by_class_name('result')
			elements[i].click()
		except:
			pass
		time.sleep(sleep_time)
		
		for key, val in xpath.items():
			try:
				record[key] = driver.find_element_by_xpath(val).text
			except:
				record[key] = ''

		try:
			email = driver.find_element_by_class_name('email-business')
			record['email'] = email.get_attribute('href').split('mailto:')[1]
		except:
			record['email'] = ''
		try:
			website = driver.find_element_by_class_name('website-link')
			record['website'] = website.get_attribute('href')
		except:
			record['website'] = ''

		print(record)
		writer.writerow(record)
		driver.back()
		time.sleep(sleep_time)
		time.sleep(sleep_time)

for page in range(10,100):
	run(page)