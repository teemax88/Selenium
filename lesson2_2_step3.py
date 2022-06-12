# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time




# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

browser.get(link)


#Считать значение для переменной x.
x_element = browser.find_element_by_id("num1")
x = x_element.text
y_element = browser.find_element_by_id("num2")
y = y_element.text

sum = str(int(x)+int(y))


select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(sum) # ищем элемент sum



# Найдем кнопку, которая отправляет введенное решение
submit_button = browser.find_element_by_css_selector(".btn")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(10)

# После выполнения всех действий мы не должны забыть закрыть окно браузера

time.sleep(10)
browser.quit()
