from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from userInfo import *
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest
from constants.deneyimlerimConstants import *
from selenium.webdriver.common.action_chains import ActionChains

class Test_Deneyimlerim:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(base_url)
    
    def teardown_method(self):
        self.driver.quit()
        
    def waitForElementVisible(self,locator,timeout=10):
      return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
        
    @pytest.mark.skip()
    def test_login(self):  
        email_input = self.waitForElementVisible((By.NAME, "email"))
        password_input = self.waitForElementVisible((By.NAME, "password"))
        password_input.click()
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(email_input, username)
        actions.send_keys_to_element(password_input, password)
        actions.perform()
        login_input = self.waitForElementVisible((By.XPATH,login_input_Xpath ))
        login_input.click()
        Pop_up_messsage_sucsesfull= self.waitForElementVisible((By.XPATH,login_messsage_Xpath))
        assert Pop_up_messsage_sucsesfull.text == Pop_up_messsage_sucsesfull_text
    def test_title_control(self):
        self.test_login()
        tab_profile_button = self.waitForElementVisible((By.XPATH,tab_profile_button_Xpath))
        tab_profile_button.click()
        edit_profile_button = self.waitForElementVisible((By.XPATH, edit_profile_button_Xpath))
        edit_profile_button.click()
        sleep(2)
        experiences_button = self.waitForElementVisible((By.XPATH,experiences_button_Xpath))
        experiences_button.click()
        
        #Başlık kontrolleri
        required_field_step  = self.waitForElementVisible((By.XPATH, "//label[contains(.,'Kurum Adı*')]"))  
        required_field_step1 = self.waitForElementVisible((By.XPATH, "//label[contains(.,'Pozisyon*')]"))
        required_field_step2 = self.waitForElementVisible((By.XPATH, "//label[contains(.,'Sektör*')]"))
        required_field_step3 = self.waitForElementVisible((By.XPATH, "//label[contains(.,'Şehir Seçiniz*')]"))
        required_field_step4 = self.waitForElementVisible((By.XPATH,"//label[contains(.,'İş Başlangıcı*')]"))
        required_field_step5 = self.waitForElementVisible((By.XPATH,"//label[contains(.,'İş Bitiş*')]"))
        required_field_step6 = self.waitForElementVisible((By.XPATH,"//label[contains(.,'İş Açıklaması')]"))
        assert {required_field_step.text  == Required_field_step_text,
               required_field_step1.text== Required_field_step1_text, 
               required_field_step2.text== Required_field_step2_text,
               required_field_step3.text== Required_field_step3_text,
               required_field_step4.text== Required_field_step4_text,
               required_field_step5.text== Required_field_step5_text,
               required_field_step6.text== Required_field_step6_text
               }

        

    def test_warging_message(self):
        self.test_title_control()
        
        save_experiences_button=self.waitForElementVisible((By.XPATH,save_experiennces_button_Xpath))
        save_experiences_button.click()
        
     #save buttonuna tıklama işleminden sonraki uyarılar
        required_field_warning  = self.waitForElementVisible((By.CSS_SELECTOR,required_field_warning_css))  
        required_field_warning1 = self.waitForElementVisible((By.CSS_SELECTOR, required_field_warning1_css))
        required_field_warning2 = self.waitForElementVisible((By.CSS_SELECTOR, required_field_warning2_css))
        required_field_warning3 = self.waitForElementVisible((By.CSS_SELECTOR, required_field_warning3_css))
        required_field_warning4 = self.waitForElementVisible((By.CSS_SELECTOR,required_field_warning4_css))
        assert {required_field_warning.text  == required_field_warning_text,
                required_field_warning1.text == required_field_warning1_text,
                required_field_warning2.text == required_field_warning2_text,
                required_field_warning3.text == required_field_warning3_text,
                required_field_warning4.text == required_field_warning4_text
                }
        
   
   
    def test_input_values(self):
        self.test_title_control()
        save_experiences_button=self.waitForElementVisible((By.XPATH,save_experiennces_button_Xpath))
        save_experiences_button.click()
        #Kurum Adı
        corporationName_input = self.waitForElementVisible((By.NAME,"corporationName"))
        corporationName_input.click()
        corporationName_input.send_keys("Aşçı")
        assert corporationName_text in self.waitForElementVisible((By.XPATH,corporationName_text_Xpath)).text
        corporationName_input.clear()
        corporationName_input.send_keys(ellibirkaraktermetin)
        assert corporationName2_text in self.waitForElementVisible((By.XPATH, corporationName2_text_Xpath)).text
        
        
        #Pozisyon
        position_input=self.driver.find_element(By.NAME, "position")
        position_input.click()
        position_input.send_keys("aşçı")
        assert position_button_text in self.waitForElementVisible((By.XPATH,position_button_text_Xpath)).text
        position_input.clear()
        position_input.send_keys(ellibirkaraktermetin)
        assert position_button2_text in self.waitForElementVisible((By.XPATH, position_button2_text_Xpath)).text
        
        #sektör
        sector_input=self.driver.find_element(By.NAME, "sector")
        sector_input.click()
        sector_input.send_keys("aşçı")
        assert sector_input_text in self.waitForElementVisible((By.XPATH,sector_input_text_Xpath)).text
        sector_input.clear()
        sector_input.send_keys(ellibirkaraktermetin)
        assert sector_input2_text in self.waitForElementVisible((By.XPATH, sector_input2_text_Xpath)).text
       
        
    def test_add_experience(self):
        self.test_title_control()
        save_experiences_button=self.waitForElementVisible((By.XPATH,save_experiennces_button_Xpath))
        save_experiences_button.click()
        
        corporationName_input = self.waitForElementVisible((By.NAME,"corporationName"))
        corporationName_input.click()
        corporationName_input.send_keys("Boğaziçi Et Lokantası")
        
        position_input=self.driver.find_element(By.NAME, "position")
        position_input.click()
        position_input.send_keys("Garson")
        
        sector_input=self.driver.find_element(By.NAME, "sector")
        sector_input.click()
        sector_input.send_keys("Yemek")
        
        dropdown = self.driver.find_element(By.NAME, "country")
        dropdown.find_element(By.XPATH, "//option[. = 'İstanbul']").click()
        #İş Başlangıcı
        startDate_input=self.driver.find_element(By.XPATH,startDate_input_Xpath )
        startDate_input.click()
        startDate_input.send_keys("2020-01-01", Keys.ENTER)
        
        
        not_working=self.waitForElementVisible((By.XPATH,not_working_Xpath))
        not_working.click()
        save_button=self.waitForElementVisible((By.XPATH,save_experiennces_button_Xpath))
        save_button.click()
        
        
          
    def test_experiences_delete(self):
        self.test_add_experience()
        self.driver.execute_script("window.scrollTo(0, 650);")
        sleep(2)
        experiences_delete_button = self.waitForElementVisible((By.XPATH,experiences_delete_button_css))
        experiences_delete_button.click()
        sleep(2)                                                       
        yes_button = self.waitForElementVisible((By.XPATH,yes_button_Xpath))
        yes_button.click()
        sleep(2)
        Pop_up_Message = self.waitForElementVisible((By.XPATH,Pop_up))
        assert Pop_up_Message.text.lower() == Pop_up_messsage_text.lower()
        sleep(2)

    




        

        

















