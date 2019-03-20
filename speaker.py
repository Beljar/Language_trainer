import selenium
import pychrome
import requests, os, bs4
import sys
import time
from selenium import webdriver
write = sys.stdout.write
from selenium.webdriver.common.keys import Keys
import sqlite3
import os
import time

class Speaker:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('log-level=3')
        # set the window size
        options.add_argument('window-size=1200x600')
        self.browser = webdriver.Chrome("C:/Python36/selenium/webdriver/chrome/chromedriver.exe", chrome_options=options)
    def say(self, word):
        url = 'https://translate.google.com/#en/ru/' + word              # starting url
        self.browser.get(url)
        #sound_btn = self.browser.find_element_by_id('gt-src-listen')
        sound_btn = self.browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[5]/div[3]/div[2]")
        sound_btn.click()

