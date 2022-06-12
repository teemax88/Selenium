# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
import time
import math

# Функция calc(), которая рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

browser.get(link)


#Считать значение для переменной x.
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)


# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему.
# Напишем текст ответа в найденное поле
input = browser.find_element_by_id("answer")
input.send_keys(y)
print(y)
time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()
radio = browser.find_element_by_id("robotsRule")
radio.click()
submit_button = browser.find_element_by_css_selector(".btn")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(10)

# После выполнения всех действий мы не должны забыть закрыть окно браузера

time.sleep(10)
browser.quit()
