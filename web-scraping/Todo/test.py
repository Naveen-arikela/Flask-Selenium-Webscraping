from bs4 import BeautifulSoup

def scrape_html_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    div_content = soup.find_all()
    print(div_content.contents)
    print(type(div_content))
    p_content = soup.find('p').text.strip() if soup.find('p') else None

    result = {"div": div_content, "p": p_content}
    print(result)

html_content = """
<div>
    This div
      text
    <p>this is the para</p>
    text
</div>
"""

scrape_html_content(html_content)
