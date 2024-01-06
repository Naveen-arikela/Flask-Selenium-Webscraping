from flask import Flask, render_template, request, jsonify
from main.webscrap import SearchWithContainers
from main.constants import(
    SCRAP_WEBSITE_FORM,
    DISPLAY_TAGS_FORM,
    NO_CONTENT_RESPONSE,
    USERNAME,
    PASSWORD
)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
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

        if form_type == SCRAP_WEBSITE_FORM:
            website_url = request.form.get('website_url')
            container_tags = request.form.get('container_tags')

            if website_url and container_tags:
                scrap_object = SearchWithContainers(website_url, container_tags)
                html_tags = scrap_object.run_search_tags()
                # print(html_tags)
                return render_template('index.html', html_tags=html_tags)
            
        elif form_type == DISPLAY_TAGS_FORM:
            print(request.form)
            return NO_CONTENT_RESPONSE 
            
    return render_template('index.html', html_tags=html_tags)

@app.route('/process_tags', methods=['GET', 'POST'])
def process_tags():
    html_tags = {
        'html': [], 'body': [], 'p': [{'h1': 'Title 1'}, {'p': 'Paragraph 1'}, {'h2': 'Title 2'}, {'p': 'Paragraph 2'}, {'h3': 'Title 3'}, {'h2': 'Why ChooseUs?'}, {'p': 'Paragraph 3'}, {'p': 'data'}, {'p': 'data'}], 'h2': [], 'h3': [], 'img': [{'img': 'image link'}], 'span': [], 'div': []
    }
    print(request.form)
    return render_template('index.html', html_tags=html_tags)

if __name__ == '__main__':
    app.run(debug=True)
 
