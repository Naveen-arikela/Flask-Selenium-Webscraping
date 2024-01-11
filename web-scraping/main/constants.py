import os

#Form Types
SCRAP_WEBSITE_FORM = "scrap-website-form"
DISPLAY_TAGS_FORM = "display-tags-form"
LOGIN_FORM = "login-form"

#App Constants
NO_CONTENT_RESPONSE = ('', 204)
SPLIT_LINES = '\n'
FILE_EXTENSION = '.docx'

#Tags
SPECIAL_CONTAINER_TAGS = ['body']
PARAGRAPH_TAGS = ['div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']
HEADER_TAGS = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
TAGS_STRUCTURE = {
        'p': [{'h1': 'Title 1'}, {'p': 'Paragraph 1'}, {'h2': 'Title 2'}, {'h3': 'Title 3'}],
        'img': [{'img': 'image link'}]
}

#Store images & meta in Local diretory
STATIC_FILES_OUTPUT_DIRECTORY = 'static\images'
OUTPUT_FILES_DIRECTORY = 'output_files'

os.makedirs(STATIC_FILES_OUTPUT_DIRECTORY, exist_ok=True)
os.makedirs(OUTPUT_FILES_DIRECTORY, exist_ok=True)

#Users
USERNAME = 'admin'
PASSWORD = 'admin@123'


HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Get Text from Div</title>
</head>
<body>

<div id="myDiv">
content 
of div
<p>this is the para2</p>
data
</div>
<h1></h1>
</body>
</html>


"""