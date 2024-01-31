from mimesis import Generic
from mimesis.locales import Locale

# import webbrowser
from selenium import webdriver
import pyautogui
import time
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

generic = Generic(locale=Locale.EN)


def random_sleep(seconds=0):
    time_sleep = random.randint(1 + seconds, 3 + seconds) + random.random()
    time.sleep(time_sleep)
    print("Sleeping for " + str(time_sleep) + " seconds")
    return


driver = webdriver.Firefox()
url = 'https://www.google.com/'
driver.get(url)

# webbrowser.open('https://www.google.com/')
time.sleep(3)
# pyautogui.hotkey('shift', 'ctrl', 'n')
pyautogui.hotkey('shift', 'ctrl', 'P')
time.sleep(3)
pyautogui.write('https://account.proton.me/signup?plan=free')
pyautogui.press('enter')
# pyautogui.press('F11')
time.sleep(3)
random_sleep()

username = generic.person.username()
pyautogui.typewrite(username)
random_sleep()

pyautogui.press('tab', presses=3)
random_sleep()
print("Username: " + username)

password = generic.person.password(length=10)
pyautogui.typewrite(password)
random_sleep()

pyautogui.press('tab', presses=1)
pyautogui.typewrite(password)
random_sleep()
print("Password: " + password)

pyautogui.press('tab', presses=1)
pyautogui.press('enter')
print("Password: " + password)
pyautogui.press('enter')
random_sleep(4)


def perform_mouse_actions(driver, target=''):
    try:
        # Ищем элемент по xpath
        # element = driver.find_element(By.XPATH, '//*[@id="label_1"]')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="label_1"]')))

        location = element.location_once_scrolled_into_view

        element.click()
        pyautogui.typewrite('HELLO')

    except Exception as e:
        print(f"Ошибка при поиске элемента: {e}")
        return


target = r'//*[@id="label_1"]'
perform_mouse_actions(driver, target)
