# fast smoketest
# from selenium import webdriver   # instalacja

# driver = webdriver.Chrome(executable_path='D:\AutoTests\chromedriver.exe')

from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service(executable_path="D:\AutoTests\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
title = driver.title
print(title)

assert title == 'Web form'
