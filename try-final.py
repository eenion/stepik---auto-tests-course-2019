from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
==================================================
import time
from selenium import webdriver


try:
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")  # <- Путь до файла хромдрайвера
    browser.get(link)


except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    
finally:
    driver.close()
    time.sleep(2)
    driver.quit()