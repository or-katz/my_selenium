#!/home/or/SeleniumOnJenkins/bin/python

from selenium import webdriver
from time import sleep

chromedriver_path = "/home/or/SeleniumOnJenkins/chromedriver"
chrome_browser = webdriver.Chrome(executable_path=chromedriver_path)

url = 'https://translate.google.com/?sl=iw&tl=en&op=translate'
translate_xpath = '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea'

chrome_browser.get(url)
translate_element = chrome_browser.find_element_by_xpath(translate_xpath)
translate_element.send_keys('שלום עולם')
sleep(3)
translate_results = chrome_browser.find_element_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span').text
print(translate_results)
chrome_browser.close()
