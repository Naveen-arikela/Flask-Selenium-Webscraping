from selenium import webdriver
import time
from flask import Flask, render_template, request
import os

app = Flask(__name__)
root_dir = os.path.dirname(os.path.abspath(__file__))
filename = f'saved_page_203.html'
file_path = os.path.join(root_dir, filename)

url = 'https://www.thelancet.com/journals/laneur/article/PIIS1474-4422(22)00428-8/fulltext'

INPUT_FILES_DIRECTORY = 'input_files'
os.makedirs(INPUT_FILES_DIRECTORY, exist_ok=True)

output_files_path = os.path.join(INPUT_FILES_DIRECTORY, 'test1258')

for index in range(1):
    driver = webdriver.Chrome()
    driver.get(url)

    #website html content
    html_content = driver.page_source
    filename = f'saved_page_{index}.html'
    input_file_path = os.path.join(INPUT_FILES_DIRECTORY, filename)
    with open(input_file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

    # Close the browser window
    time.sleep(10)
    driver.quit()



