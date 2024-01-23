# Getting Netflix content

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from chrome_options import ChromeOptions
from time import sleep
import pandas as pd

NETFLIX_USERNAME = 'magnus3@VoltVex.com'
NETFLIX_PASSWORD = 'p433837'

URL = 'https://www.netflix.com/browse/genre/34399?so=az'
chrome_options = ChromeOptions()
driver = webdriver.Chrome(options=chrome_options.get_options())
driver.get(URL)
driver.maximize_window()

login_link = driver.find_element(By.XPATH, value='//*[@id="appMountPoint"]/div/div[2]/div/div[2]/a')
login_link.click()

sleep(3)

username_input = driver.find_element(By.ID, value='id_userLoginId')
username_input.send_keys(NETFLIX_USERNAME)

password_input = driver.find_element(By.ID, value='id_password')
password_input.send_keys(NETFLIX_PASSWORD)

sleep(3)

login_button = driver.find_element(By.XPATH, value='//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
login_button.click()

sleep(3)

profile_button = driver.find_element(By.XPATH, value='//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a/div/div')
profile_button.click()

while True:
    prev_heigh = driver.execute_script('return document.body.scrollHeight')
    driver.execute_script(f'window.scrollTo(0, document.body.scrollHeight)')
    sleep(3)
    new_height = driver.execute_script('return document.body.scrollHeight')
    print(prev_heigh)
    print(new_height)
    if new_height == prev_heigh:
        print('breaking')
        break



# myNumber = 100
# print(f'{myNumber} hola')

row_number = 0
item_number = 0

while row_number <= 974:
    if item_number == 5:
        item_number = 0
    title = driver.find_element(By.XPATH, value=f'//*[@id="title-card-{row_number}-{item_number}"]/div[1]/a/div/div/p')
    print(title.text)
    row_number += 1
    item_number += 1

# //*[@id="title-card-973-0"]/div[1]/a/div/div/p
# //*[@id="title-card-973-3"]/div[1]/a/div/div/p
# //*[@id="title-card-974-1"]/div[1]/a/div/div/p