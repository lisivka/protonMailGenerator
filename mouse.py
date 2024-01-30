from selenium import webdriver
import pyautogui
import time
from selenium.webdriver.common.by import By


def perform_mouse_actions(driver, target_id):
    time.sleep(5)
    # Ищем элемент по классу
    try:
        # element = driver.find_element(By.ID, target_id)
        # поиск по XPath
        element = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/form/div[1]/div[1]/div[2]')



        # element=driver.find_element(By.CSS_SELECTOR, target_id)
        location = element.location_once_scrolled_into_view
        #click
        element.click()
        pyautogui.typewrite('HELLO')
        pyautogui.press('enter')

    except Exception as e:
        print(f"Ошибка при поиске элемента: {e}")
        return

    if location:
        # Опускаемся ниже элемента на 90 пикселей
        pyautogui.moveTo(location['x'], location['y'] + 50, duration=1)

        # Нажимаем левую кнопку мыши
        pyautogui.mouseDown()

        # Ждем 3 секунды
        time.sleep(3)

        # Тянем элемент мышкой вниз
        pyautogui.moveTo(location['x']+200, location['y'] + 200, duration=1)

        # Ждем еще 3 секунды
        time.sleep(3)

        # Отпускаем мышку
        pyautogui.mouseUp()

        print("Действия с мышью выполнены успешно.")
    else:
        print(f"Элемент с классом {target_class} не найден на странице.")


# Пример использования
url = "https://www.google.com/"  # Замените на ваш URL
# target_class = "challenge-canvas"
# target_id = "searchform"
target_id = "RNNXgb"
# Запустить браузер  Firefox на весь экран

options = webdriver.FirefoxOptions()
options.add_argument("--start-maximized")

driver = webdriver.Firefox(options=options)  # Используйте свой webdriver (например, FirefoxDriver)


driver.get(url)
pyautogui.press('F11')
# Ждем, чтобы страница загрузилась
time.sleep(2)
pyautogui.write('121212')
pyautogui.press('enter')

# Вызываем функцию для выполнения действий с мышью
perform_mouse_actions(driver, target_id)

# Закрываем браузер
# driver.quit()
