import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
#from userInfo import newPassword, passwordConfirmation, falsePassword, password, passwordAgain
import pytest
from constants.resetPasswordConstants import *

class Test_Tobeto_Platform_Password_Forget():

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(MAIL_URL)
        self.driver.maximize_window()

    def teardown_method(self): 
        self.driver.quit()
   
    def waitForElementVisible(self, locator, timeout = 5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    #On Hazirlik
    def pre_condition_test_reset_password_forget(self, newPassword, passwordConfirmation):
        passwordInput = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, new_password_xpath)))
        passwordInput.send_keys(newPassword)
        passwordConfirmationInput = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, password_confirmation_xpath)))
        passwordConfirmationInput.send_keys(passwordConfirmation)

        newPasswordButton = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, new_password_send_button_xpath)))
        newPasswordButton.click()

    #Case 3: Sifre yenileme
    def test_reset_password_forget(self):
        self.pre_condition_test_reset_password_forget(newPassword, passwordConfirmation)
        sleep(2)

        resetSuccesfulAlert = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, password_reset_succesful_alert_path)))
        assert resetSuccesfulAlert.text == resetSuccesfulAlertText

    #Case 4: Sifrelerin eslesmemesi
    @pytest.mark.parametrize("newPassword, passwordConfirmation", [(falsePassword, newPassword), (newPassword, falsePassword)])
    def test_reset_passwords_not_match(self, newPassword, passwordConfirmation):
        passwordInput = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, new_password_xpath)))
        passwordInput.send_keys(newPassword)
        passwordConfirmationInput = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, password_confirmation_xpath)))
        passwordConfirmationInput.send_keys(passwordConfirmation)

        newPasswordButton = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, new_password_send_button_xpath)))
        newPasswordButton.click()
        sleep(2)

        passwordsNotMatch = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, passwords_not_match_path)))
        assert passwordsNotMatch.text == passwordsNotMatchText

    #Case 5: Mevcut sifrenin girilmesi FAIL
    @pytest.mark.parametrize("password, passwordAgain", [(password, passwordAgain)])
    def test_reset_current(self, password, passwordAgain):
        passwordInput = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, new_password_xpath)))
        passwordInput.send_keys(password) #mevcut sifre
        passwordConfirmationInput = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, password_confirmation_xpath)))
        passwordConfirmationInput.send_keys(passwordAgain)

        newPasswordButton = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, new_password_send_button_xpath)))
        newPasswordButton.click()
        sleep(2)

        currentPasswordFail = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, currentPasswordFailText)))
        assert currentPasswordFail.text == currentPasswordFailText

    
    