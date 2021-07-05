# -*- coding: utf-8 -*-

# Developed by Endika Gil
# Github:   https://github.com/endikagil/OsaVaccineTurn
#
# Due to covid19 and the global pandemic, vaccination shifts have been established among the population. 
# This script checks on 'Osakidetza' health page if they have included us within the current vaccination shift.
# In that case, it notifies you thought Telegram.
# It checks every 2 minutes, but you can adapt as you wish. 
# 
# Use .env file to specify sensitive information: 
# TIS_NUMBER, SURNAME, BIRTHDATE, CHROME_DRIVER_PATH, TELEGRAM_API_TOKEN, TELEGRAM_CHAT_ID

from selenium import webdriver  # Used for openning and using Chrome
from selenium.webdriver.common.keys import Keys # Used for sending keyboard keys on Chrome
from selenium.webdriver.common.action_chains import ActionChains # Used for sending keyboard keys on Chrome
import requests     # Used for sending message using Telegram
import json         # Used to work with Telegram json response
import time         # Used for sleep function
import os           # Used for getting env variables
from dotenv import load_dotenv # Used for reading .env files and hidde sensitive information
load_dotenv()

# Reading constants from .env file
CHROME_DRIVER_PATH=os.getenv('CHROME_DRIVER_PATH')
TELEGRAM_API_TOKEN=os.getenv('TELEGRAM_API_TOKEN')
TELEGRAM_CHAT_ID=os.getenv('TELEGRAM_CHAT_ID')
TIS_NUMBER=os.getenv('TIS_NUMBER')
SURNAME=os.getenv('SURNAME')
BIRTHDATE=os.getenv('BIRTHDATE')

while True:
    # Creating Chrome session
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    driver.implicitly_wait(120) # We are going to check every 2 minutes
    driver.maximize_window()

    # Accessing to website
    driver.get("https://zitaberria.osakidetza.eus/o22PlamWar/iniciologin.do?idioma=cas")

    # Locate search terms text boxes
    tis_number = driver.find_element_by_id("codnumerico")
    tis_number.clear()
    surname = driver.find_element_by_id("apellido")
    surname.clear()
    birthdate = driver.find_element_by_id("idfecha")
    birthdate.clear()

    # Write search terms
    tis_number.send_keys(TIS_NUMBER)
    surname.send_keys(SURNAME)
    birthdate.send_keys(BIRTHDATE)

    # Clic on "Confirm" button
    confirm = driver.find_element_by_id("btnSubmitTis")
    confirm.submit()

    # Ask for new appointment, 5 tab keystroke and enter
    time.sleep(2)
    n = 5
    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB * n)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    # Check if vaccine option is able
    if driver.find_elements_by_xpath("//*[contains(text(), 'Vacuna Covid19 (1ªDosis)')]"):
        # Found, let's go with the notice
        r = requests.post('https://api.telegram.org/bot'+TELEGRAM_API_TOKEN+'/sendMessage',
                data={'chat_id': TELEGRAM_CHAT_ID, 'text': 'Se han abierto las citas para la vacuna!'})
        data = json.loads(r.text)

        # Checking if message was sent correctly
        if data['ok']:
            break

    driver.close()
    time.sleep(1)

