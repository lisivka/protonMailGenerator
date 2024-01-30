from mimesis import Generic
from mimesis.locales import Locale
generic = Generic(locale=Locale.EN)

username = generic.person.username()
password = generic.person.password(length=10)
# Output: 'sherley3354'

userdate = generic.datetime.date()

print(f'{username=}')
print(f'{userdate=}')
print(f'{password=}')
username = generic.person.username()
print(f'{username=}')
print(f'{userdate=}')


import webbrowser
import pyautogui
import time


# webbrowser.open('https://www.google.com/')
# webbrowser.get('firefox %s').open('http://google.com')
# time.sleep(2)
# pyautogui.hotkey('shift', 'ctrl', 'n')
# time.sleep(2)
# pyautogui.write('https://account.proton.me/signup?plan=free')
# pyautogui.press('enter')

def get_default_browser():
    # Получаем путь к браузеру по умолчанию
    browser_path = webbrowser.get()
    return browser_path

# Выводим путь к браузеру по умолчанию
default_browser = get_default_browser()
print(f"Default browser: {default_browser}")