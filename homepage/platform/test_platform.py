from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from time import sleep
from constants.platformConstants import *
import pytest
from selenium.webdriver.common.alert import Alert

class Test_platform:   
        def login_page(self):
            self.driver = webdriver.Chrome()
            self.driver.get(LOGIN_URL)
            self.driver.maximize_window() 
        
        def tearDown(self):
            self.driver.quit()
 
        def valid_login(self):
            self.login_page()
            email = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME, userEmail)))
            email.send_keys("tobetopair5@gmail.com")
            sleep(2)
            password = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, userPassword)))
            password.send_keys("********")
            loginButton = self.driver.find_element(By.XPATH, LOGIN_XPATH)
            loginButton.click()
            sleep(2)
            self.driver.execute_script("window.scrollBy(0, 500);")    #Aşağıya kaydırma
            sleep(2)

        def test_platform(self):
            self.valid_login()
            #Eğitimlerim kontrolü
            egitimlerim = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, LESSONS)))
            egitimlerim.click()
            sleep(5)
            
            #Duyuru ve haber kontrolü
            duyuruvehaber = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, NOTIFICATION)))
            duyuruvehaber.click()
            sleep(5)

            #Anketlerim kontrolü
            anket = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, SURVEY)))
            anket.click()
            sleep(5)
            
            #Basvuru kontrolü
            basvuru = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, APPLY)))
            basvuru.click()
            sleep(5)

            self.driver.execute_script("window.scrollBy(0, 500);")   #Sınavlarım, profilini oluştur,kendini değerlendir ve öğrenmeye başla kısmı görüntülensin diye aşağı kaydırıyor.
            sleep(5)