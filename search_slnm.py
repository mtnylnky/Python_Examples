from selenium import webdriver
import time

enterword=input("Enter word: ")
#Firefox: webdriver.Firefox() - Chrome: webdriver.Chrome()
browser=webdriver.Firefox(executable_path=r"gecko_driver_path")
browser.get('https://www.website.com')

time.sleep(3)
username=browser.find_element_by_xpath("website_input_xpath")
username.send_keys(enterword)
time.sleep(1)
login=browser.find_element_by_name("web_site_btn_name")
login.click()
time.sleep(5)
browser.quit()
