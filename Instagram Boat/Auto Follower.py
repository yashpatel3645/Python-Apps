from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

ids = open('id.txt')
password = open('password.txt')

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(5)

for i in ids:
    