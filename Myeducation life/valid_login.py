from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import globalConstants as c
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

class Test_Valid_Login:
    def __init__(self,driver):
        self.driver = driver
    def setup_method(self):        
        self.driver = webdriver.Chrome()
        self.driver.get(c.LOGIN_URL)
        self.driver.maximize_window()
    def teardown_method(self):
        self.driver.quit()  
    def valid_login(self,email,password):
        firstLoginButton = self.driver.find_element(By.CSS_SELECTOR,c.firstLoginButton)
        firstLoginButton.click()
        emailInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.emailName)))
        sleep(2)
        emailInput.send_keys(email)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.passwordName)))
        sleep(3)
        passwordInput.send_keys(password)
        loginButton = self.driver.find_element(By.XPATH,c.loginButton)
        loginButton.click()
        loginMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,c.loginMessage)))
        assert loginMessage.text == "• Giriş başarılı."    

