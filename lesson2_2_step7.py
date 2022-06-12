from selenium import webdriver
import os

browser = webdriver.Chrome()




# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir)
# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, 'selenium.docx')
print(file_path)

time.sleep(10)
browser.quit()