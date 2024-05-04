from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from time import sleep
from constants.topMenuConstants import *
import pytest
from selenium.webdriver.common.alert import Alert

class Test_topMenu:   
    def login_page(self):
        self.driver = webdriver.Chrome()
        self.driver.get(LOGIN_URL)
        self.driver.maximize_window() 
        
    def valid_login(self):
        self.login_page()
        email = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.NAME, userEmail)))
        email.send_keys("tobetopair5@gmail.com")
        sleep(2)
        password = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.NAME, userPassword)))
        password.send_keys("*******")
        loginButton = self.driver.find_element(By.XPATH, LOGIN_XPATH)
        loginButton.click()
        sleep(2)
        
    def test_topMenu(self):
        self.valid_login()
        myProfileButton = self.driver.find_element(By.XPATH, myProfile)
        myProfileButton.click()
        sleep(3)
        reviewsButton = self.driver.find_element(By.XPATH, reviews)
        reviewsButton.click()
        sleep(3)
        catalogButton = self.driver.find_element(By.XPATH, catalog)
        catalogButton.click()
        sleep(3)
        calendarButton = self.driver.find_element(By.XPATH, calender)
        calendarButton.click()
        sleep(3)
        homePageButton = self.driver.find_element(By.XPATH, homePage)
        homePageButton.click()
        sleep(3)
        istanbulKodluyorButton = self.driver.find_element(By.XPATH, istanbul_kodluyor)
        istanbulKodluyorButton.click()
        sleep(3)
        #istanbulkodluyor ekranında sayfa sonlanır.