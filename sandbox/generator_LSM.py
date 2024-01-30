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

generic = Generic(locale=Locale.EN)
username = generic.person.username() + str(random.randint(1, 100))
password = generic.person.password(length=10)


def get_anonym_browser():
    driver = webdriver.Firefox()
    driver.get('https://www.google.com')
    # driver.get("https://example.com/")
    # driver.maximize_window()
    # driver.set_window_size(800  , 600)
    time.sleep(4)
    pyautogui.hotkey('ctrl', 'shift', 'p', interval=0.1)
    time.sleep(2)
    return driver


def open_proton_signup():
    pyautogui.typewrite('https://account.proton.me/signup?plan=free\n',
                        interval=0.05)
    time.sleep(5)


def enter_data_signup():
    # Username
    # _username_=username
    pyautogui.typewrite(username, interval=0.1)
    pyautogui.press('tab', presses=3)
    print("Username:" + username)

    # Password
    _password_ = password
    pyautogui.typewrite(password, interval=0.1)
    pyautogui.press('tab', presses=1)
    pyautogui.typewrite(password, interval=0.1)
    pyautogui.press('enter')
    print("Password:" + password)
    time.sleep(5)


def change_to_tab():
    # pyautogui.typewrite('\t\t\t\n')
    pyautogui.press('tab', presses=3)
    pyautogui.press('enter')
    time.sleep(3)
    # pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('t'); pyautogui.keyUp('ctrlleft')


def open_dropmail_page():
    time.sleep(1)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(3)
    pyautogui.typewrite('https://dropmail.me/en/\n', interval=0.05)
    time.sleep(3)
    # pyautogui.press('tab', presses=15, interval=0.2)
    # pyautogui.press('left', presses=1, interval=0.1)
    # pyautogui.press('tab', presses=13, interval=0.2)
    # pyautogui.press('tab', presses=13, interval=0.1)
    # pyautogui.click('@')


def get_mail_data():
    pyautogui.hotkey('ctrl', 'f', interval=0.2)
    pyautogui.typewrite('@', interval=0.2)
    pyautogui.hotkey('Esc', interval=0.2)
    start_x, start_y = pyautogui.position()
    time.sleep(1)
    # Нажмем левую кнопку мыши в текущем месте
    pyautogui.click(start_x, start_y)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c', interval=0.2)
    time.sleep(1)
    # Получаем значение из буфера обмена
    clipboard_content = pyperclip.paste()
    # Выводим полученное значение
    print("Содержимое буфера обмена:", clipboard_content)

    # pyautogui.hotkey('ctrl', 't', interval=0.2)
    # time.sleep(3)
    # pyautogui.hotkey('ctrl', 'v', interval=0.2)


def get_mail_data2():
    time.sleep(5)

    # Находим элемент с классом "address"
    # email_element = driver.find_element(By.CLASS_NAME, 'address')
    element = driver.find_element(By.CSS_SELECTOR,
                                  'div.text-center:nth-child(2)')
    # Получаем текст из элемента
    email_address = element.text

    # Выводим значение
    print("Электронная почта:", email_address)


def pasta_mail():
    pyautogui.hotkey('ctrl', 'pageup', interval=0.2)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v', interval=0.2)


def save_user():
    logfile = open("../mailgen/accLog.txt", "a")
    logfile.write(username + "@proton.me    " + password + "\n")
    logfile.close()


driver = get_anonym_browser()
# open_proton_signup()
# enter_data_signup()
# change_to_tab()
open_dropmail_page()

# get_mail_data()
get_mail_data2()
# pasta_mail()


save_user()
