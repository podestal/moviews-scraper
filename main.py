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

movies = {}

URL = 'https://www.netflix.com/browse/genre/34399?so=az'
chrome_options = ChromeOptions()
driver = webdriver.Chrome(options=chrome_options.get_options())
# driver.get(URL)
# driver.maximize_window()

# login_link = driver.find_element(By.XPATH, value='//*[@id="appMountPoint"]/div/div[2]/div/div[2]/a')
# login_link.click()

# sleep(3)

# username_input = driver.find_element(By.ID, value='id_userLoginId')
# username_input.send_keys(NETFLIX_USERNAME)

# password_input = driver.find_element(By.ID, value='id_password')
# password_input.send_keys(NETFLIX_PASSWORD)

# sleep(3)

# login_button = driver.find_element(By.XPATH, value='//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
# login_button.click()

# sleep(3)

# profile_button = driver.find_element(By.XPATH, value='//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a/div/div')
# profile_button.click()

# sleep(3)

# while True:
#     prev_heigh = driver.execute_script('return document.body.scrollHeight')
#     driver.execute_script(f'window.scrollTo(0, document.body.scrollHeight)')
#     sleep(3)
#     new_height = driver.execute_script('return document.body.scrollHeight')
#     if new_height == prev_heigh:
#         print('breaking')
#         break

# row_number = 0
# item_number = 0

# while row_number <= 648:
#     if item_number == 6:
#         item_number = 0
#         row_number += 1
#     if row_number == 648:
#         break
#     title = driver.find_element(By.XPATH, value=f'//*[@id="title-card-{row_number}-{item_number}"]/div[1]/a/div/div/p')
#     movies[title.text] = 'netflix'
#     print(title.text)
#     print(row_number)
#     print(item_number)
#     item_number += 1

DISNEY_URL = 'https://www.disneyplus.com/identity/login/enter-email'

driver.get(DISNEY_URL)
driver.maximize_window()

username = 'l.r.p.2991@gmail.com'
password = '13anguloX'

sleep(3)

email = driver.find_element(By.ID, value='email')
email.send_keys(username)

continue_button = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div/div/div/div[2]/div/form/button')
continue_button.click()

sleep(3)

password_input = driver.find_element(By.XPATH, value='//*[@id="password"]')
password_input.send_keys(password)

sleep(3)

login_button = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div/div/div/div[2]/div/form/button')
login_button.click()

sleep(20)

profile_button = driver.find_element(By.XPATH, value='//*[@id="remove-main-padding_index"]/div/div/section/ul/div[1]/div/div')
profile_button.click()

sleep(10)

driver.get('https://www.disneyplus.com/en-gb/movies/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4')

# # //*[@id="title-card-973-0"]/div[1]/a/div/div/p
# # //*[@id="title-card-973-3"]/div[1]/a/div/div/p
# # //*[@id="title-card-974-1"]/div[1]/a/div/div/p

print(movies) 