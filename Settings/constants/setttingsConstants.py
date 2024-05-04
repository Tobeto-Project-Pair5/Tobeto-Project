BASE_URL = "https://tobeto.com/"
LOGIN_URL= "https://tobeto.com/giris"
PLATFORM_URL= "https://tobeto.com/platform"

email_tuba= "mihraa777@gmail.com"
password_tuba="123456"

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
# profile_page ="/html/body/div[1]/div/nav/div[1]/ul/li[2]/a"


#Settings 
settings_button_xpath= "//*[@id='__next']/div/main/section/div/div/div[1]/div/a[8]"
old_password_xpath="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input"
new_password_xpath="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input"
new_password_again_xpath="//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input"
change_password_button="//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[1]/button"
alert_password_empty="//*[@id='__next']/div/div[2]/div/div[2]"
alert_old_wrong_password="//*[@id='__next']/div/div[2]/div/div[2]"
alert_short_password="//*[@id='__next']/div/div[2]/div/div[2]"
alert_password_not_match="//*[@id='__next']/div/div[2]/div/div[2]"
alert_password_match="//*[@id='__next']/div/div[2]/div/div[2]"
alert_password_not_same="//*[@id='__next']/div/div[2]/div/div[2]"
membership_termination_button="#__next > div > main > section > div > div > div.col-12.col-lg-9 > div > div > div:nth-child(2) > button"
account_deleted_win ="body > div.fade.alert-modal.modal.show > div > div > div > div > div > div.alert-buttons > button.btn.btn-yes.my-3"
delete_account_choose_button="/html/body/div[4]/div/div"
account_yes_button_id="body > div.fade.alert-modal.modal.show > div > div > div > div > div > div.alert-buttons > button.btn.btn-yes.my-3"
alert_account_deleted="//div[@id='__next']//div[@role='alert']/div[@class='toast-body']"