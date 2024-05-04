import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
#from userInfo import email, password
from selenium.webdriver.support.ui import Select
import pytest
from constants.foreignLanguageConstans import *

class Test_Tobeto_Platform_Foreign_Language_Test():

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(LOGIN_URL)
        self.driver.maximize_window()

    def teardown_method(self): 
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout = 5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def test_foreign_language_page(self):
        #Siteye giris yapma
        emailInput = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, login_checkbox_email_xpath)))
        emailInput.send_keys(email)
        passwordInput = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, login_checkbox_password_xpath)))
        passwordInput.send_keys(password)

        loginButton = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, login_button_xpath)))
        loginButton.click()
        sleep(5)

        #navbar'a tiklama
        navbarButton = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, navbar_button_css)))
        navbarButton.click()
        sleep(5)

        #Profil butonuna tiklama
        profilePageButton = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, profile_page_xpath)))
        profilePageButton.click()
        sleep(5)

        #Profil bilgileri butonuna tiklama
        profileInfoPageButton = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, profile_info_page_xpath)))
        profileInfoPageButton.click()
        sleep(5)

        #Yabanci dillerim kismina tiklama
        foreignLanguagePageButton = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, foreign_language_xpath)))
        foreignLanguagePageButton.click()
        sleep(5)

        ## 1- Dil ve seviye seceklerinin bos gecilmesi
        languageSaveButton = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, language_save_button_xpath)))
        languageSaveButton.click()
        sleep(2)

        errorEmptyLanguage = WebDriverWait(self.driver,2).until(EC.visibility_of_element_located((By.XPATH, error_empty_language)))
        assert errorEmptyLanguage.text == errorEmptyLanguageText

        ## 2- Yabancı Dil kaydinin basarıyla gerceklesmesi
        find_language = \
        self.driver.find_element(By.NAME,"languageName")
        select_language = Select(find_language)
        select_language.select_by_visible_text("Fransızca")
        sleep(5)

        selectLanguageLevelButton = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, select_language_level_xpath)))
        selectLanguageLevelButton.click()
        sleep(5)

        find_language_level = \
        self.driver.find_element(By.NAME,"proficiency")
        select_language_level = Select(find_language_level)
        select_language_level.select_by_visible_text("Anadil")
        sleep(5)

        languageSaveButton = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, language_save_button_xpath)))
        languageSaveButton.click()
        sleep(2)

        addLanguageMessage =  WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, alert_xpath)))
        assert addLanguageMessage.text == addLanguageMessageText 
        sleep(5)
        ## 3- Bu dil zaten mevcut uyarisinin alinmasi
        find_language = \
        self.driver.find_element(By.NAME,"languageName")
        select_language = Select(find_language)
        select_language.select_by_visible_text("Fransızca")
        sleep(5)

        selectLanguageLevelButton = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, select_language_level_xpath)))
        selectLanguageLevelButton.click()
        sleep(5)

        find_language_level = \
        self.driver.find_element(By.NAME,"proficiency")
        select_language_level = Select(find_language_level)
        select_language_level.select_by_visible_text("Anadil")
        sleep(5)

        languageSaveButton = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, language_save_button_xpath)))
        languageSaveButton.click()
        sleep(2)

        errorAddLanguageMessage =  WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, alert_xpath)))
        assert errorAddLanguageMessage.text == errorAddLanguageMessageText 
        sleep(2)

        ## 4- Silme islemi
        def deleteLanguage(self):
            deleteBox = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, delete_box_xpath)))
            deleteBox.click()
            sleep(5)

            deleteLanguageButton = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, delete_language_button_xpath)))
            deleteLanguageButton.click()
            sleep(5)

        #Silme islemini reddet
        deleteLanguage(self)

        rejectDeleteButton = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, reject_delete_button_xpath)))
        rejectDeleteButton.click()
        sleep(5)

        #Silme islemini onayla
        deleteLanguage(self)
            
        confirmDeleteButton = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, confirm_delete_button_xpath)))
        confirmDeleteButton.click()
        sleep(2)

        LanguageRemoveSuccessful =  WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((By.XPATH, language_remove_successful)))
        assert LanguageRemoveSuccessful.text == LanguageRemoveSuccessfulText  

        self.driver.quit()
        


        
