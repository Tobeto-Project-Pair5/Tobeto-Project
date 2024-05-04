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

MAIL_URL = "https://mandrillapp.com/track/click/30897169/tobeto.com?p=eyJzIjoiaDNJTTNRdi03QVVRLXBiWDdDRW1hN09wTGl3IiwidiI6MSwicCI6IntcInVcIjozMDg5NzE2OSxcInZcIjoxLFwidXJsXCI6XCJodHRwczpcXFwvXFxcL3RvYmV0by5jb21cXFwvcmVzZXQtcGFzc3dvcmQ_Y29kZT1jZGY0MjNiNmI1YTc3ZDgwYWU3NGEyMmE4MTBiZTk1NjdiZWVjMDY0MDAzN2UwNGU2OTFhMGJjZDMwODU4OWM0MTRiMmQzZDM4ZWE1MDgwMmU0NDYxZjgwZjkzZWJhYmEwMTYzY2M1ZTA1YWE3MWU0NTA2NTI1NDE4Y2FhZDliZFwiLFwiaWRcIjpcImFiMmFlNGJmMjJhYTQ1ZTBiNWYxNGQzMjk4MzA3ZjRjXCIsXCJ1cmxfaWRzXCI6W1wiNTZmYWFkZGFlYjllYTVlNTkwZWM3ODczZDM2M2YwYWZjMjkyNjE3OFwiXX0ifQ"

#On hazirlik
new_password_xpath = "//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form//input[@name='password']"
password_confirmation_xpath = "//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form//input[@name='passwordConfirmation']"

new_password_send_button_xpath = "//div[@id='__next']/div[@class='bg-front-dark bg-front-width']/main/section//form//button[.='Gönder']"

#Case 3: Şifre yenileme
password_reset_succesful_alert_path = "//div[@id='__next']/div[@class='bg-front-dark bg-front-width']//div[@role='alert']/div[@class='toast-body']"
resetSuccesfulAlertText = "• Şifre sıfırlama işlemi başarılı."

#Case 4: Sifrelerin eslesmemesi
passwords_not_match_path = "//div[@id='__next']/div[@class='bg-front-dark bg-front-width']//div[@role='alert']/div[@class='toast-body']"
passwordsNotMatchText = "• Şifreler Eşleşmedi"

#Case 5: Mevcut sifrenin girilmesi
current_password_fail_xpath = "//div[@id='__next']/div[@class='bg-front-dark bg-front-width']//div[@role='alert']/div[@class='toast-body']"
currentPasswordFailText = "Mevcut şifre ve girilen şifre farklı olmalıdır."