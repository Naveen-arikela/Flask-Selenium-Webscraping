from bs4 import BeautifulSoup

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample Page</title>
</head>
<body>
    <div id="myDiv">
        <h1>This is a heading</h1>
    </div>
</body>
</html>
"""


soup = BeautifulSoup(html_content, 'html.parser')

div_element = soup.find('div')
tags_data = [tag for tag in div_element.find_all()]

# print("tags data:: ", tags_data)
tags_dict = {}
for tag in tags_data:
    # print(tag.name)
    tags_data = [tag for tag in soup.find_all()]
    # print("tags data:: ", tags_data)
    for tag in tags_data:
        tag_name = tag.name
        if tag_name not in tags_dict:
            tags_dict[tag_name] = []
        tags_dict[tag_name].append(tag)

print(tags_dict)

# data = {
#     "p": ['<p>This is a paragraph inside the div.</p>', '<p>This is a paragraph inside the div.</p>'],
#     "div": ['<div>This is a paragraph inside the div.</div>', '<div>This is a paragraph inside the div.</div>']
# }

# import requests
# domain_url = 'https://pubmed.ncbi.nlm.nih.gov/32382742/'
# html_content = requests.get(domain_url).text
# soup = BeautifulSoup(html_content, 'lxml')
# print(soup)