from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
import os
import time


def initialize():
    os.environ['MOZ_HEADLESS'] = '1'
    binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
    driver = webdriver.Firefox(firefox_binary=binary)
    driver.get('https://www.twitter.com')
    return driver


def go_to_login_page(driver):
    sign_in_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span/span'))
    )
    sign_in_link.click()
    time.sleep(0.3)
    login_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a/div/span/span'))
    )
    login_link.click()


def go_to_login_page_alternative(driver):
    login_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]'))
    )
    login_link.click()


def insert_email(driver, email):
    entry_bar = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'))
    )
    entry_bar.click()
    entry_bar.send_keys(email)
    time.sleep(0.7)
    submit_button = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span')
    submit_button.click()


def insert_password(driver, psswd):
    entry_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input'))
    )
    entry_field.click()
    entry_field.send_keys(psswd)
    time.sleep(0.3)

    login_button = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div')
    login_button.click()


def find_person(driver, user):
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input'))
    )
    search.click()
    search.clear()
    search.send_keys(f'@{user}')
    search.send_keys(Keys.ENTER)
    time.sleep(0.4)
    
    people_btn = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div/div[2]/div/div[3]/a/div')
    people_btn.click()
    time.sleep(0.5)

    person = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[1]'))
    )
    person.click()


def follow_person(driver):
    time.sleep(3)
    follow_btn = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/div')
    follow_btn.click()


def quit(driver):
    driver.quit()




# ----- Experimental -----

def click_tweet(driver):
    time.sleep(2)

    tweet = driver.find_element_by_xpath('//*[@id="id__xou9m7ulsud"]/div[1]/div/div/div[1]/svg')
    tweet.click()

def reply_to_tweet(driver, message):
    click_tweet()
    input_field = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
    input_field.send_keys(message)
