from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.keys import Keys
import pytest
from constants.myAnnouncementsAndNewsConstants import *
from selenium.webdriver.common.action_chains import ActionChains


class Test_MyAnnouncement_And_News:

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
        sleep(2)
    
    def test_show_more(self):
        self.valid_login_method("onurbulgu@gmail.com","Onur.5234")
        sleep(2)
        self.driver.execute_script("window.scrollBy(0, 150);")
        sleep(2)
        announcementAndNewsButton= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, announcementAndNewsButton_xpath)))
        announcementAndNewsButton.click()
        self.driver.execute_script("window.scrollBy(0, 200);")
        sleep(3)
        showMoreButton= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, showMoreButton_xpath)))
        sleep(2)
        showMoreButton.click()
        sleep(2)
        oneAnnouncement = WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR, oneAnnouncement_css)))
        assert len(oneAnnouncement) == 9
        sleep(2)
        callButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, callButton_xpath)))
        callButton.send_keys("as")
        sleep(2)
        typeButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, typeButton_xpath)))
        typeButton.click()
        sleep(2)
        announcementbutton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, announcementbutton_xpath)))
        announcementbutton.click()
        sleep(2)
        organizationButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, organizationButton_xpath)))
        organizationButton.click()
        sleep(2)
        istanbulIsCodingButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, istanbulIsCodingButton_xpath)))
        istanbulIsCodingButton.click()
        sleep(2)
        istanbulIsCodingButtonKaldir = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, istanbulIsCodingButtonKaldir_css)))
        istanbulIsCodingButtonKaldir.click()
        sleep(2)
        arrangementButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, arrangementButton_xpath)))
        arrangementButton.click()
        sleep(2)
        newToOld = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, newToOld_xpath)))
        newToOld.click()
        sleep(2)
        arrangementButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, arrangementButton_xpath)))
        arrangementButton.click()
        sleep(2)
        oldToNew = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, oldToNew_xpath)))
        oldToNew.click()
        sleep(2)
        # Fail adım (Okunmuş olanları gizlemiyor.)
        hideReadWhatButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, hideReadWhatButton_xpath)))
        hideReadWhatButton.click()
        sleep(2)
        showAllButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, showAllButton_xpath)))
        showAllButton.click()
        sleep(2)


