#!D:\Python\WPy64-3720\python-3.7.2.amd64\pythonw.exe
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 21:45:21 2019

@author: KC
"""
# A simple program to go to a website and login with username and password


def website_login(url):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    profile = webdriver.FirefoxProfile()
    profile.accept_untrusted_certs = True

    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-username")))
    username = driver.find_element_by_id("login-username")
    password = driver.find_element_by_name("password")
    
    username.send_keys("username")
    password.send_keys("password")
    
    driver.find_element_by_xpath('//button[text()="Sign In"]').click()

website_login('https://www.my.website.edu/')