from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from userInfo import *
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.keys import Keys
import pytest
from constants.MyMediaAccountConstants import *
from selenium.webdriver.common.action_chains import ActionChains

class Test_My_Media_Accounts: 

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(base_url)
    
    def teardown_method(self):
        self.driver.quit()

    def valid_login_method(self,email,password):

        emailInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, email_xpath)))
        emailInput.send_keys(email)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, password_xpath)))
        passwordInput.send_keys(password)
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, login_button_xpath)))
        loginButton.click()
        sleep()
        loginMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, loginMessage_xpath)))
        assert loginMessage.text == "• Giriş başarılı."

    def account_added(self):
        
        accountAddedAlert = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, accountAddedAlert_css)))
        assert accountAddedAlert.text == "• Sosyal medya adresiniz başarıyla eklendi."
        sleep(1)

    def account_deleted(self):

        accountDeletedAlert = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, accountDeletedAlert_css)))
        assert accountDeletedAlert.text == "• Sosyal medya adresiniz başarıyla kaldırıldı."
        sleep(1)

    def test_check_my_media_account(self):

        self.valid_login_method(usEMail,usPassword)

        myProfileButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, myProfileButton_xpath)))
        myProfileButton.click()

        editMyProfileButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, editMyProfileButton_xpath)))
        editMyProfileButton.click()
        
        myMediaAccountsButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, myMediaAccountsButton_xpath)))
        myMediaAccountsButton.click()
        sleep(1)

        saveButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, saveButton_xpath)))
        saveButton.click()
        sleep(2)

        platformAlertMessage = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, platformAlertMessage_css)))
        assert platformAlertMessage.text == "Doldurulması zorunlu alan*"

        urlAlertMessage = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, urlAlertMessage_css)))
        assert urlAlertMessage.text == "Doldurulması zorunlu alan*"

    def test_successful_account_addition(self):

        self.valid_login_method(usEMail,usPassword)

        myProfileButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, myProfileButton_xpath)))
        myProfileButton.click()
        sleep(1)
        editMyProfileButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, editMyProfileButton_xpath)))
        editMyProfileButton.click()
        sleep(1)
        myMediaAccountsButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, myMediaAccountsButton_xpath)))
        myMediaAccountsButton.click()
        sleep(1)

        # 1. medya hesabı ekleme
        platformlistButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, platformListButton_xpath)))
        platformlistButton.click()
        sleep(1)
        platformChooseButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, platformChooseButton_xpath)))
        platformChooseButton.click()
        sleep(2)
        platformUrlAdd = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, platformUrlAdd_xpath)))
        platformUrlAdd.send_keys(instagramUrl)
        sleep(1)
        saveButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, saveButton_xpath)))
        saveButton.click()
        sleep(1)
        self.account_added()
        sleep(2)

        # Aynı hesabı tekrar ekle (Ayni hesap bilgisi tekrar girilemez.)
        platformListButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, platformListButton_xpath)))
        platformListButton.click()
        sleep(1)
        platformChooseButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, platformChooseButton_xpath)))
        platformChooseButton.click()
        sleep(1)
        platformUrlAdd = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, platformUrlAdd_xpath)))
        platformUrlAdd.send_keys(instagramUrl)
        sleep(1)

        saveButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, saveButton_xpath)))
        saveButton.click()
        sleep(1)

        platformUrlAdd.clear()
        sleep(1)
        # 2. medya hesabı ekleme
        platformListButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, platformListButton_xpath)))
        platformListButton.click()
        sleep(2)

        platformChooseButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, platformChooseButton2_xpath)))
        platformChooseButton.click()
        sleep(1)

        platformUrlAdd = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, platformUrlAdd_xpath)))
        platformUrlAdd.send_keys(twitterUrl)
        sleep(1)

        saveButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, saveButton_xpath)))
        saveButton.click()
        sleep(1)

        self.account_added()
        sleep(1)

        # 3. medya hesabı ekleme
        platformListButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, platformListButton_xpath)))
        platformListButton.click()
        sleep(1)

        platformChooseButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, platformChooseButton3_xpath)))
        platformChooseButton.click()
        sleep(1)

        platformUrlAdd = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, platformUrlAdd_xpath)))
        platformUrlAdd.send_keys(linkedInUrl)
        sleep(1)

        saveButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, saveButton_xpath)))
        saveButton.click()
        sleep(1)

        self.account_added
        sleep(1)

        max3alerts = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, max3alerts_css)))
        assert max3alerts.text == "En fazla 3 adet medya seçimi yapılabilir."

        editAccountInformation = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, editAccountInformation_css)))
        editAccountInformation.click()
        sleep(1)

        editUrl = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, editUrl_xpath)))
        editUrl.send_keys("/")
        sleep(1)

        update = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, update_xpath)))
        update.click()
        sleep(1)

        updateAlert = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, forbiddenAlert_css)))
        assert updateAlert.text == "• Forbidden"
        sleep(1)

    def test_successful_account_deletion(self):

        self.valid_login_method(usEMail,usPassword)

        myProfileButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, myProfileButton_xpath)))
        myProfileButton.click()
        sleep(1)
        editMyProfileButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, editMyProfileButton_xpath)))
        editMyProfileButton.click()
        sleep(1)       
        myMediaAccountsButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, myMediaAccountsButton_xpath)))
        myMediaAccountsButton.click()
        sleep(1)

        # 1. medya hesabımı sil
        deleteButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, deleteButton_xpath)))
        deleteButton.click()
        sleep(1)

        deleteAlert = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, deleteAlert_css)))
        assert deleteAlert.text == "Seçilen sosyal medya hesabını silmek istediğinize emin misiniz?"
        sleep(2)

        deleteAlert2 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, deleteAlert2_css)))
        assert deleteAlert2.text == "Bu işlem geri alınamaz."
        sleep(3)

        yesButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, yesButton_xpath)))
        yesButton.click()
        sleep(4)

        self.account_deleted()
        sleep(1)
        # 2. medya hesabimi sil
        deleteButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, deleteButton2_xpath)))
        deleteButton.click()
        sleep(1)

        deleteAlert = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, deleteAlert_css)))
        assert deleteAlert.text == "Seçilen sosyal medya hesabını silmek istediğinize emin misiniz?"
        sleep(2)

        deleteAlert2 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, deleteAlert2_css)))
        assert deleteAlert2.text == "Bu işlem geri alınamaz."
        sleep(2)

        yesButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, yesButton_xpath)))
        yesButton.click()
        sleep(2)

        self.account_deleted()

        # 3. medya hesabımı sil
        deleteButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, deleteButton2_xpath)))
        deleteButton.click()
        sleep(1)

        deleteAlert = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, deleteAlert_css)))
        assert deleteAlert.text == "Seçilen sosyal medya hesabını silmek istediğinize emin misiniz?"
        sleep(2)

        deleteAlert2 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, deleteAlert2_css)))
        assert deleteAlert2.text == "Bu işlem geri alınamaz."
        sleep(2)

        yesButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, yesButton_xpath)))
        yesButton.click()
        sleep(2)

        self.account_deleted()
        sleep(1)
        
