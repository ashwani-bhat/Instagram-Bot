import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, psk):
        self.username = username
        self.psk = psk
        self.driver = webdriver.Edge()    # use any webdriver [ Edge, FireFox, Chrome ] 

    def closeBrowser(self):
        self.driver.close()
    
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)
        username_element = driver.find_element_by_xpath("//input[@name='username']")
        username_element.clear()
        username_element.send_keys(self.username)
        psk_element = driver.find_element_by_xpath("//input[@name='password']")
        psk_element.clear()
        psk_element.send_keys(self.psk)
        psk_element.send_keys(Keys.RETURN)
        time.sleep(3)

    def likePhoto(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
        for i in range(1, 3):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(2)

        # searching for picture link
 
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs if hashtag in href]
        print(hashtag + 'photos: '+ str(len(pic_hrefs)))
 
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            try:
                driver.find_element_by_link_text("Like").click()
                time.sleep(18)
            except Exception as e:
                time.sleep(2)

username = #write your instagram username
password = #write your instagram password
bot = InstagramBot(username, password)
bot.login()
hashtags = ['inspiration', 'motivation', 'love']   #list the hashtags
for tag in hashtags:
    bot.likePhoto(tag) 

