from bs4 import BeautifulSoup
from selenium import webdriver
import time

def login():
    url = "TARGET_URL"
    username = 'USERNAME_GOES_HERE'
    password = 'PASSWORD_GOES_HERE'

    #loaded Firefox driver with <CODE>brew install geckodriver</CODE> and then <CODE>which geckodriver</CODE>
    driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')

    driver.get(url)

    driver.find_element_by_id('userNameAL').send_keys(username)
    time.sleep(1)
    driver.find_element_by_name('passwordAL').send_keys(password)
    time.sleep(2)
    submit = driver.find_element_by_xpath('//*[@id="loginMobileForm"]/div[4]/div/button')
    time.sleep(1)
    submit.location_once_scrolled_into_view
    time.sleep(1)
    submit.click()
