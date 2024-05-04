from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from time import sleep
from constants.educationsConstants import *

class Test_myEducations:
    def login_page(self):
        self.driver = webdriver.Chrome()
        self.driver.get(LOGIN_URL)
        self.driver.maximize_window() 
        
    def tearDown(self):
        self.driver.quit()
 
    def valid_login(self):
        self.login_page()
        email = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME, NAME_TAG)))
        email.send_keys("tobetopair5@gmail.com")
        sleep(2)
        psw = WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.NAME, PSW_TAG)))
        psw.send_keys("********")
        loginButton = self.driver.find_element(By.XPATH, login_xpath)
        loginButton.click()
        sleep(2)
        self.driver.execute_script("window.scrollBy(0, 500);")    # Aşağıya 200 piksel kaydırma
        sleep(2)
        
    def test_education(self):
        self.valid_login()
        sleep(5)
        myEducations = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, myEducations_id)))
        myEducations.click()
        sleep(6)
        myEducationsShowMore = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, showMoreButton)))
        myEducationsShowMore.click()
        sleep(5)
        
    #eğitim ismiyle eşleşen veri konrolü
        searchButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, search_id)))
        searchButton.send_keys("h")
        sleep(5)
    #eğitim arama butonun içini silme
        searchButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, search_id)))
        searchButton.clear()
        sleep(5)
    #eğitim olmayan arama yapma 
        searchButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, search_id)))
        searchButton.send_keys("w")
        sleep(5)
        education_message = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, education_xpath)))
        testResult = education_message.text == "Size atanan herhangi bir eğitim bulunmamaktadır."
        print(f"Eğitim yok sonucu: {testResult}")
        sleep(5)
    #sayfa yenilenir
        self.driver.get(EDUCATION_URL)
        self.driver.refresh()
        sleep(3)
    #kurum seçimi arama butonu İstanbul Kodluyor seçimi
        institutionButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, institution_xpath)))
        institutionButton.click()
        istanbulKodluyor = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, istanbulKodluyor_id)))
        istanbulKodluyor.click()            
        sleep(5)
        deleteFilterButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,deleteFilter)))
        deleteFilterButton.click()
        sleep(5)
    
    #Devam ettiklerim
        continueButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, continue_xpath)))
        continueButton.click() 
        sleep(5) 

    #Tamamladıklarım
        completedEducations = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, completedEducations_xpath)))
        completedEducations.click() 
        sleep(5)

    #tumegitimler
        allEducations = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, allEducations_xpath)))
        allEducations.click() 
        sleep(5)

    #tarihe göre E-Y sırala-->FAİL:Yanlış sıralanıyor
        listButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, listButton_xpath)))
        listButton.click()
        listE_Y=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, listE_Y_id)))
        listE_Y.click()
        sleep(7)

    #tarihe göre Y-E sırala-->FAİL:Yanlış sıralanıyor
        listButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, listButton_xpath)))
        listButton.click()
        listY_E=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, listY_E_id)))
        listY_E.click()
        sleep(7)

    #adına göre Z-A sırala
        siralamaButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, listButton_xpath)))
        siralamaButton.click()
        adinagoreZA=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, listZ_A_id)))
        adinagoreZA.click()
        sleep(7)

    #adına göre A-Z sırala
        listButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, listButton_xpath)))
        listButton.click()
        listA_Z=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, listA_Z_id)))
        listA_Z.click()
        sleep(7)