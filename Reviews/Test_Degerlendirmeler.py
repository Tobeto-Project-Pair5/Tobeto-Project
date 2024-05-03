from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.keys import Keys
import pytest
from degerlendirmelerContstants import *
from selenium.webdriver.common.action_chains import ActionChains

class Test_Degerlendirmeler:
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
        sleep(3)
    def testReviewsbegin(self):
        self.valid_login_method("moxar70660@abnovel.com","test1234")
        sleep(2)
        reviewsButton= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, reviewsxpath)))
        reviewsButton.click()
        sleep(2)
        systemMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, systemMessagexpath)))
        assert systemMessage.text == "Yetkinliklerini ücretsiz ölç, bilgilerini test et."
        tobetoButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, beginxpath)))
        tobetoButton.click()
        sleep(2)
        self.driver.execute_script("window.scrollBy(0, 175);")
        sleep(2)
        reviewsBeginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, beginTestxpath)))
        reviewsBeginButton.click()
        sleep(2)
        self.driver.execute_script("window.scrollBy(0, 175);")
        sleep(2)
    def testReviewshalf(self):
        self.valid_login_method("moxar70660@abnovel.com","test1234")
        sleep(2)
        reviewsButton= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, reviewsxpath)))
        reviewsButton.click()
        sleep(2)
        sistemMesaji = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, systemMessagexpath)))
        assert sistemMesaji.text == "Yetkinliklerini ücretsiz ölç, bilgilerini test et."
        tobetoButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, beginxpath)))
        tobetoButton.click()
        sleep(2)
        self.driver.execute_script("window.scrollBy(0, 175);")
        sleep(2)
        reviewsButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, beginTestxpath)))
        reviewsButton.click()
        sleep(3)
        reviews = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, buttonClickxpath)))
        reviews.click()
        sleep(3)
        reviews1 = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, buttonClickxpath1)))
        reviews1.click()
        sleep(3)        
        reviews2 = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, buttonClickxpath2)))
        reviews2.click()
        sleep(3)
        reviews3 = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, buttonClickxpath3)))
        reviews3.click()
        sleep(3)
        reviews4 = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, buttonClickxpath4)))
        reviews4.click()
        sleep(3)
        reviews5 = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, buttonClickxpath5)))
        reviews5.click()
        sleep(3)
        reviews6 = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, buttonClickxpath6)))
        reviews6.click()
        sleep(3)
        reviewsButton= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, reviewsxpath)))
        reviewsButton.click()
        sleep(2)
        sistemMesaji = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, systemMessagexpath)))
        assert sistemMesaji.text == "Yetkinliklerini ücretsiz ölç, bilgilerini test et."
        tobetoButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, beginxpath)))
        tobetoButton.click()
        sleep(2)
        self.driver.execute_script("window.scrollBy(0, 175);")
        sleep(2)
        reviewsButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, beginTestxpath)))
        reviewsButton.click()
        self.driver.execute_script("window.scrollBy(0, 175);")
        sleep(2)

        



                                                              


        