from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

ids = open('id.txt')
password = open('password.txt')

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(5)
# link = input("Input Link to Start Auto Liker: ")

for i in ids:
    browser.get("https://www.instagram.com/p/CARjfQ3jZ-i/")
    login_link = browser.find_element_by_xpath("//a[text()='Log in']")
    login_link.click()

    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys(i)
    for p in password:
        password_input.send_keys(p)
        break
    try:
        browser.find_element_by_xpath("//button[@type='submit']").click()
    except:
        pass
    browser.find_element_by_class_name("wpO6b ").click()
    browser.get("https://www.instagram.com/"+i+"/")
    browser.find_element_by_class_name("wpO6b ").click()
    # browser.find_element_by_class_name("RnEpo Yx5HN    ").find_element_by_xpath("//a[text()='Log Out']").click()
    browser.find_element_by_class_name("RnEpo").find_element_by_class_name("pbNvD").find_element_by_class_name("piCib").find_element_by_class_name("mt3GC").find_element_by_xpath("//button[text()='Log Out']").click()
    browser.get("https://www.instagram.com/p/CARjfQ3jZ-i/")
