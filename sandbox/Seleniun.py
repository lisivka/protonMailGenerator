import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.firefox.options import Options

#
# with webdriver.Firefox() as driver:
#
#     driver.get("https://google.com/ncr")
#     wait = WebDriverWait(driver, 10)
#     driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
#     wait.until(presence_of_element_located((By.XPATH, '//*[@id="rcnt"]')))
#     results = driver.find_elements(By.XPATH, "//a[@href]")
#
#     for i, elem in enumerate(results):
#         print(f'#{i} {elem.text} ({elem.get_attribute("href")})')

options = Options()

# Устанавливаем режим приватного браузера
options.add_argument("-private")


driver = webdriver.Firefox(options=options)
time.sleep(2)
driver.get('https://dropmail.me/en/')
wait = WebDriverWait(driver, 10)
wait.until(presence_of_element_located((
    By.XPATH,"/html/body/div[2]/div[3]/div/div/div/span[1]")))

results = driver.find_elements(By.XPATH, "/html/body/div[2]/div[3]/div/div/div/span[1]")
my_email = results[0].text
print(results)
print(my_email)
