BASE_URL = "https://tobeto.com/"
LOGIN_URL= "https://tobeto.com/giris"
PLATFORM_URL= "https://tobeto.com/platform"

email_tuba= "mihraa777@gmail.com"
password_tuba= "123456"


#Login
login_input_button = "/html/body/div[1]/div/section[1]/nav/div/div/a[1]"
login_email_input = "//*[@id='__next']/div/main/section/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[1]/input"
login_password_input = "//*[@id='__next']/div/main/section/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/input"
email_xpath = "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[1]"
password_xpath = "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[2]"
login_button_xpath = "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button"
alert_login_text ="//div[@id='__next']/div[@class='back-white']//div[@role='alert']//button[@type='button']"

#Profile
my_profile_edit= ".cv-edit-icon"
my_profile_page = "//div[@id='__next']//nav//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a[@href='#']"
alert_login_text ="//div[@id='__next']/div[@class='back-white']//div[@role='alert']//button[@type='button']"
# profile_page ="/html/body/div[1]/div/nav/div[1]/ul/li[2]/a"


#Competences
my_competences_xpath = "/html//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-3 mb-8 mb-lg-0']/div/a[4]/span[@class='sidebar-text']"
alert_competency_not_added = "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']"
section_competence = "/html/body/div[1]/div/main/section/div/div/div[2]/div[1]/div/div/div/div[1]/div[2]"
save_competence_button = "/html/body/div[1]/div/main/section/div/div/div[2]/button"
delete_competence_icon = "#__next > div > main > section > div > div > div.col-12.col-lg-9 > div.col-12 > div:nth-child(1) > div > span"
delete_competence_choose_button = "body > div.fade.alert-modal.modal.show > div > div"
alert_competence_deleted = "alert_competence_deleted"
alert_competence_added="div[role='alert'] > .toast-body"
yes_button_id = "body > div.fade.alert-modal.modal.show > div > div > div > div > div > div.alert-buttons > button.btn.btn-yes.my-3"
competence_see_icon ="#__next > div > main > div > div:nth-child(2) > div.col-md-4.col-12 > div > div:nth-child(3) > div > div.cv-box-header > div > span.cv-see-icon"
