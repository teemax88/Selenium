from selenium import webdriver
import time
import math

# Функция calc(), которая рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(2)

    # Считать значение для переменной x.
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему.
    # Напишем текст ответа в найденное поле
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    print(y)
    #time.sleep(5)

    submit_button = browser.find_element_by_css_selector(".btn")
    # Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
    submit_button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()