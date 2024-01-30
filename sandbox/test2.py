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

generic = Generic(locale=Locale.EN)
username = generic.person.username()+str(random.randint(1, 100))
password = generic.person.password(length=10)
userdate = generic.datetime.date()

def sleep_random(seconds):
    wait = (random.randint(1+seconds, 3+seconds)+random.random())
    print(f'Wait: {wait}')
    time.sleep(wait)
    return

driver = webdriver.Firefox()
driver.get('https://www.google.com')
time.sleep(2)
pyautogui.hotkey('Ctrl', 'Shift', 'P')

time.sleep(2)


pyautogui.write('https://account.proton.me/signup?plan=free')
pyautogui.press('enter')
pyautogui.hotkey('F11')
sleep_random(3)
pyautogui.write(username, interval=0.1)
pyautogui.press('tab', presses=3)
pyautogui.write(password, interval=0.1)
pyautogui.press('tab', presses=1)
pyautogui.write(password, interval=0.1)
pyautogui.press('tab', presses=1)
pyautogui.press('enter')
sleep_random(3)

# def perform_mouse_actions(driver, target=''):
#
#     try:
#         # Ищем элемент по xpath
#         # element = driver.find_element(By.XPATH, '//*[@id="label_1"]')
#         sleep_random(2)
#         element = driver.find_element(By.XPATH, target)
#         print(f"Найден элемент: {element}")
#         location = element.location_once_scrolled_into_view
#
#         element.click()
#         # pyautogui.typewrite('HELLO')
#
#     except Exception as e:
#         print(f"Ошибка при поиске элемента: {e}")
#         return
# #
# #
# #
# # x_email_1= ('/html/body/div[1]/div[4]/div/main/div/div[2]/div/div[1]/nav/ul/li[2]/button/span')
# x_email_2 = '//*[@id="label_1"]'
# perform_mouse_actions(driver, x_email_2)
#label_1 > span:nth-child(1)
# pyautogui.hotkey("Alt", 'Tab')
#label_1

# .input
# .input

# кликунть правой кнопкой мыши в цетре экрана
# pyautogui.click(500, 500, button='right')

pyautogui.screenshot('screenshot2.png')
# https://habr.com/ru/articles/525380/
# https://robx.org/wiki/prog/opencv-biblioteka/filtraciya-v-opencv/
# https://account-api.proton.me/captcha/v1/assets/?purpose=signup