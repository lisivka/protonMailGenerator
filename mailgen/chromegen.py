from PIL import Image
import pyautogui
import time
import random
import string
import webbrowser
import ctypes
import re

CF_TEXT = 1

kernel32 = ctypes.windll.kernel32
kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
kernel32.GlobalLock.restype = ctypes.c_void_p
kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
user32 = ctypes.windll.user32
user32.GetClipboardData.restype = ctypes.c_void_p

def get_clipboard_data():
    user32.OpenClipboard(0)
    try:
        if user32.IsClipboardFormatAvailable(CF_TEXT):
            data = user32.GetClipboardData(CF_TEXT)
            if data:
                data_locked = kernel32.GlobalLock(data)
                text = ctypes.c_char_p(data_locked)
                value = text.value
                kernel32.GlobalUnlock(data_locked)
                return str(re.findall(r'(\d{6})', str(value)))
    finally:
        user32.CloseClipboard()

def get_temp_mail():
    user32.OpenClipboard(0)
    try:
        if user32.IsClipboardFormatAvailable(CF_TEXT):
            data = user32.GetClipboardData(CF_TEXT)
            if data:
                data_locked = kernel32.GlobalLock(data)
                text = ctypes.c_char_p(data_locked)
                value = text.value
                kernel32.GlobalUnlock(data_locked)
                if any(domain in str(value) for domain in ["@dropmail.me", "@emltmp.com", "@spymail.one", "@10mail.org"]):
                    match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', str(value))
                    return str(match.group(0))
    finally:
        user32.CloseClipboard()

def randomize(option, length):
    if length > 0:
        if option == '-p':
            characters = string.ascii_letters + string.digits + '!@#$%^&*()_+'
        elif option == '-s':
            characters = string.ascii_letters + string.digits
        elif option == '-l':
            characters = string.ascii_letters
        elif option == '-n':
            characters = string.digits
        elif option == '-m':
            characters = 'JFMASOND'

        if option == '-d':
            generated_info = random.randint(1, 28)
        elif option == '-y':
            generated_info = random.randint(1950, 2000)
        else:
            generated_info = ''.join(random.choice(characters) for _ in range(length))

        return generated_info
    else:
        return 'error'

def open_proton_signup():
    webbrowser.open('https://account.proton.me/signup?plan=free')
    time.sleep(5)

from mimesis import Generic
from mimesis.locales import Locale
generic = Generic(locale=Locale.EN)

username = generic.person.username()
password = generic.person.password(length=10)
def create_account():
    open_proton_signup()
    # Username
    # username = randomize('-s', 5) + randomize('-s', 5) + randomize('-s', 5)
    username = generic.person.username()
    pyautogui.typewrite(username)
    pyautogui.press('tab', presses=3)
    print("Username: " + username)

    # Password

    # password = randomize('-p', 16)
    password = generic.person.password(length=10)
    pyautogui.typewrite(password + '\t' + password + '\t')
    print("Password: " + password)

    # pyautogui.typewrite('\n')
    # time.sleep(5)
    # pyautogui.typewrite('\t\t\t\n')
    #
    # pyautogui.hotkey('ctrlleft', 't')
    # time.sleep(10)
    # pyautogui.typewrite('https://dropmail.me/\n')
    #
    # pyautogui.hotkey('shiftleft', 'down')
    # time.sleep(10)
    #
    # new_mail = True
    # while True:
    #     if not new_mail:
    #         pyautogui.hotkey('ctrlleft', 'r')
    #         time.sleep(5)
    #     pyautogui.typewrite('\t' * 24)
    #     pyautogui.hotkey('ctrlleft', 'shiftleft', 'shiftright', 'down')
    #     pyautogui.hotkey('ctrlleft', 'c')
    #     new_mail = get_temp_mail()
    #     if new_mail:
    #         print("10 min mail: " + new_mail)
    #         break
    #
    # pyautogui.hotkey('ctrlleft', '\t')
    # time.sleep(1)
    # pyautogui.hotkey('ctrlleft', 'v')
    # pyautogui.press('backspace')
    # pyautogui.typewrite('\n')
    #
    # time.sleep(10)
    #
    # pyautogui.hotkey('ctrlleft', '\t')
    # time.sleep(1)
    #
    # pyautogui.hotkey('ctrlleft', 'a')
    # pyautogui.hotkey('ctrlleft', 'c')
    #
    # pyautogui.hotkey('ctrlleft', '\t')
    # time.sleep(5)
    # pyautogui.typewrite(str(get_clipboard_data()) + '\n')
    #
    # time.sleep(5)
    # pyautogui.typewrite('\n')
    # time.sleep(5)
    # pyautogui.typewrite('\t\t\t\n')
    # time.sleep(1)
    # pyautogui.typewrite('\t\n')
    #
    # print(username + "@proton.me:" + password)
    #
    logfile = open("accLog.txt", "a")
    logfile.write(username + "@proton.me:" + password + "\n")
    logfile.close()

if __name__ == "__main__":
    print("Starting...")
    create_account()

