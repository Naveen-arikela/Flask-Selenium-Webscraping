import os

#Form Types
SCRAP_WEBSITE_FORM = "scrap-website-form"
DISPLAY_TAGS_FORM = "show-tags-form"

#App Constants
NO_CONTENT_RESPONSE = ('', 204)
SPLIT_LINES = '\n'
FILE_EXTENSION = '.docx'

#Tags
SPECIAL_CONTAINER_TAGS = ['body']
PARAGRAPH_TAGS = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']
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


