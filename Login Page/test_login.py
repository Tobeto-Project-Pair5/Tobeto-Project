import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
#from userInfo import email, password, falseEmail, falsePassword, verificationEmail, verificationPassword
import pytest
from constants.loginConstans import *

class Test_Tobeto_Platform_Login_Test():

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(LOGIN_URL)
        self.driver.maximize_window()

    def teardown_method(self): 
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout = 5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def pre_condition_method_login(self, email, password): #on kosul 
        emailInput = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, login_checkbox_email_xpath)))
        emailInput.send_keys(email)
        passwordInput = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, login_checkbox_password_xpath)))
        passwordInput.send_keys(password)

        loginButton = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, login_button_xpath)))
        loginButton.click()

    #Case 1 : Basarili giris yapildiginda
    def test_successful_login(self):
        self.pre_condition_method_login(email, password)
        sleep(4)

        succesfulLoginMessage = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, successful_login_message_xpath)))
        assert succesfulLoginMessage.text == succesfulLoginMessageText  

    #Case 2 : E-posta veya sifre girilmediginde
    @pytest.mark.parametrize("email, password", [("", password), (email, ""), ("", "")])
    def test_passing_empty(self, email, password):
        self.pre_condition_method_login(email, password)
        sleep(4)

        requiredField = WebDriverWait(self.driver,2).until(EC.visibility_of_element_located((By.XPATH, required_field_xpath)))
        assert requiredField.text == requiredFieldText

    #Case 3 : E-posta veya sifre yanlis girildiginde
    @pytest.mark.parametrize("email, password", [(falseEmail, falsePassword), (email, falsePassword), (falseEmail, password)])
    def test_false_login(self, email, password):
        emailInput = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, login_checkbox_email_xpath)))
        emailInput.send_keys(email)
        passwordInput = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, login_checkbox_password_xpath)))
        passwordInput.send_keys(password)

        loginButton = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, login_button_xpath)))
        loginButton.click()   
        sleep(2)
        
        invalidEmailPasswordAlert = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, invalid_email_password_alert))) 
        assert invalidEmailPasswordAlert.text == invalidEmailPasswordAlertText

    #Case 4: Dogrulanmamis e-posta uyarisi
    def test_verification_link_login(self):
        self.pre_condition_method_login(verificationEmail, verificationPassword)
        sleep(4)

        unverifiedEmail = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, unverified_email_xpath)))
        assert unverifiedEmail.text == unverifiedEmailText
        
        unverifiedEmailAlert = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, unverified_email_alert_xpath)))
        assert unverifiedEmailAlert.text == unverifiedEmailAlertText 
    
