base_url = "https://tobeto.com/giris"
email_xpath = "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[1]"
password_xpath = "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[2]"
login_button_xpath = "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button"
loginMessage_xpath = "//div[@id='__next']//div[@role='alert']/div[@class='toast-body']"
myProfileButton_xpath = "//div[@id='__next']//nav//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a[@href='#']"
editMyProfileButton_xpath = "//div[@id='__next']/div[@class='back-white']/main/div[@class='container']//span[@class='cv-edit-icon']"
profilimiOlusturButton_css = "[class='details pack-bg-2'] [class]"
myMediaAccountsButton_xpath = "/html//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-3 mb-8 mb-lg-0']/div/a[6]/span[@class='sidebar-text']"
saveButton_xpath = "//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']//form/button[.='Kaydet']"

# Doldurulması zorunlu alan

platformAlertMessage_css = "[class='col-md-4 col-12'] .text-danger"
urlAlertMessage_css = "[class='col-md-8 col-12'] .text-danger"

# Medya hesabı eklemek için 
platformListButton_xpath = "/html//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']//form//select[@name='socialMedia']"

#İnstagram XPATH
platformChooseButton_xpath = "//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']//form//select[@name='socialMedia']/option[@value='Instagram']"

#Twitter XPATH
platformChooseButton2_xpath = "//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']//form//select[@name='socialMedia']/option[@value='Twitter']"

#LinkedIn XPATH
platformChooseButton3_xpath = "//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']//form//select[@name='socialMedia']/option[@value='LinkedIn']"

#Behance XPATH
platformChooseButton4_xpath = "//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']//form//select[@name='socialMedia']/option[@value='Behance']"

#Dribble XPATH
platformChooseButton5_xpath = "//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']//form//select[@name='socialMedia']/option[@value='Dribble']"

#Github XPATH
platformChooseButton6_xpath = "//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']//form//select[@name='socialMedia']/option[@value='Github']"

#link eklemek için

platformUrlAdd_xpath = "/html//div[@id='__next']/div[@class='back-white']/main/section//div[@class='col-12 col-lg-9']//form//input[@name='socialMediaUrl']"

#Medya hesabı eklendi uyarısı 
accountAddedAlert_css = "div[role='alert'] > .toast-body"

#Medya hesabı silindi uyarısı
accountDeletedAlert_css = "div[role='alert'] > .toast-body"

#En fazla 3 adet medya seçimi yapılabilir uyarısı.
max3alerts_css = "[class='col-12 col-lg-9'] span"

#Aynı sosyal medya hesabı eklenemez uyarısı.
ayniHesapEklemeUyarisi_css = "div[role='alert'] > .toast-body"

#Hesap bilgisi güncelleme.
editAccountInformation_css = "div:nth-of-type(1) > .section-header.tobeto-input > .btn > .fa.fa-pencil-square"

#url düzenle.
editUrl_xpath = "//body/div[@role='dialog']/div/div[@class='modal-content']//form//input[@value='https://www.instagram.com']"

#güncelle buton
update_xpath = "//body/div[@role='dialog']/div//div[@class='modal-footer']/button[1]"

# Forbidden hatası
forbiddenAlert_css = "div[role='alert'] > .toast-body"

# sil butonu 
deleteButton_xpath = "//div[@id='__next']/div[@class='back-white']/main/section/div[@class='container']//div[@class='col-12 col-lg-9']/div[1]/div[@class='section-header tobeto-input']/btn[@class='btn social-delete']"
# silButton_xpath = "//div[@id='__next']/div[@class='back-white']/main/section/div[@class='container']//div[@class='col-12 col-lg-9']/div[2]/div[@class='section-header tobeto-input']/btn[@class='btn social-delete']"
deleteButton2_xpath = "//div[@id='__next']/div[@class='back-white']/main/section/div[@class='container']//div[@class='col-12 col-lg-9']/div[2]/div[@class='section-header tobeto-input']/btn[@class='btn social-delete']"
deleteButton3_xpath = "//div[@id='__next']/div[@class='back-white']/main/section/div[@class='container']//div[@class='col-12 col-lg-9']/div[3]/div[@class='section-header tobeto-input']/btn[@class='btn social-delete']"
deleteAlert_css = "[class='alert-message mx-3']"
deleteAlert2_css = "[class='alert-message-light mx-3']"
yesButton_xpath = "//body/div[@role='dialog']/div[@class='modal-dialog modal-dialog-centered']/div[@class='modal-content']//button[@class='btn btn-yes my-3']"
silindiUyari_css = "div[role='alert'] > .toast-body"