#! python3
# Michi4
from PIL import Image
import pyautogui
import sys
import time
import random
import string
import webbrowser
import ctypes
import re
from mimesis import Generic
from mimesis.locales import Locale
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
from selenium import webdriver
import webbrowser
import time
import random
import pyperclip
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.expected_conditions import \
    presence_of_element_located

generic = Generic(locale=Locale.EN)
username = generic.person.username() + str(random.randint(1, 100))
password = generic.person.password(length=10)


def sleep_random(seconds=0):
    wait = (random.randint(1 + seconds, 3 + seconds) + random.random())
    print(f'Wait: {wait}')
    time.sleep(wait)
    return


options = Options()
options.add_argument("-private")
options.add_argument("--window-size=800,600")
#scale
# options.add_argument("--scale=0.5")
driver = webdriver.Firefox(options=options)

def open_dropmail(url):

    host = "droopmailme"
    while host not in ["dropmail.me","spymail.one",
                       "10mail.org","minimail.gq",
                       "yomail.info","emlhub.com",
                       "zeroe.ml",
                       ]:
        print(f"{host=}")
        driver.get(url)
        fake_email = get_email()
        _, host = fake_email.split("@")

    print(f"GET {fake_email=}")
    print("First window: ", driver.title)
    sleep_random()
    return fake_email




def get_email():
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(presence_of_element_located((
            By.XPATH, "/html/body/div[2]/div[3]/div/div/div/span[1]")))

        results = driver.find_elements(
            By.XPATH,
            "/html/body/div[2]/div[3]/div/div/div/span[1]")
        sleep_random()
        my_email = results[0].text
        print(my_email)
    except Exception as e:
        print(f"Ошибка при поиске EMAIL: {e}")
        my_email = "ERROR"
    return my_email


def open_proton():
    driver.execute_script("window.open('', '_blank');")
    # Переключаемся на вторую вкладку
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://account.proton.me/signup?plan=free")
    print("Second window: ", driver.title)
    sleep_random()




def find_xpath(target, data='', driver=driver, name=""):
    try:
        wait = WebDriverWait(driver, 2)
        element = wait.until(presence_of_element_located((
            By.XPATH, target)))
        element.send_keys(data) if element else print(f"{name} not found")
    except Exception as e:
        print(f"Ошибка при поиске элемента {name}: {e}")
        return False


def click_button(xpath, name=""):
    try:
        button_xpath = xpath
        button_element = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, button_xpath))
        )
        if button_element:
            button_element.click()
            print(f"Кнопка {name} нажата")
        else:
            print(f"Кнопка {name} не найдена")
        return button_element
    except Exception as e:
        print(f"Ошибка при поиске кнопки {name}: {e}")


def enter_data_signup():

    # driver.switch_to.window(driver.window_handles[1])
    print("Enter User: ", driver.title)
    sleep_random(3)

    pyautogui.typewrite(username, interval=0.1)
    pyautogui.press('tab', presses=3)
    print("Username:" + username)

    pyautogui.typewrite(password, interval=0.1)
    pyautogui.press('tab', presses=1)
    pyautogui.typewrite(password, interval=0.1)
    pyautogui.press('enter')
    print("Password:" + password)
    sleep_random()

    button_xpath ='/html/body/div[1]/div[4]/div[1]/main/div[1]/div[2]/form/button'
    click_button(button_xpath, name="Create User")

    sleep_random()

    button_xpath = '/html/body/div[1]/div[4]/div/main/div/div[2]/div/div[1]/nav/ul/li[2]'
    click_button(button_xpath, name="Tab EMAIL")

def enter_email(fake_email):
    sleep_random()
    # pyautogui.typewrite(fake_email, interval=0.1)
    # pyautogui.press('tab', presses=1)
    pyautogui.typewrite(fake_email, interval=0.1)
    button_xpath ='/html/body/div[1]/div[4]/div/main/div/div[2]/div/div[2]/button'
    click_button(button_xpath, name="Enter EMAIL")
    '/html/body/div[1]/div[4]/div/main/div/div[2]/div[2]/div[2]/span' #
    sleep_random()

def get_code_confirm():
    driver.switch_to.window(driver.window_handles[0])
    confirm_text = ""
    while confirm_text == "":
        wait = WebDriverWait(driver, 60)
        try:
            wait.until(presence_of_element_located((
                By.XPATH, "/html/body/div[2]/div[9]/div[2]/ul/li/div[3]/div[1]/pre")))

            results = driver.find_elements(
                By.XPATH,
                "/html/body/div[2]/div[9]/div[2]/ul/li/div[3]/div[1]/pre")
            sleep_random()
            confirm_text = results[0].text
            print(f"{confirm_text=}")

        except Exception as e:
            print(f"Ошибка при поиске CODE: {e}")
            confirm_text = ""
    return confirm_text.strip()

def enter_confirm_():
    driver.switch_to.window(driver.window_handles[1])
    sleep_random()
    pyautogui.typewrite(confirm, interval=0.1)
    pyautogui.press('tab', presses=1)
    button_xpath ='/html/body/div[1]/div[4]/div/main/div/div[2]/button[1]'
    click_button(button_xpath, name="Enter CONFIRM")
    sleep_random()

def enter_recover():
    driver.switch_to.window(driver.window_handles[1])
    sleep_random()
    button_xpath ='/html/body/div[1]/div[4]/div/main/div/div[2]/form/button[2]'
    click_button(button_xpath, name="Enter RECOVER")
    sleep_random(15)
    pyautogui.press('enter')
    sleep_random(5)
    pyautogui.press('tab', presses=3)
    pyautogui.press( 'enter')
    pyautogui.press('tab', presses=1)
    sleep_random(5)
    pyautogui.press('enter')

def save_user(fake_email):
    logfile = open("../mailgen/accLog.txt", "a")
    logfile.write(username + "@proton.me\t" + password +"\t" + fake_email + "\n")
    logfile.close()


url_drop = "https://dropmail.me/en/"
fake_email = open_dropmail(url_drop)
open_proton()
enter_data_signup()
enter_email(fake_email)
confirm = get_code_confirm()
print(f"{confirm=}")
confirm= confirm[-6:]

enter_confirm_()
#
save_user(fake_email)

# url_ = r"file:\\\D:\WORK\Freelance\protonMailGenerator\Temporary_email.html"
# driver.get(url_)
# confirm = get_code_confirm()
# print(f"{confirm=}")
# confirm= confirm[-6:]

