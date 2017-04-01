__author__ = 'BernardoGO'


import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.proxy import *
import sys

USERNAME = "ElCorreioEletronico@gmail.com"
PASSWORD = "ElPasswordo"
START_FROM = 1
driver = None
def loadInviteURL():

    straturl = "https://www.overleaf.com/space#!invites"
    try:
        driver.get(straturl)
    except:
        #
        driver.execute_script("window.stop();")
        print ("TIMED OUT")
    print ("running")
    time.sleep(2)

def invite(emails):
    global START_FROM
    count = 0
    for email in emails.split(","):
        if count < START_FROM:
            count += 1
            continue
        invited = False
        while not invited:
            try:
                driver.find_element_by_xpath('//*[@id="referral_referree_email"]').send_keys(email)
                driver.find_elements_by_xpath('//*[@id="new_referral"]/div/div[3]/input')[0].click()
                time.sleep(2)
                invited = True
                count += 1
                print("Invited " + str(count))
            except:
                print("Loading invite url")
                loadInviteURL()

def main():
    print (sys.argv)
    global driver
    driver =  webdriver.Chrome()
    straturl = "https://www.overleaf.com/users/sign_in"
    try:
        driver.get(straturl)
    except:
        #
        driver.execute_script("window.stop();")
        print ("TIMED OUT")
    print ("running")
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="user_email"]').send_keys(USERNAME)#"")
    driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(PASSWORD)#"")
    driver.find_elements_by_xpath('//*[@id="new_user"]/div[1]/input[3]')[0].click()
    #text_file = open("mailList.txt", "r")
    with open('mailList.txt') as f:
        invite(str(f.read()))




main()
