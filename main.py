# Getting Netflix content

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from chrome_options import ChromeOptions
from time import sleep
import json
import re
from unicodedata import normalize
import base64
import io
from PIL import Image

spanish_titles = []
movies = {}
chrome_options = ChromeOptions()
driver = webdriver.Chrome(options=chrome_options.get_options())

JUSTWATCH_URL = 'https://www.justwatch.com/pe'
NETFLIX_URL = 'https://www.justwatch.com/pe/proveedor/netflix?monetization_types=flatrate&sort_by=title'
DISNEY_URL = 'https://www.justwatch.com/pe/proveedor/disney-plus?monetization_types=flatrate&sort_by=title'
PRIME_URL = 'https://www.justwatch.com/pe/proveedor/amazon-prime-video?monetization_types=flatrate&sort_by=title'
PARAMOUNT = 'https://www.justwatch.com/pe/proveedor/paramount-plus?monetization_types=flatrate&sort_by=title'
HBO_URL = 'https://www.justwatch.com/pe/proveedor/hbo-max?monetization_types=flatrate&sort_by=title'

urls = [NETFLIX_URL, DISNEY_URL, PRIME_URL, PARAMOUNT, HBO_URL]

driver.get(JUSTWATCH_URL)
driver.maximize_window()

def normalize_string(s):
    s = re.sub(
            r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
            normalize( "NFD", s), 0, re.I
        )
    s = normalize( 'NFC', s)
    return s

def get_english_titles(driver, streaming):

    all_titles = driver.find_elements(By.XPATH,value='//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div')
    item_number = 1

    while item_number <= len(all_titles):
        try:
            original_title_element = driver.find_element(By.XPATH, value=f'//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[{item_number}]/a/div/picture/img')
            original_title = normalize_string(original_title_element.get_attribute('alt'))
            poster = driver.find_element(By.XPATH, value=f'//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[{item_number}]/a/div/picture/source[2]').get_attribute('srcset')
            title_element= driver.find_element(By.XPATH, value=f'//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[{item_number}]/a')
            title = normalize_string(title_element.get_attribute('href').split('/')[-1].replace('-', ' '))
            if movies.get(title):
                movies[title]['streaming'].append(streaming)
            else:
                print(f'Adding {title} and {original_title}')
                movies[title] = {'streaming': [streaming], 'original_title': original_title, 'spanish_title_one': '#', 'spanish_title_two': '#', 'poster': poster}
        except:
            print('error')
        item_number += 1

def get_spanish_titles(driver):
    item_number = 1
    all_titles = driver.find_elements(By.XPATH,value='//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div')

    while item_number < len(all_titles):
        
        try:
            title_element = driver.find_element(By.XPATH, value=f'//*[@id="base"]/div[3]/div/div[2]/div/div[1]/div/div[{item_number}]/a/div/picture/img')
            spanish_title_one = normalize_string(title_element.get_attribute('data-src').split('/')[-1].replace('-', ' '))
            spanish_title_two = normalize_string(title_element.get_attribute('alt'))
            if movies.get(spanish_title_one):
                print('adding', spanish_title_one)
                movies[spanish_title_one]['spanish_title_one'] = spanish_title_one
                movies[spanish_title_one]['spanish_title_two'] = spanish_title_two
            elif movies.get(spanish_title_two):
                print('adding', spanish_title_two)
                movies[spanish_title_two]['spanish_title_one'] = spanish_title_one
                movies[spanish_title_two]['spanish_title_two'] = spanish_title_two
        except:
            print('error')
        item_number += 1

def set_english_language(driver):
    login = driver.find_element(By.XPATH, value='//*[@id="app"]/div[3]/div/div[2]/div[2]/div[1]/div/button/div/span')
    login.click()

    sleep(10)

    langauge_button = driver.find_element(By.XPATH, value='/html/body/ion-modal/div[2]/div/ion-content/div/div/div[2]/button[2]')
    langauge_button.click()

    sleep(10)

    english_us_button = driver.find_element(By.XPATH, value='/html/body/ion-modal/div[2]/div/ion-content/div/div/div/div[12]')
    driver.execute_script("arguments[0].click();", english_us_button)

    sleep(10)

    close_button = driver.find_element(By.XPATH, value='/html/body/ion-modal/div[2]/div/ion-header/ion-toolbar/ion-buttons[2]/ion-button')
    close_button.click()

    sleep(10)

def set_spanish_language(driver):
    login = driver.find_element(By.XPATH, value='//*[@id="app"]/div[3]/div/div[2]/div[2]/div[1]/div/button/div/span')
    login.click()

    sleep(10)

    langauge_button = driver.find_element(By.XPATH, value='/html/body/ion-modal/div[2]/div/ion-content/div/div/div[2]/button[2]')
    langauge_button.click()

    sleep(10)

    spanish_latin_button = driver.find_element(By.XPATH, value='/html/body/ion-modal/div[2]/div/ion-content/div/div/div/div[15]')
    driver.execute_script("arguments[0].click();", spanish_latin_button)

    sleep(10)

    close_button = driver.find_element(By.XPATH, value='/html/body/ion-modal/div[2]/div/ion-header/ion-toolbar/ion-buttons[2]/ion-button')
    close_button.click()
        
    sleep(10)


def get_to_the_end(driver):
    while True:
        prev_heigh = driver.execute_script('return document.body.scrollHeight')
        driver.execute_script(f'window.scrollTo(0, document.body.scrollHeight)')
        sleep(5)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == prev_heigh:
            print('breaking')
            break

print('Netflix')

set_english_language(driver)

driver.get(NETFLIX_URL)

sleep(5)

# get_to_the_end(driver)

get_english_titles(driver, 'Netflix')

# set_spanish_language(driver)

# get_to_the_end(driver)

# get_spanish_titles(driver)

# DISNEY

# print('Disney+')

# set_english_language(driver)

# driver.get(DISNEY_URL)

# sleep(5)

# get_to_the_end(driver)

# get_english_titles(driver, 'Disney+')

# set_spanish_language(driver)

# get_to_the_end(driver)

# get_spanish_titles(driver)

# PRIME

# print('Amazon Prime')

# set_english_language(driver)

# driver.get(PRIME_URL)

# sleep(5)

# get_to_the_end(driver)

# get_english_titles(driver, 'Amazon Prime Video')

# set_spanish_language(driver)

# get_to_the_end(driver)

# get_spanish_titles(driver)

# PARAMOUNT

# print('Paramount')

# set_english_language(driver)

# driver.get(PARAMOUNT)

# sleep(5)

# get_to_the_end(driver)

# get_english_titles(driver, 'Paramount')

# set_spanish_language(driver)

# get_to_the_end(driver)

# get_spanish_titles(driver)

# HBO

# print('HBO Max')

# set_english_language(driver)

# driver.get(HBO_URL)

# sleep(5)

# get_to_the_end(driver)

# get_english_titles(driver, 'HBO Max')

# set_spanish_language(driver)

# get_to_the_end(driver)

# get_spanish_titles(driver)

# while True:
#     prev_heigh = driver.execute_script('return document.body.scrollHeight')
#     driver.execute_script(f'window.scrollTo(0, document.body.scrollHeight)')
#     sleep(5)
#     new_height = driver.execute_script('return document.body.scrollHeight')
#     if new_height == prev_heigh:
#         print('breaking')
#         break



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
    
# original_title = []
# title_two = []
# title_three = []
# title_four = []
# streaming = []

data = []

for key in movies:

    data.append({
        'original_title': movies[key]['original_title'],
        'title_two': key,
        'title_three': movies[key]['spanish_title_one'],
        'title_four': movies[key]['spanish_title_two'],
        'poster': movies[key]['poster'],
        'streaming': movies[key]['streaming']
    })

with open("movies.json", "w") as file:
    json.dump(data, file, indent=4)

