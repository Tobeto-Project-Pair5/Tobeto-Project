from selenium import webdriver
# from userInfo import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from constants.myCertificatesConstants import *
# from PIL import Image
from time import sleep
import pytest

class Test_My_Certificates():
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

    #Sertifikalarım görüntüle
    def test_myCertificates(self):
        self.valid_login()
        sleep(2)
        myCertificatesPage= self.waitForElementVisible((By.XPATH, my_certificates_xpath))
        myCertificatesPage.click()
        current_url= self.driver.current_url
        excepted_url = "https://tobeto.com/profilim/profilimi-duzenle/sertifikalarim"
        assert current_url == excepted_url
            


    #Sertifikalarım ,belge yükleme
    def test_myCertificatesFileLoad(self):
        self.valid_login()
        myCertificatesPage= self.waitForElementVisible((By.XPATH, my_certificates_xpath))
        myCertificatesPage.click()
        sleep(2)
        certificateFileLoad = self.waitForElementVisible((By.CSS_SELECTOR,certificates_file_load))
        certificateFileLoad.click()
        sleep(3)
        # certificateBrowseButton = self.waitForElementVisible((By.CSS_SELECTOR, certificate_browse_button ))
        # certificateBrowseButton.click()
        # sleep(3)
        # certificateFileInput = self.waitForElementVisible((By.XPATH, "//input[@type='file']"))
        # certificateFileInput.send_keys(r"C:\Users\Desktop\Certificates")
        profileFileInput = self.driver.find_element(By.XPATH, profile_file_input)
        profileFileInput.send_keys(file_path)
        sleep(2)
        fileLoadButton=self.waitForElementVisible((By.CSS_SELECTOR,file_load_button))
        fileLoadButton.click()
        sleep()








    #Sertifikalarım ,yüklü olan sertifikayı indirme
    def test_myCertificatesDownload(self):
        self.valid_login()
        myCertificatesPage= self.waitForElementVisible((By.XPATH, my_certificates_xpath))
        myCertificatesPage.click()
        sleep(2)
        certificateDownload = self.waitForElementVisible((By.CSS_SELECTOR,certificates_download_icon))
        certificateDownload.click() 
        sleep(3)                                                                                       

    #Sertifika Silme
    def test_myCertificatesDelete(self):
        self.valid_login()
        myCertificatesPage= self.waitForElementVisible((By.XPATH, my_certificates_xpath))
        myCertificatesPage.click()
        sleep(1)
        certificateDeleteIcon =self.waitForElementVisible((By.CSS_SELECTOR, certificate_delete_icon))
        certificateDeleteIcon.click()
        sleep(2)
        deleteCertificateChoose = self.waitForElementVisible((By.XPATH, certificate_choose_button))
        deleteCertificateChoose.click()
        sleep(1)
        yesButtonCertificate = self.waitForElementVisible((By.CSS_SELECTOR, yesButton))
        yesButtonCertificate.click()
        sleep(1)
        alertCertificateDeleted = self.waitForElementVisible((By.CSS_SELECTOR, alert_certificate_deleted))
        assert alertCertificateDeleted.text == "• Dosya kaldırma işlemi başarılı."
        sleep(2)
   

