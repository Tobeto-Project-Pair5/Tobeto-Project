import pyautogui



print("Farenizi dosyanın üzerine götürün ve bir tuşa basın...")
input()

# Şu anki fare konumunu alın
fare_x, fare_y = pyautogui.position()

# Elde edilen X ve Y koordinatlarını yazdırın
print("Dosyanın X koordinatı:", fare_x)
print("Dosyanın Y koordinatı:", fare_y)