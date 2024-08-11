from selenium import webdriver
from userInfo import username, password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from constants.globalConstants import *
import pytest
from time import sleep
import pyautogui



class Test_Register():
     
  def setup_method(self):
   self.driver = webdriver.Chrome()
   self.driver.maximize_window()
   self.driver.get(BASE_URL)
   self.vars = {} 
   
  def teardown_method(self):
   self.driver.quit()
   
  def waitForElementVisible(self,locator,timeout=5):
    return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

   
  def waitForElementVisible(self,locator,timeout=10):
     return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
                                            #LOGİN      
  @pytest.mark.skip
  def test_login(self):  
    email_input = self.waitForElementVisible((By.XPATH,email_input_Xpath))
    email_input.click()
    password_input = self.waitForElementVisible((By.XPATH,password_input_Xpath))
    password_input.click()
    actions = ActionChains(self.driver)
    actions.send_keys_to_element(email_input, username)
    actions.send_keys_to_element(password_input, password)
    actions.perform()
    login_input = self.waitForElementVisible((By.XPATH,login_input_Xpath))
    login_input.click()
    Pop_up_messsage_sucsesfull= self.waitForElementVisible((By.XPATH,Pop_up_messsage_Xpath))
    assert Pop_up_messsage_sucsesfull.text == Pop_up_messsage_sucsesfull_text
                                              #PROFİLE 
  @pytest.mark.skip 
  def test_profilim(self):
    self.test_login()
    tab_profile_button = self.waitForElementVisible((By.XPATH,tab_profile_button_Xpath))
    tab_profile_button.click()
    
   
    edit_profile_button = self.waitForElementVisible((By.XPATH, edit_profile_button_Xpath))
    edit_profile_button.click()
 
    selectors = {
        "Kişisel Bilgiler": "Kişisel Bilgilerim",
        "Deneyimlerim"    : "Deneyimlerim",
        "Eğitim Hayatım"  : "Eğitim Hayatım",
        "Yetkinliklerim"  : "Yetkinliklerim",
        "Sertifikalarım"  : "Sertifikalarım",
        "Medya Hesaplarım": "Medya Hesaplarım",
        "Yabancı Dillerim": "Yabancı Dillerim",
        "Ayarlar"         : "Ayarlar"
    }
    
    
    driver = self.driver  
    wait = WebDriverWait(driver, 10)  
    for section, xpath in selectors.items():
        xpath = f"//span[contains(., '{xpath}')]" #xpathleri burada yazdırdı.
        try:
            element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            assert element.is_displayed(), f"{section} bulunamadı!"
            print(f"{section} görüntülendi.")
        except AssertionError as e:
            print(f"Hata: {e}")
    assert len(selectors) == 8, "Başlık sayısı beklenenden farklı!"
  

    self.driver.execute_script(SCROLLTO)
    sleep(2)
    save_button = self.waitForElementVisible((By.XPATH,save_button_Xpath))
    save_button.click()
                                       #WARNİNG MESSAGES     
   
  def test_add_delete_profile(self):
    self.test_profilim()
    
    click_empty = self.waitForElementVisible((By.CSS_SELECTOR, "body"))
    actions = ActionChains(self.driver)
    actions.move_to_element(click_empty).move_by_offset(0, 0).click().perform()
    sleep(5)
    
    profile_photo_edit_button = self.waitForElementVisible((By.XPATH,profile_photo_edit_button_Xpath ))
    actions.move_to_element(profile_photo_edit_button).click().perform()
    sleep(5)

    profile_file_input = self.driver.find_element(By.XPATH, profile_file_input_Xpath).send_keys(file_path)
    sleep(2)
    file_load_button=self.waitForElementVisible((By.XPATH,file_load_button_Xpath)).click()
    sleep(5)
    # self.driver.switch_to.default_content()
  
    delete_photo_button = self.waitForElementVisible((By.XPATH,delete_photo_button_Xpath))
    delete_photo_button.click()
    delete_yes_button = self.waitForElementVisible((By.XPATH,delete_yes_button_Xpath))
    delete_yes_button.click()
    
    pop_up_message1_delete= self.waitForElementVisible((By.XPATH,Pop_up_messsage1_Xpath ))
    assert pop_up_message1_delete.text == Pop_up_messsage1_delete_text
    sleep(2)
    
    
  def test_drapdrop(self):
    self.test_profilim()
    
    
    actions = ActionChains(self.driver)
    profile_photo_edit_button = self.waitForElementVisible((By.XPATH,profile_photo_edit_button_Xpath ))
    actions.move_to_element(profile_photo_edit_button).click().perform()
    pyautogui.hotkey('winleft', 'down')
    sleep(2)
    
    dosya_x, dosya_y = 1473,553 
    sleep(10)
    tarayici_x, tarayici_y = 683, 380
    
    sleep(1)
    pyautogui.moveTo(dosya_x, dosya_y)
    sleep(1)
    pyautogui.mouseDown()
    sleep(2)
    pyautogui.moveTo(tarayici_x, tarayici_y)
    sleep(3)
    pyautogui.mouseUp()
    sleep(5)
    pyautogui.press("enter")
    sleep(5)
   
  def test_copy_paste(self):
    self.test_profilim()
    actions = ActionChains(self.driver)
   
    edit_profile_photo_button = self.waitForElementVisible((By.XPATH, profile_photo_edit_button_Xpath))
    actions.move_to_element(edit_profile_photo_button).click().perform()
    
    pyautogui.hotkey('winleft', 'down')
    
    dosya_x, dosya_y = 1550,553  #dosya kordinatım
    pyautogui.click(dosya_x, dosya_y)  
    pyautogui.hotkey('ctrl', 'c') 
    sleep(5)
    tarayici_x, tarayici_y = 600, 600
    pyautogui.click(tarayici_x, tarayici_y)
    pyautogui.hotkey('ctrl', 'v')
    sleep(5)
    pyautogui.press("enter")
    sleep(5)
    

   
  def test_warning_message(self):
    self.test_profilim()
    
    
    #NAME
    name_input=self.driver.find_element(By.NAME, "name")
    name_input.clear()
    # name_input.click()
    self.driver.find_element(By.NAME, "name").send_keys("ebrar")
   
    #LASTNAME
    surname_input=self.driver.find_element(By.NAME, "surname")
    surname_input.clear()
    # surname_input.click()
    self.driver.find_element(By.NAME, "surname").send_keys("tobeto")
    
    
    
    #country_flags
    sleep(2)
    self.driver.find_element(By.NAME, "phoneNumberCountry").click()
    dropdown = self.driver.find_element(By.NAME, "phoneNumberCountry")
    dropdown.find_element(By.XPATH,dropdown_Samoa ).click()
    self.driver.find_element(By.NAME, "phoneNumberCountry").click()
    dropdown = self.driver.find_element(By.NAME, "phoneNumberCountry")
    dropdown.find_element(By.XPATH,dropdown_Türkiye).click()
    
    
    #Date of birth
    self.driver.find_element(By.NAME, "birthday").click()
    self.driver.find_element(By.NAME, "birthday").send_keys("2024-04-23")
    sleep(2)
    #TC
    
    TC_number_input = self.waitForElementVisible((By.NAME, "identifier"))
    TC_number_input.click()
    TC_number_input.clear()

    TC_number_input.send_keys("9828668383")
    assert required_field_message_TC in self.driver.find_element(By.XPATH, required_field_message_TC_XPath).text
    sleep(5)
    TC_number_input.clear()
    TC_number_input.send_keys("9828668383386")

    assert required_field_message_TC1 in self.driver.find_element(By.XPATH, required_field_message_TC1_XPath).text
    self.driver.execute_script(SCROLLTO)
    sleep(2)
    #COUNTRY
        
    country_input=self.waitForElementVisible((By.NAME, "country"))
    country_input.click()
    country_input.clear()
    country_input.send_keys("T")
    assert required_field_message_Country in self.driver.find_element(By.XPATH,required_field_message_Country_XPath).text
    
    country_input.clear()
    country_input.send_keys(country_input_send_keys)
    
    assert required_field_message_Country1 in self.driver.find_element(By.XPATH, required_field_message_Country2_XPath).text
    self.driver.execute_script(SCROLLTO)
    #CİTY
    city_dropdown = self.driver.find_element(By.NAME, "city")
    city_dropdown.find_element(By.XPATH,required_field_message_City_XPath ).click()
  
    sleep(2)
    
    #DİSTRİCT
    district_dropdown = self.driver.find_element(By.NAME, "district")
    district_dropdown.click()
    district_dropdown.find_element(By.XPATH, required_field_message_District_XPath).click()
    
    #STREET
    street_input=self.waitForElementVisible((By.NAME,"address"))
    street_input.click()
    street_input.clear()
    street_input.send_keys(street_input_send_keys)
    assert required_field_about_me in self.driver.find_element(By.XPATH, required_field_message_Street_XPath).text
    sleep(5)
    #ABOUT ME
    about_me_input=self.waitForElementVisible((By.XPATH,required_field_message_about_me_XPath))
    about_me_input.click()
    about_me_input.clear()
    about_me_input.send_keys(about_me_input_send_keys)
    assert required_field_about_me1 in self.driver.find_element(By.XPATH, required_field_message_about_me_write_XPath).text
    sleep(5)
    
    
    
   
   
    

    
   
   
