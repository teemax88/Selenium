from selenium import webdriver
import os
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath("//input[@name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//input[@name='email']")
    input3.send_keys("Smolensk@example.ru")

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'selenium.docx')

    # найдем кнопку для загрузки файла
    download_button = browser.find_element_by_id("file")

    # передадим ей путь к файлу
    download_button.send_keys(file_path)


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()