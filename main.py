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

# this is a new comment

spanish_titles = []
movies = {}
chrome_options = ChromeOptions()
driver = webdriver.Chrome(options=chrome_options.get_options())

JUSTWATCH_URL = 'https://www.justwatch.com/pe'
NETFLIX_URL = 'https://www.justwatch.com/pe/proveedor/netflix'
DISNEY_URL = 'https://www.justwatch.com/pe/proveedor/disney-plus'
PRIME_URL = 'https://www.justwatch.com/pe/proveedor/amazon-prime-video?monetization_types=flatrate'
PARAMOUNT = 'https://www.justwatch.com/pe/proveedor/paramount-plus'
HBO_URL = 'https://www.justwatch.com/pe/proveedor/hbo-max'
STAR_URL = 'https://www.justwatch.com/pe/proveedor/star-plus'

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

    all_titles = driver.find_element(By.XPATH,value='/html/body/div/div[4]/div[3]/div/div[2]/div/div[1]/div')
    links = all_titles.find_elements(By.TAG_NAME, value='a')

    i = 0

    while i < len(links):
        try:
            original_title = normalize_string(links[i].find_element(By.TAG_NAME, value='img').get_attribute('alt'))
            title = normalize_string(links[i].get_attribute('href').split('/')[-1].replace('-', ' ')).lower()
            posters = []
            poster_one = str(links[i].find_element(By.TAG_NAME, value='source').get_attribute('data-srcset')).split(',')[0]
            psoter_two = str(links[i].find_element(By.TAG_NAME, value='source').get_attribute('srcset')).split(',')[0]
            posters.append(poster_one)
            posters.append(psoter_two)

            if movies.get(title):
                movies[title]['streaming'].append(streaming)
            else:
                print(f'Adding {title} and {original_title}')
                movies[title] = {'streaming': [streaming], 'original_title': original_title.lower(), 'spanish_title_one': '#', 'spanish_title_two': '#', 'poster': posters}
        except:
            print('error')
        i += 1

def get_spanish_titles(driver):
    all_titles = driver.find_element(By.XPATH,value='/html/body/div/div[4]/div[3]/div/div[2]/div/div[1]/div')
    imgs = all_titles.find_elements(By.TAG_NAME, value='img')

    i = 0

    while i < len(imgs):
        try:
            spanish_title_one = normalize_string(str(imgs[i].get_attribute('data-src')).split('/')[-1].replace('-', ' ')).lower()
            spanish_title_two = normalize_string(str(imgs[i].get_attribute('alt'))).lower()
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
        i += 1

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

# Netflix

print('Netflix')

set_english_language(driver)

driver.get(NETFLIX_URL)

sleep(5)

get_to_the_end(driver)

get_english_titles(driver, 'Netflix')

set_spanish_language(driver)

get_to_the_end(driver)

get_spanish_titles(driver)

# DISNEY

print('Disney+')

set_english_language(driver)

driver.get(DISNEY_URL)

sleep(5)

get_to_the_end(driver)

get_english_titles(driver, 'Disney+')

set_spanish_language(driver)

get_to_the_end(driver)

get_spanish_titles(driver)

# PRIME

print('Amazon Prime')

set_english_language(driver)

driver.get(PRIME_URL)

sleep(5)

get_to_the_end(driver)

get_english_titles(driver, 'Amazon Prime Video')

set_spanish_language(driver)

get_to_the_end(driver)

get_spanish_titles(driver)

# PARAMOUNT

print('Paramount')

set_english_language(driver)

driver.get(PARAMOUNT)

sleep(5)

get_to_the_end(driver)

get_english_titles(driver, 'Paramount')

set_spanish_language(driver)

get_to_the_end(driver)

get_spanish_titles(driver)

# HBO

print('HBO Max')
    
set_english_language(driver)

driver.get(HBO_URL)

sleep(5)

get_to_the_end(driver)

get_english_titles(driver, 'HBO Max')

set_spanish_language(driver)

get_to_the_end(driver)

get_spanish_titles(driver)

# STAR PLUS

print('Star Plus')
    
set_english_language(driver)

driver.get(STAR_URL)

sleep(5)

get_to_the_end(driver)

get_english_titles(driver, 'Star Plus')

set_spanish_language(driver)

get_to_the_end(driver)

get_spanish_titles(driver)


data = []

for key in movies:

    data.append({
        'original_title': movies[key]['original_title'].title(),
        'title_two': key,
        'title_three': movies[key]['spanish_title_one'],
        'title_four': movies[key]['spanish_title_two'],
        'poster': movies[key]['poster'],
        'streaming': movies[key]['streaming']
    })

with open("movies-star.json", "w") as file:
    json.dump(data, file, indent=4)

