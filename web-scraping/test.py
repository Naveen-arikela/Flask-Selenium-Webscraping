import os
import requests
from bs4 import BeautifulSoup


INPUT_FILES_DIRECTORY = 'input_files'
PARAGRAPH_TAGS = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']

class YourScraper:
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')
        self.data_dict = {}

    def extract_data(self):
        tags_dict = {}
        tags_data = self.soup.find_all()
        paragraph_flag = True

        for tag in tags_data:
            tag_name = tag.name
            tag_text = tag.get_text(strip=True)

            if tag_name not in tags_dict:
                if tag_name in PARAGRAPH_TAGS and paragraph_flag:
                    tags_dict['p'] = []
                    paragraph_flag = False
                else:
                    tags_dict[tag_name] = []
                    
            if tag_name == 'img':
                tag_text = tag.get('src', '')
                tags_dict[tag_name].append({tag_name: tag_text})

            elif tag_name in PARAGRAPH_TAGS:
                tags_dict['p'].append({tag_name: tag_text})
        
        return tags_dict

    def get_data_list(self):
        return self.extract_data()

# Example usage
html_content = """
<html>
  <body>
    <h1>Title 1</h1>
    <p>Paragraph 1</p>
    <h2>Title 2</h2>
    <p>Paragraph 2</p>
    <h3>Title 3</h3>
    <img src="image link">
    <h2 class="makes-head text-center mrgt-15">Why Choose<span class="makes-text-color-red"> Us?</span></h2>
    <p>Paragraph 3</p>
    <div>
    <p>data</p>
    </div>
    <div>
    <p>data</p>
    </div>
  </body>
</html>
"""



# url = "http://makes.org.in/"
# response = requests.get(url)
# html_content = response.text

# # print(html_content)
# input_file_path = os.path.join(INPUT_FILES_DIRECTORY, 'naveen_test.html')
# with open(input_file_path, 'w', encoding='utf-8') as file:
#     file.write(str(html_content))

scraper = YourScraper(html_content)
print(scraper.extract_data())
# data_list = scraper.get_data_list()

# input_file_path = os.path.join(INPUT_FILES_DIRECTORY, 'naveen_test.txt')
# with open(input_file_path, 'w', encoding='utf-8') as file:
#     file.write(str(data_list))
