from selenium import webdriver
# from userInfo import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from constants.setttingsConstants import *
# from PIL import Image
from time import sleep
import pytest

class Test_Settings():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(LOGIN_URL)

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def valid_login(self):
        loginInputButton= self.waitForElementVisible((By.XPATH,login_input_button))
        loginInputButton.click()
        emailInput = self.waitForElementVisible((By.XPATH, email_xpath))
        emailInput.send_keys(email_tuba)
        passwordInput = self.waitForElementVisible((By.XPATH, password_xpath))
        passwordInput.send_keys(password_tuba)
        loginButton = self.waitForElementVisible((By.XPATH, login_button_xpath))
        loginButton.click()
        alert_quit = self.waitForElementVisible((By.XPATH, alert_login_text))
        alert_quit.click()
        myProfilePage = self.waitForElementVisible((By.XPATH, my_profile_page))
        myProfilePage.click()
        myProfileEdit = self.waitForElementVisible((By.CSS_SELECTOR, my_profile_edit))
        myProfileEdit.click()
        sleep(2)

    #Settings = Ayarlar
    #Ayarlar sayfasını görüntüle
    def test_settings(self):  
        self.valid_login()
        settingsButton = self.waitForElementVisible((By.XPATH, settings_button_xpath))
        settingsButton.click()
        sleep(1)
        settingsButton = self.waitForElementVisible((By.XPATH, settings_button_xpath))
        settingsButton.click()
        current_url= self.driver.current_url
        excepted_url = "https://tobeto.com/profilim/profilimi-duzenle/ayarlar"
        assert current_url == excepted_url
       

    #Ayarlarım sayfasında ,şifre değiştirme alanlarının boş geçilmesi
    def test_settings_emptyPassword(self):
        self.valid_login()
        settingsButton = self.waitForElementVisible((By.XPATH, settings_button_xpath))
        settingsButton.click()
        sleep(1)
        oldPassword = self.waitForElementVisible((By.XPATH,old_password_xpath))
        oldPassword.send_keys("")
        newPassword = self.waitForElementVisible((By.XPATH,new_password_xpath)) 
        newPassword.send_keys("") 
        newPasswordAgain =self.waitForElementVisible((By.XPATH,new_password_again_xpath)) 
        newPasswordAgain.send_keys("")
        changePasswordButton = self.waitForElementVisible((By.XPATH,change_password_button)) 
        changePasswordButton.click()
        if oldPassword.get_attribute("value") == "" or newPassword.get_attribute("value") == "" or newPasswordAgain.get_attribute("value") == "":
           alertPasswordEmpty = self.waitForElementVisible((By.XPATH, alert_password_empty))
        assert alertPasswordEmpty.text == "Doldurulması zorunlu alan"
                
    #Ayarlarım eski şifre yanlış girilmesi 
    def test_settings_wrongOldPassword(self):
        self.valid_login()
        settingsButton = self.waitForElementVisible((By.XPATH, settings_button_xpath))
        settingsButton.click()
        sleep(1)
        oldPassword = self.waitForElementVisible((By.XPATH,old_password_xpath))
        oldPassword.send_keys("123abc")
        newPassword = self.waitForElementVisible((By.XPATH,new_password_xpath))
        newPassword.send_keys("987654")
        newPasswordAgain =self.waitForElementVisible((By.XPATH,new_password_again_xpath))
        newPasswordAgain.send_keys("987654")
        changePasswordButton = self.waitForElementVisible((By.XPATH,change_password_button))
        changePasswordButton.click()
        alertOldWrongPassword =self.waitForElementVisible((By.XPATH,alert_old_wrong_password))
        assert alertOldWrongPassword.text == "• Mevcut şifre geçersizdir."

    #Belirlenen şifre 6 karakterden az ise uyarıyı görüntüle
    def test_settings_shortPassword(self):
        self.valid_login()
        settingsButton = self.waitForElementVisible((By.XPATH, settings_button_xpath))
        settingsButton.click()
        sleep(1)
        oldPassword = self.waitForElementVisible((By.XPATH,old_password_xpath))
        oldPassword.send_keys("123456")
        newPassword = self.waitForElementVisible((By.XPATH,new_password_xpath))
        newPassword.send_keys("123")
        newPasswordAgain =self.waitForElementVisible((By.XPATH,new_password_again_xpath))
        newPasswordAgain.send_keys("123")
        changePasswordButton = self.waitForElementVisible((By.XPATH,change_password_button))    
        changePasswordButton.click()
        alertShortPassword =self.waitForElementVisible((By.XPATH,alert_short_password))
        assert alertShortPassword.text == "• Şifreniz en az 6 karakterden oluşmalıdır."
     

    
    #Şifreler uyuşmuyor ise uyarı ver
    def test_settings_passwordNotMatch(self):
        self.valid_login()
        settingsButton = self.waitForElementVisible((By.XPATH, settings_button_xpath))
        settingsButton.click()
        sleep(1)
        oldPassword = self.waitForElementVisible((By.XPATH,old_password_xpath))
        oldPassword.send_keys("123456")
        newPassword = self.waitForElementVisible((By.XPATH,new_password_xpath))
        newPassword.send_keys("123456789")
        newPasswordAgain =self.waitForElementVisible((By.XPATH,new_password_again_xpath))
        newPasswordAgain.send_keys("1234567")
        changePasswordButton = self.waitForElementVisible((By.XPATH,change_password_button))
        changePasswordButton.click()
        alertPasswordNotMatch =self.waitForElementVisible((By.XPATH,alert_password_not_match))
        assert alertPasswordNotMatch.text == "Girilen şifreler eşleşmiyor kontrol ediniz."       



    #Eski şifre ile yeni şifre farklı olmalı
    def test_settings_passwordNotSame(self):
        self.valid_login()
        settingsButton = self.waitForElementVisible((By.XPATH, settings_button_xpath))
        settingsButton.click()
        sleep(1)
        oldPassword = self.waitForElementVisible((By.XPATH,old_password_xpath))
        oldPassword.send_keys("123456")
        newPassword = self.waitForElementVisible((By.XPATH,new_password_xpath))
        newPassword.send_keys("123456")
        newPasswordAgain =self.waitForElementVisible((By.XPATH,new_password_again_xpath))
        newPasswordAgain.send_keys("123456")
        changePasswordButton = self.waitForElementVisible((By.XPATH,change_password_button))
        changePasswordButton.click()
        alertPasswordNotSame =self.waitForElementVisible((By.XPATH,alert_password_not_same))
        assert alertPasswordNotSame.text == "Yeni şifreniz mevcut şifrenizden farklı olmalıdır."
        sleep(1)

    
    #Şifreler uyuşuyor ise şifre değiştirme işlemi gerçekleşir
    def test_settings_passwordMatch(self):
        self.valid_login()
        settingsButton = self.waitForElementVisible((By.XPATH, settings_button_xpath))
        settingsButton.click()
        sleep(1)
        oldPassword = self.waitForElementVisible((By.XPATH,old_password_xpath))
        oldPassword.send_keys("123456")
        newPassword = self.waitForElementVisible((By.XPATH,new_password_xpath))
        newPassword.send_keys("123456789")
        newPasswordAgain =self.waitForElementVisible((By.XPATH,new_password_again_xpath))
        newPasswordAgain.send_keys("123456789")
        changePasswordButton = self.waitForElementVisible((By.XPATH,change_password_button))
        changePasswordButton.click()
        alertPasswordMatch =self.waitForElementVisible((By.XPATH,alert_password_match))
        assert alertPasswordMatch.text == "Şifreniz güncellenmiştir."
        sleep(1)


    #Üyeliği sonlandır = Membership Termination
    def test_settings_membershipTermination(self): 
        self.valid_login() 
        settingsButton = self.waitForElementVisible((By.XPATH, settings_button_xpath))
        settingsButton.click()
        sleep(1)
        membershipTerminationButton = self.waitForElementVisible((By.CSS_SELECTOR, membership_termination_button))
        membershipTerminationButton.click()
        accountDeletedWindow = self.waitForElementVisible((By.CSS_SELECTOR, account_deleted_win))
        accountDeletedWindow.click()
        sleep(1)
        deleteAccountChoose= self.waitForElementVisible((By.XPATH,delete_account_choose_button))
        deleteAccountChoose.click()
        sleep(1)
        accountYesButton = self.waitForElementVisible((By.CSS_SELECTOR,account_yes_button_id))
        accountYesButton.click()
        sleep(2)
        alertaccountDeleted = self.waitForElementVisible((By.CSS_SELECTOR, alert_account_deleted))
        assert alertaccountDeleted.text == "Hesabınız silindi."
        sleep(3)
        self.driver.save_screenshot("screenshot.png")
    





    
       
      
