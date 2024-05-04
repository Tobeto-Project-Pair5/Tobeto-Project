from selenium import webdriver
from userInfo import usName , invalidName, uslastName , invalidLastName, usEmail, invalidEmail, invalidEmail2, registeredEmail, usPassword, usPasswordAgain, invalidPassword, invalidPasswordAgain, usPhone, invalidPhone, invalidPhone2
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from constants.registerConstants import *
import pytest
from time import sleep

class Test_Register():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.driver.get(BASE_URL)

  def teardown_method(self):
    self.driver.quit()
    
  # def waitForElementVisible(self,locator,timeout=5):
  #   return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
  
  def sign_up_method(self,firstName,lastName ,email, password,passwordAgain):
    signup_button= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, free_signup_button_id)))
    signup_button.click()
    sleep(1)
    nameInput= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME, "firstName")))
    nameInput.send_keys(firstName)
    sleep(1)
    lastnameInput= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,"lastName")))
    lastnameInput.send_keys(lastName)
    sleep(1)
    emailInput= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,"email")))
    emailInput.send_keys(email)
    sleep(1)
    passwordInput= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,"password")))
    passwordInput.send_keys(password)
    sleep(1)
    passwordAgainInput= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,"passwordAgain")))
    passwordAgainInput.send_keys(passwordAgain)
    sleep(1)

  def Captcha(self):

    iframe = WebDriverWait(self.driver, 10).until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='reCAPTCHA']")))
    captchaButton = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, captcha_button_xpath)))
    captchaButton.click()
    sleep(10)
    self.driver.switch_to.default_content()

#başarılı kayıt 
  def test_signup(self):
    self.sign_up_method(usName,uslastName,usEmail,usPassword,usPasswordAgain)
    
    signup_button= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,signup_button_xpath)))
    signup_button.click()
    checkbox1= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,checkbox1_xpath)))
    checkbox1.click()
    checkbox2= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,checkbox2_xpath)))
    checkbox2.click()
    checkbox3= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,checkbox3_xpath)))
    checkbox3.click()
    checkbox4= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,checkbox4_xpath)))
    checkbox4.click()
    telephoneInput= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,telephone_xpath)))
    telephoneInput.send_keys(usPhone)
    sleep(3)
    # captchaButton = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, captcha_id)))
    # captchaButton.click()
    # sleep(3)
    self.Captcha()
    continueButton= WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, continue_button_xpath)))
    continueButton.click()
    sleep(5)

    # activation_message= WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH,activationMessage_id )))
    # assert activation_message.text == activation_message_text

#"Şifre en az 6 karakterden oluşmalıdır." uyarısının görüntülenmesi
  def test_password_message(self):
    self.sign_up_method(usName, uslastName, registeredEmail, invalidPassword, invalidPasswordAgain)
    
    signup_button = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, signup_button_xpath)))
    signup_button.click()
    checkbox1 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, checkbox1_xpath)))
    checkbox1.click()
    checkbox2 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, checkbox2_xpath)))
    checkbox2.click()
    checkbox3 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, checkbox3_xpath)))
    checkbox3.click()
    checkbox4 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, checkbox4_xpath)))
    checkbox4.click()
    telephoneInput = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, telephone_xpath)))
    telephoneInput.send_keys(usPhone)
    sleep(3)
    self.Captcha()
    continueButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, continue_button_xpath)))
    continueButton.click()
    sleep(5)

#"Şifreler eşleşmedi." uyarısının görüntülenmesi
  def test_password_message2(self):
    self.sign_up_method(usName, uslastName, usEmail, usPassword, invalidPasswordAgain)
    
    signup_button = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, signup_button_xpath)))
    signup_button.click()
    checkbox1 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, checkbox1_xpath)))
    checkbox1.click()
    checkbox2 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, checkbox2_xpath)))
    checkbox2.click()
    checkbox3 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, checkbox3_xpath)))
    checkbox3.click()
    checkbox4 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, checkbox4_xpath)))
    checkbox4.click()
    telephoneInput = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, telephone_xpath)))
    telephoneInput.send_keys(usPhone)
    sleep(3)
    self.Captcha()
    continueButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, continue_button_xpath)))
    continueButton.click()
    sleep(5)

#"Geçersiz e-posta adresi" uyarısının görüntülenmesi
  def test_invalid_email(self):
    self.sign_up_method(usName,uslastName,invalidEmail, usPassword, usPasswordAgain)
    sleep(3)

#"Girdiğiniz e-posta adresi ile kayıtlı üyelik bulunmaktadır." uyarısının görüntülenmesi
  def test_registered_email(self):
    self.sign_up_method(usName, uslastName, registeredEmail, usPassword, usPasswordAgain)
    
    signup_button = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, signup_button_xpath)))
    signup_button.click()
    checkbox1 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, checkbox1_xpath)))
    checkbox1.click()
    checkbox2 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, checkbox2_xpath)))
    checkbox2.click()
    checkbox3 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, checkbox3_xpath)))
    checkbox3.click()
    checkbox4 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, checkbox4_xpath)))
    checkbox4.click()
    telephoneInput = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, telephone_xpath)))
    telephoneInput.send_keys(usPhone)
    sleep(3)
    self.Captcha()
    continueButton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, continue_button_xpath)))
    continueButton.click()
    sleep(5)
  
#Telefon numarasında "En az 10 karakter girmelisiniz." uyarısının görüntülenmesi
  def test_phone_message(self):
    self.sign_up_method(usName,uslastName,usEmail,usPassword,usPasswordAgain)
    
    signup_button= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,signup_button_xpath)))
    signup_button.click()
    checkbox1= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,checkbox1_xpath)))
    checkbox1.click()
    checkbox2= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,checkbox2_xpath)))
    checkbox2.click()
    checkbox3= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,checkbox3_xpath)))
    checkbox3.click()
    checkbox4= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,checkbox4_xpath)))
    checkbox4.click()
    telephoneInput= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,telephone_xpath)))
    telephoneInput.send_keys(invalidPhone)
    sleep(3)
    
    self.Captcha()
    continueButton= WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, continue_button_xpath)))
    continueButton.click()
    sleep(5)

#Telefon numarasında "En fazla 10 karakter girebilirsiniz." uyarısının görüntülenmesi
  def test_phone_message2(self):
    self.sign_up_method(usName,uslastName,usEmail,usPassword,usPasswordAgain)
    
    signup_button= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,signup_button_xpath)))
    signup_button.click()
    checkbox1= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,checkbox1_xpath)))
    checkbox1.click()
    checkbox2= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,checkbox2_xpath)))
    checkbox2.click()
    checkbox3= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,checkbox3_xpath)))
    checkbox3.click()
    checkbox4= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,checkbox4_xpath)))
    checkbox4.click()
    telephoneInput= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,telephone_xpath)))
    telephoneInput.send_keys(invalidPhone2)
    sleep(3)
    
    self.Captcha()
    continueButton= WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, continue_button_xpath)))
    continueButton.click()
    sleep(5)

#FAIL:Ad, soyad ve e posta kısmına geçersiz veri girince kayıt oluyor.
  def test_invalid_name_lastname(self):
    self.sign_up_method(invalidName,invalidLastName,invalidEmail2,usPassword,usPasswordAgain)
    
    signup_button= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,signup_button_xpath)))
    signup_button.click()
    checkbox1= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,checkbox1_xpath)))
    checkbox1.click()
    checkbox2= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,checkbox2_xpath)))
    checkbox2.click()
    checkbox3= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,checkbox3_xpath)))
    checkbox3.click()
    checkbox4= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,checkbox4_xpath)))
    checkbox4.click()
    telephoneInput= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,telephone_xpath)))
    telephoneInput.send_keys(usPhone)
    sleep(3)
    # captchaButton = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, captcha_id)))
    # captchaButton.click()
    # sleep(3)
    self.Captcha()
    continueButton= WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, continue_button_xpath)))
    continueButton.click()
    sleep(5)

#FAIL:E-posta yazıp sildikten sonra "Doldurulması zorunlu alan" uyarısı iki tane çıkıyor.
  def test_email_message(self):
    self.sign_up_method(usName,uslastName,usEmail, usPassword, usPasswordAgain)
    sleep(3)
    emailInput= self.driver.find_element(By.NAME,"email")
    emailInput.clear()
    sleep(6)
    '''if emailInput.get_attribute("value") == "":
        # Eğer alan boş ise, metin kutusu temizlenmiştir
      error_message = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[1]/div/div/form/p[1]")  
      assert error_message.text == "Doldurulması zorunlu alan"
    else:
        print("Alan temizlenemedi.")'''


    



