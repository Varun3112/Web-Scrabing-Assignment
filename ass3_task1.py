from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("Enter username")
user = input()
print("Enter password")
password = input()

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://moodle.iitd.ac.in/login/index.php")

driver.find_element_by_id('username').send_keys(user)
driver.find_element_by_id('password').send_keys(password)

login = driver.find_element_by_id("login")

numbers = []
for word in login.text.split():
   if word.isdigit():
      numbers.append(int(word))

n1 = numbers[0]
n2 = numbers[1]

if "add" in login.text:
    captcha = n1 + n2
elif "subtract" in login.text:
    captcha = n1 - n2
elif "first" in login.text:
    captcha = n1
elif "second" in login.text:
    captcha = n2

driver.find_element_by_id("valuepkg3").clear()
driver.find_element_by_id("valuepkg3").send_keys(captcha)

driver.find_element_by_id('loginbtn').click()




