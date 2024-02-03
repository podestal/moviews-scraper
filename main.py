# Getting Netflix content

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from chrome_options import ChromeOptions
from time import sleep
import pandas as pd
import json


NETFLIX_USERNAME = 'magnus3@VoltVex.com'
NETFLIX_PASSWORD = 'p433837'

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

# driver.get(DISNEY_URL)
# driver.maximize_window()

# username = 'l.r.p.2991@gmail.com'
# password = '13anguloX'

# sleep(10)

# email = driver.find_element(By.ID, value='email')
# email.send_keys(username)

# continue_button = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div/div/div/div[2]/div/form/button')
# continue_button.click()

# sleep(10)

# password_input = driver.find_element(By.XPATH, value='//*[@id="password"]')
# password_input.send_keys(password)

# sleep(10)

# login_button = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div/div/div/div[2]/div/form/button')
# login_button.click()

# sleep(20)

# For profiles

# profile_button = driver.find_element(By.XPATH, value='//*[@id="remove-main-padding_index"]/div/div/section/ul/div[1]/div/div')
# profile_button.click()

# sleep(20)

# driver.get('https://www.disneyplus.com/en-gb/movies/9f7c38e5-41c3-47b4-b99e-b5b3d2eb95d4')

# sleep(20)

# while True:
#     prev_heigh = driver.execute_script('return document.body.scrollHeight')
#     driver.execute_script(f'window.scrollTo(0, document.body.scrollHeight)')
#     sleep(5)
#     new_height = driver.execute_script('return document.body.scrollHeight')
#     if new_height == prev_heigh:
#         print('breaking')
#         break

# all_titles = driver.find_elements(By.XPATH, value='//*[@id="section_index"]/article/div[2]/div/div/div/div/div')

# item_number = 1
# total_titles = len(all_titles)

# while item_number <= total_titles:
#     title = driver.find_element(By.XPATH, value=f'//*[@id="section_index"]/article/div[2]/div/div/div/div/div[{item_number}]/a/div')
#     movies[title.get_attribute('alt')] = 'disney'
#     item_number += 1


# paramount

# PARAMOUNT_URL = 'https://www.paramountplus.com/movies/'

# USERNAME = 'cuentastreaming29010@gmail.com'
# PASSWORD = 'zavastech100290'

# driver.get(PARAMOUNT_URL)
# driver.maximize_window()

# Credentials scraping

# username_input = driver.find_element(By.XPATH, value='//*[@id="email"]')
# username_input.send_keys(USERNAME)

# password_input = driver.find_element(By.XPATH, value='//*[@id="password"]')
# password_input.send_keys(PASSWORD)

# sleep(10)

# submit = driver.find_element(By.XPATH, value='//*[@id="sign-in-form"]/div/div[3]/button')
# submit.click()

# sleep(10)

# profile = driver.find_element(By.XPATH, value='//*[@id="who-s-watching"]/ul/li[5]/div[1]/div')
# profile.click()

# while True:
#     prev_heigh = driver.execute_script('return document.body.scrollHeight')
#     driver.execute_script(f'window.scrollTo(0, document.body.scrollHeight)')
#     sleep(5)
#     new_height = driver.execute_script('return document.body.scrollHeight')
#     if new_height == prev_heigh:
#         print('breaking')
#         break

# item_number = 1
# all_titles = driver.find_elements(By.XPATH, value='//*[@id="main-container"]/section[1]/div/article')

# while item_number <= len(all_titles):
#     title = driver.find_element(By.XPATH, value=f'//*[@id="main-container"]/section[1]/div/article[{item_number}]/a/div/img')
#     movies[title.get_attribute('alt')] = 'paramount'
#     item_number += 1

# PRIME_URL = 'https://www.justwatch.com/pe/proveedor/amazon-prime-video?monetization_types=flatrate'

# driver.get(PRIME_URL)
# driver.maximize_window()

# sleep(5)

# while True:
#     prev_heigh = driver.execute_script('return document.body.scrollHeight')
#     driver.execute_script(f'window.scrollTo(0, document.body.scrollHeight)')
#     sleep(5)
#     new_height = driver.execute_script('return document.body.scrollHeight')
#     if new_height == prev_heigh:
#         print('breaking')
#         break

# item_number = 1
# all_titles = driver.find_elements(By.XPATH,value='//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div')

# while item_number < len(all_titles):
#     try:
#         title = driver.find_element(By.XPATH, value=f'//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[{item_number}]/a/span/div/picture/img')
#         movies[title.get_attribute('alt')] = 'prime'
#     except:
#         print('error')
#     item_number += 1
    
    # movies[title.get_attribute('alt')] = 'prime'
# //*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[181]/a/span/div/picture/img
# //*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[2]/a/span/div/picture/img
# //*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[2]/a/span/div/picture/img
# //*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[3]/a/span/div/picture/img
# //*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[13]/a/span/div/picture/img
# //*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[73]/a/span/div/picture/img

# total 100

JUSTWATCH_URL = 'https://www.justwatch.com/pe'
NETFLIX_URL = 'https://www.justwatch.com/pe/proveedor/netflix?monetization_types=flatrate&sort_by=title'
DISNEY_URL = 'https://www.justwatch.com/pe/proveedor/disney-plus?monetization_types=flatrate&sort_by=title'
PRIME_URL = 'https://www.justwatch.com/pe/proveedor/amazon-prime-video?monetization_types=flatrate&sort_by=title'
PARAMOUNT = 'https://www.justwatch.com/pe/proveedor/paramount-plus?monetization_types=flatrate&sort_by=title'
HBO_URL = 'https://www.justwatch.com/pe/proveedor/hbo-max?monetization_types=flatrate&sort_by=title'

driver.get(JUSTWATCH_URL)
driver.maximize_window()


login = driver.find_element(By.XPATH, value='//*[@id="app"]/div[3]/div/div[2]/div[2]/div[1]/div/button/div/span')
login.click()

sleep(3)

langauge_button = driver.find_element(By.XPATH, value='/html/body/ion-modal/div[2]/div/ion-content/div/div/div[2]/button[2]')
langauge_button.click()

sleep(5)

english_us_button = driver.find_element(By.XPATH, value='/html/body/ion-modal/div[2]/div/ion-content/div/div/div/div[12]')
driver.execute_script("arguments[0].click();", english_us_button)

sleep(5)

close_button = driver.find_element(By.XPATH, value='/html/body/ion-modal/div[2]/div/ion-header/ion-toolbar/ion-buttons[2]/ion-button')
close_button.click()

sleep(5)

driver.get(NETFLIX_URL)
movies = {}
spanish_movies = {}
item_number = 1

# while True:
#     prev_heigh = driver.execute_script('return document.body.scrollHeight')
#     driver.execute_script(f'window.scrollTo(0, document.body.scrollHeight)')
#     sleep(5)
#     new_height = driver.execute_script('return document.body.scrollHeight')
#     if new_height == prev_heigh:
#         print('breaking')
#         break

all_titles = driver.find_elements(By.XPATH,value='//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div')
spanish_titles = []

while item_number <= len(all_titles):
    try:
        original_title_element = driver.find_element(By.XPATH, value=f'//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[{item_number}]/a/div/picture/img')
        original_title = original_title_element.get_attribute('alt')
        title_element= driver.find_element(By.XPATH, value=f'//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[{item_number}]/a')
        title = title_element.get_attribute('href').split('/')[-1].replace('-', ' ')
        if movies.get(title):
            movies[title]['streaming'].append('netflix')
        else:
            print(f'Adding {title} and {original_title}')
            movies[title] = {'streaming': ['netflix'], 'original_title': original_title, 'spanish_title_one': '#', 'spanish_title_two': '#'}
    except:
        print('error')
    item_number += 1

login = driver.find_element(By.XPATH, value='//*[@id="app"]/div[3]/div/div[2]/div[2]/div[1]/div/button/div/span')
login.click()

sleep(5)

langauge_button = driver.find_element(By.XPATH, value='/html/body/ion-modal/div[2]/div/ion-content/div/div/div[2]/button[2]')
langauge_button.click()

sleep(5)

spanish_latin_button = driver.find_element(By.XPATH, value='/html/body/ion-modal/div[2]/div/ion-content/div/div/div/div[15]')
driver.execute_script("arguments[0].click();", spanish_latin_button)

sleep(5)

close_button = driver.find_element(By.XPATH, value='/html/body/ion-modal/div[2]/div/ion-header/ion-toolbar/ion-buttons[2]/ion-button')
close_button.click()
    
sleep(5)

# while True:
#     prev_heigh = driver.execute_script('return document.body.scrollHeight')
#     driver.execute_script(f'window.scrollTo(0, document.body.scrollHeight)')
#     sleep(5)
#     new_height = driver.execute_script('return document.body.scrollHeight')
#     if new_height == prev_heigh:
#         print('breaking')
#         break

item_number = 1
all_titles = driver.find_elements(By.XPATH,value='//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div')

while item_number < len(all_titles):
    
    try:
        title_element = driver.find_element(By.XPATH, value=f'//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[{item_number}]/a/div/picture/img')
        spanish_title_one = title_element.get_attribute('data-src').split('/')[-1].replace('-', ' ')
        spanish_title_two = title_element.get_attribute('alt')

        # if spanish_movies.get(spanish_title_one):
        #     print('spanish title exist')
        # else:
        #     spanish_movies[spanish_title_one] = spanish_title_two
        #     spanish_titles.append(f'{spanish_title_one}, {spanish_title_two}')
        #     print('spanish title does not exist')
        if movies.get(spanish_title_one):
            movies[spanish_title_one]['spanish_title_one'] = spanish_title_one
            movies[spanish_title_one]['spanish_title_two'] = spanish_title_two
        elif movies.get(spanish_title_two):
            movies[spanish_title_two]['spanish_title_one'] = spanish_title_one
            movies[spanish_title_two]['spanish_title_two'] = spanish_title_two
    except:
        print('error')
    item_number += 1

# driver.get(DISNEY_URL)

# sleep(5)

# while True:
#     prev_heigh = driver.execute_script('return document.body.scrollHeight')
#     driver.execute_script(f'window.scrollTo(0, document.body.scrollHeight)')
#     sleep(5)
#     new_height = driver.execute_script('return document.body.scrollHeight')
#     if new_height == prev_heigh:
#         print('breaking')
#         break

# item_number = 1
# all_titles = driver.find_elements(By.XPATH,value='//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div')

# while item_number < len(all_titles):
#     try:
#         title_element = driver.find_element(By.XPATH, value=f'//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[{item_number}]/a/div/picture/img')
#         title = title_element.get_attribute('alt')
#         spanish_title_element = driver.find_element(By.XPATH, value=f'//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[{item_number}]/a')
#         spanish_title = spanish_title_element.get_attribute('href').split('/')[-1].replace('-', ' ')
#         if movies.get(title):
#             movies[title].append('disney')
#             print('title exist')
#         else:
#             movies[title] = ['disney']
#             spanish_titles.append(spanish_title)
#             print('title does not exist')
#     except:
#         print('error')
#     item_number += 1

# sleep(5)

# driver.get(PRIME_URL)

# sleep(5)

# while True:
#     prev_heigh = driver.execute_script('return document.body.scrollHeight')
#     driver.execute_script(f'window.scrollTo(0, document.body.scrollHeight)')
#     sleep(5)
#     new_height = driver.execute_script('return document.body.scrollHeight')
#     if new_height == prev_heigh:
#         print('breaking')
#         break

# item_number = 1
# all_titles = driver.find_elements(By.XPATH,value='//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div')

# while item_number < len(all_titles):
#     try:
#         title_element = driver.find_element(By.XPATH, value=f'//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[{item_number}]/a/div/picture/img')
#         title = title_element.get_attribute('alt')
#         spanish_title_element = driver.find_element(By.XPATH, value=f'//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[{item_number}]/a')
#         spanish_title = spanish_title_element.get_attribute('href').split('/')[-1].replace('-', ' ')
#         if movies.get(title):
#             movies[title].append('prime')
#             print('title exist')
#         else:
#             movies[title] = ['prime']
#             spanish_titles.append(spanish_title)
#             print('title does not exist')
#     except:
#         print('error')
#     item_number += 1

# sleep(5)

# driver.get(PARAMOUNT)

# sleep(5)

# while True:
#     prev_heigh = driver.execute_script('return document.body.scrollHeight')
#     driver.execute_script(f'window.scrollTo(0, document.body.scrollHeight)')
#     sleep(5)
#     new_height = driver.execute_script('return document.body.scrollHeight')
#     if new_height == prev_heigh:
#         print('breaking')
#         break

# item_number = 1
# all_titles = driver.find_elements(By.XPATH,value='//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div')

# while item_number < len(all_titles):
#     try:
#         title_element = driver.find_element(By.XPATH, value=f'//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[{item_number}]/a/div/picture/img')
#         title = title_element.get_attribute('alt')
#         spanish_title_element = driver.find_element(By.XPATH, value=f'//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[{item_number}]/a')
#         spanish_title = spanish_title_element.get_attribute('href').split('/')[-1].replace('-', ' ')
#         if movies.get(title):
#             movies[title].append('paramount')
#             print('title exist')
#         else:
#             movies[title] = ['paramount']
#             spanish_titles.append(spanish_title)
#             print('title does not exist')
#     except:
#         print('error')
#     item_number += 1

# sleep(5)

# driver.get(HBO_URL)

# sleep(5)

# while True:
#     prev_heigh = driver.execute_script('return document.body.scrollHeight')
#     driver.execute_script(f'window.scrollTo(0, document.body.scrollHeight)')
#     sleep(5)
#     new_height = driver.execute_script('return document.body.scrollHeight')
#     if new_height == prev_heigh:
#         print('breaking')
#         break

# item_number = 1
# all_titles = driver.find_elements(By.XPATH,value='//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div')

# while item_number < len(all_titles):
#     try:
#         title_element = driver.find_element(By.XPATH, value=f'//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[{item_number}]/a/div/picture/img')
#         title = title_element.get_attribute('alt')
#         spanish_title_element = driver.find_element(By.XPATH, value=f'//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[{item_number}]/a')
#         spanish_title = spanish_title_element.get_attribute('href').split('/')[-1].replace('-', ' ')
#         if movies.get(title):
#             movies[title].append('hbo')
#             print('title exist')
#         else:
#             movies[title] = ['hbo']
#             spanish_titles.append(spanish_title)
#             print('title does not exist')
#     except:
#         print('error')
#     item_number += 1

# original_title = []
# streaming_platforms = []
# latin_title = []

# for key in movies:
#     original_title.append(key)
#     streaming_platforms.append(movies[key])

# print('movies length', len(movies))
# print('movies spanish length', len(spanish_movies))

# df = pd.DataFrame({'original_title': original_title, 'streaming_platforms': streaming_platforms})
# df.to_csv('movies_data.csv', index=False)
# print('file created')

# my_nested_dict = {}

# title = 'title1'

# my_nested_dict['title'] = {'streaming': ['netflix'], 'titles': ['title1', 'title2']}
# print(my_nested_dict['title']['titles'])

# if title in my_nested_dict['title']['titles']:
#     print('is in')
# else:
#     print('is not')

# my_nested_dict['title']['streaming'].append('disney')
# print(my_nested_dict)
    
original_title = []
title_two = []
title_three = []
title_four = []
streaming = []

for key in movies:
    original_title.append(movies[key]['original_title'])
    title_two.append(key)
    title_three.append(movies[key]['spanish_title_one'])
    title_four.append(movies[key]['spanish_title_two'])
    streaming.append(movies[key]['streaming'])

with open("sample.json", "w") as file:
    json.dump(movies, file, indent=4)