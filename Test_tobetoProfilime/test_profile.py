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
from PIL import Image
import os



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
  
  @pytest.mark.skip
  def test_login(self):  
    email_input = self.waitForElementVisible((By.XPATH, email_input_Xpath))
    email_input.click()
    password_input = self.waitForElementVisible((By.XPATH,password_input_Xpath ))
    password_input.click()
    actions = ActionChains(self.driver)
    actions.send_keys_to_element(email_input, username)
    actions.send_keys_to_element(password_input, password)
    actions.perform()
    login_input = self.waitForElementVisible((By.XPATH,login_form_Xpath ))
    login_input.click()
    sucsesfullmessage= self.waitForElementVisible((By.XPATH,sucsesfull_message_Xpath ))
    assert sucsesfullmessage.text == sucsesfull_message  
  
  def test_profilim(self):
    self.test_login()
    tab_profile_button = self.waitForElementVisible((By.XPATH,tab_profile_button_Xpath ))
    tab_profile_button.click()
   
   

   
    episode1=self.waitForElementVisible((By.XPATH,episode1_Xpath ))
    assert episode1.is_displayed(), "bölüm görüntülenemedi." #bölümün görüntülendiğini kontrol etmek için kullanılır.
    episode2=self.waitForElementVisible((By.XPATH,episode2_Xpath ))
    assert episode2.is_displayed(), "bölüm görüntülenemedi."
    
    edit_profile_button=self.waitForElementVisible((By.XPATH,edit_profile_button_Xpath))
    assert edit_profile_button.is_displayed(),"düzenle ikonu görüntülenmedi."
    
    share_button=self.waitForElementVisible((By.ID, "dropdown-basic"))
    assert share_button.is_displayed(),"paylaşım ikonu görüntülenmedi." 
  
    share_button=self.waitForElementVisible((By.ID, "dropdown-basic")).click()
    share_profile_button=self.waitForElementVisible((By.CSS_SELECTOR, ".react-switch-handle"))
    assert share_profile_button.is_displayed(),"profile paylaşımı görüntülenemedi"
    copy_icon=self.waitForElementVisible((By.CSS_SELECTOR, ".exw-widget-container > div"))
    assert copy_icon.is_displayed(),"kopyalama ikonu görüntülenemedi"
    bostikla=self.waitForElementVisible((By.CSS_SELECTOR, "main"))
    bostikla.click()
   

    user_information=self.driver.find_elements(By.CSS_SELECTOR, "div.cv-info.cv-padding info-box span.header")
    user_information_expected = ["Ad Soyad","Doğum Tarihi","E-Posta Adresi","Telefon Numarası"]
    for i, tab in enumerate(user_information): #enumarete  elemanın hem kendisine hemde indeks numarasına aynı anda erişim sağlamak için kullanılır.
     assert tab.text == user_information_expected[i], f"başlık ismi beklenen ile uyuşmuyor: {tab.text}"
   
    menu=self.driver.find_elements(By.CSS_SELECTOR, "#__next > div > main > div > div:nth-child(2) > div.col-md-4.col-12 > div > div:nth-child(2) > div > div > span")
    menu_expected=["Hakkımda"]
    for i, tab in enumerate(menu): 
      assert tab.text == menu_expected[i], f"başlık ismi beklenen ile uyuşmuyor: {tab.text}"
    ##################################################################
    self.driver.execute_script("window.scrollTo(0,800)")
    view_content = self.driver.find_elements(By.CSS_SELECTOR, "div.cv-box.cv-padding p#user_desc.cv-desc")
    view_content_expected = ["Html kodlama biliyorum. Evde web site yapıyorum yayınlıyorum."]
    for i, content in enumerate(view_content): 
      assert content.text == view_content_expected[i], f"İçerik beklenen ile uyuşmuyor: {content.text}"
      print(f"{content.text} görüntülendiğini ekrana yazdır")
    menu1 = self.driver.find_elements(By.CSS_SELECTOR, "#__next > div > main > div > div:nth-child(2) > div.col-md-4.col-12 > div > div:nth-child(3) > div > div.cv-box-header > div > span")
    menu_expected1 = ["Yetkinliklerim"]
    for i, tab in enumerate(menu1): 
      actual_text = tab.text  # 'get_attribute("actual_text")' yerine 'tab.text' kullanılmalı
      assert actual_text == menu_expected1[i], f"Menü öğesi beklenen ile uyuşmuyor: {actual_text}"
    sleep(1)
    
    current_url = self.driver.current_url
    if "tobeto.com" in current_url:
     print(f"Test başarılı: {current_url}")  # Eğer varsa, test başarılıdır ve URL'yi yazdır
    else:
     print(f"Test başarısız. Beklenen URL: 'tobeto.com'. Alınan URL: '{current_url}'")
     
     # Ekran görüntüsünü al ve "screenshot.png" adıyla kaydet
    self.driver.execute_script("window.scrollTo(0,800)")
    self.driver.save_screenshot("screenshot.png")
    
    sleep(1)
      
    screenshot = Image.open("screenshot.png")
    screenshot.show()
    sleep(3)
   
    self.driver.execute_script("window.scrollTo(0,900)")
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".text-truncate:nth-child(1)").click()
    sleep(5)
    self.driver.get("https://tobeto.com/profilim")

    
    
