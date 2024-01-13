from flask import Flask, render_template, request
from main.webscrap import SearchWithContainers, CreateWordDocument
from main.constants import(
    LOGIN_FORM,
    SCRAP_WEBSITE_FORM,
    DISPLAY_TAGS_FORM,
    NO_CONTENT_RESPONSE,
    USERNAME,
    PASSWORD
)

from selenium import webdriver
import webview

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    print(f"home_page:: {request.form}")
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username.strip() == USERNAME and password.strip() == PASSWORD:
            return render_template('index.html', username=username, password=password)
    return render_template('login.html')

#scrap website content
@app.route('/scrap-website', methods=['GET', 'POST'])
def run_webscrap():
    html_tags = {
        'html': [], 'body': [], 'p': [{'h1': 'Title 1'}, {'p': 'Paragraph 1'}, {'h2': 'Title 2'}, {'p': 'Paragraph 2'}, {'h3': 'Title 3'}, {'h2': 'Why ChooseUs?'}, {'p': 'Paragraph 3'}, {'p': 'data'}, {'p': 'data'}], 'h2': [], 'h3': [], 'img': [{'img': 'image link'}], 'span': [], 'div': []
    }
    if request.method == 'POST':
        form_type = request.form.get('form_type')

        if form_type == LOGIN_FORM:
            print(f"run_webscrap:: {request.form}")
            username = request.form.get('username')
            password = request.form.get('password')
            if username.strip() == USERNAME and password.strip() == PASSWORD:
                return render_template('index.html', username=username, password=password)
            else:
                return render_template('login.html')

        elif form_type == SCRAP_WEBSITE_FORM:
            website_url = request.form.get('website_url')
            div_class = request.form.get('div_class')
        
            if website_url or (website_url and div_class):
                scrap_object = SearchWithContainers(website_url, div_class)
                html_tags = scrap_object.run_search_tags()
                # print(f"html_tags:: {html_tags}")
                return render_template('index.html', html_tags=html_tags)
            
        elif form_type == DISPLAY_TAGS_FORM:
            selected_tags = request.form.getlist('selected_tags')
            print(f"selected_tags: {selected_tags}")
            document_object = CreateWordDocument(selected_tags)
            document_object.run_create_word_document()

            return NO_CONTENT_RESPONSE 
            
    return render_template('index.html', html_tags=None)

@app.route('/process_tags', methods=['GET', 'POST'])
def process_tags():
    html_tags = {
        'html': [], 'body': [], 'p': [{'h1': 'Title 1'}, {'p': 'Paragraph 1'}, {'h2': 'Title 2'}, {'p': 'Paragraph 2'}, {'h3': 'Title 3'}, {'h2': 'Why ChooseUs?'}, {'p': 'Paragraph 3'}, {'p': 'data'}, {'p': 'data'}], 'h2': [], 'h3': [], 'img': [{'img': 'image link'}], 'span': [], 'div': []
    }
    return render_template('index.html', html_tags=html_tags)

# webview.create_window('Centrix Webscrapper App', app)
if __name__ == '__main__':
    app.run(debug=True)

 


