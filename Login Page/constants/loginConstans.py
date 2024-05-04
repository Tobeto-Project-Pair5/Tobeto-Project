#firstName = "Pair"
#lastName = "Beş"
email = "tobeto.pair5@gmail.com"
password = "123456789"
passwordAgain = "123456789"
#telephone = "05555555555"

emptyEmail = ""
emptyPassword = ""

falseEmail = "email1234@gmail.com"
falsePassword = "sifresifre"

verificationEmail = "hanifecalkn@gmail.com"
verificationPassword = "@tobeto98@"

# verificationEmail = "tobetotobeto0@gmail.com"
# verificationPassword = "123456789"

newPassword = "1234567"
passwordConfirmation = "1234567"

falsePassword1 ="12345678"

LOGIN_URL= "https://tobeto.com/giris"

#Case 1 : Basarili giris yapildiginda
successful_login_message_xpath = "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']"
succesfulLoginMessageText = "• Giriş başarılı."

#Case 2 : E-posta veya sifre girilmediginde
required_field_xpath = "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/p"
requiredFieldText = "Doldurulması zorunlu alan*"

#Case 3 : E-posta veya sifre yanlis girildiginde
login_checkbox_email_xpath = "/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/input[@name='email']"
login_checkbox_password_xpath = "/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/input[@name='password']"
login_button_xpath = "/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form[@action='#']/button[.='Giriş Yap']"

invalid_email_password_alert = "div[class='toast-body']"
invalidEmailPasswordAlertText = "• Geçersiz e-posta veya şifre."

#Case 4 : E-posta veya sifre girilmediginde
unverified_email_alert_xpath = "/html//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//div[@role='alert']/div[@class='toast-body']"
unverifiedEmailAlertText = "Hesabınız henüz doğrulanmamış. Lütfen hanifecalkn@gmail.com adresinize ilettiğimiz doğrulama linkine tıklayın. Eğer doğrulama e-postası almadıysanız yeniden gönderebilmemiz için tıklayınız."

unverified_email_xpath = "//div[@role='alert']/div[@class='toast-body']"
unverifiedEmailText = "• Henüz e-posta adresinizi doğrulamadınız."






