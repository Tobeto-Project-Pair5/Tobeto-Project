import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
#from userInfo import email
import pytest
from constants.forgetPasswordConstants import *

class Test_Tobeto_Platform_Password_Forget():

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(PASSWORD_FORGET_URL)
        self.driver.maximize_window()

    def teardown_method(self): 
        self.driver.quit()
   
    def waitForElementVisible(self, locator, timeout = 5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    #Case 1: Sifre sifirlama e-postasi gonderme
    def test_password_forget(self):
        emailInput = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, email_for_reset_password_path)))   
        emailInput.send_keys(email)
        
        sendButton = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, send_button_email_for_reset_password_path))) 
        sendButton.click()
        sleep(4)

        passwordResetLinkMessage = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, password_reset_link_message_path)))
        assert passwordResetLinkMessage.text == passwordResetLinkMessageText
   
    #Case 2: Girilen e-postanin gecersiz olma durumu
    def test_invalid_email(self):  
        emailInput = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, invalid_email_input_css)))   
        emailInput.send_keys("email123")
        
        sendButton = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, invalid_email_button_xpath))) 
        sendButton.click()
        sleep(4)

        invalidEmail = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, invalid_email_xpath)))
        assert invalidEmail.text == invalidEmailText
        