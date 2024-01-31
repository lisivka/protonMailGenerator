from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

# Создаем объект опций для Firefox
options = Options()

# Устанавливаем режим приватного браузера
options.add_argument("-private")


# Запускаем браузер Firefox с использованием опций
driver = webdriver.Firefox(options=options)
# element = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/form/div[1]/div[1]/div[2]')

# Пример использования
# driver.get("https://www.example.com")

driver.get("https://www.example.com")
print("Первое окно: ", driver.title)

# Открываем новую вкладку (второе окно)
driver.execute_script("window.open('', '_blank');")
# Переключаемся на вторую вкладку
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.google.com")
print("Второе окно: ", driver.title)

# Ждем некоторое время
time.sleep(2)

# Переключаемся обратно на первую вкладку
driver.switch_to.window(driver.window_handles[0])
print("Снова в первом окне: ", driver.title)
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
print("Снова в втором окне: ", driver.title)
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
print("Снова в первом окне: ", driver.title)