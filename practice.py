# from bs4 import BeautifulSoup
# import requests

# url = ("https://raw.githubusercontent.com/"
# "joelgrus/data/master/getting-data.html")
# html = requests.get(url).text
# soup = BeautifulSoup(html, 'html5lib')

# first_paragraph = soup.find('p') 
# print(first_paragraph)

# first_paragraph_text = soup.p.text
# first_paragraph_words = soup.p.text.split()
# print(first_paragraph_text)
# print(first_paragraph_words)

# first_paragraph_id = soup.p['id'] # raises KeyError if no 'id'
# first_paragraph_id2 = soup.p.get('id') # returns None if no 'id'
# print(first_paragraph_id)
# print(first_paragraph_id2)

# all_paragraphs = soup.find_all('p') # or just soup('p')
# paragraphs_with_ids = [p for p in soup('p') if p.get('id')]
# print(all_paragraphs)
# print(paragraphs_with_ids)

# important_paragraphs = soup('p', {'class' : 'important'})
# important_paragraphs2 = soup('p', 'important')
# important_paragraphs3 = [p for p in soup('p') if 'important' in p.get('class', [])]
# print(important_paragraphs)
# print(important_paragraphs2)
# print(important_paragraphs3)

# spans_inside_divs = [span
# for div in soup('div') # for each <div> on the page
# for span in div('span')] # find each <span> inside it
# print(spans_inside_divs)


from bs4 import BeautifulSoup
import requests
url = "https://www.house.gov/representatives"
text = requests.get(url).text
soup = BeautifulSoup(text, "html5lib")
all_urls = [a['href']
for a in soup('a')
if a.has_attr('href')]
# print(len(all_urls)) # 965 for me, way too many


import re
regex = r"^https?://.*\.house\.gov/?$"
assert re.match(regex, "http://joel.house.gov")
assert re.match(regex, "https://joel.house.gov")
assert re.match(regex, "http://joel.house.gov/")
assert re.match(regex, "https://joel.house.gov/")
assert not re.match(regex, "joel.house.gov")
assert not re.match(regex, "http://joel.house.com")
assert not re.match(regex, "https://joel.house.gov/biography")

good_urls = [url for url in all_urls if re.match(regex, url)]
print(len(good_urls)) 

good_urls = list(set(good_urls))
print(len(good_urls)) # only 431 for me

html = requests.get('https://jayapal.house.gov').text
soup = BeautifulSoup(html, 'html5lib')
# Use a set because the links might appear multiple times.
links = {a['href'] for a in soup('a') if 'press releases' in a.text.lower()}
# print(links) # {'/media/press-releases'}

# from typing import Dict, Set
# press_releases: Dict[str, Set[str]] = {}
# for house_url in good_urls:
#     html = requests.get(house_url).text
#     soup = BeautifulSoup(html, 'html5lib')
#     pr_links = {a['href'] for a in soup('a') if 'press releases'
#     in a.text.lower()}
#     # print(f"{house_url}: {pr_links}")
#     press_releases[house_url] = pr_links

# def paragraph_mentions(text: str, keyword: str) -> bool:
#     """
#     Returns True if a <p> inside the text mentions {keyword}
#     """
#     soup = BeautifulSoup(text, 'html5lib')
#     paragraphs = [p.get_text() for p in soup('p')]
#     return any(keyword.lower() in paragraph.lower()
#     for paragraph in paragraphs)

# text = """<body><h1>Facebook</h1><p>Twitter</p>"""
# assert paragraph_mentions(text, "twitter") # is inside a <p>
# assert not paragraph_mentions(text, "facebook") # not inside a <p>

# for house_url, pr_links in press_releases.items():
#     for pr_link in pr_links:
#         url = f"{house_url}/{pr_link}"
#         text = requests.get(url).text
#         if paragraph_mentions(text, 'data'):
#             print(f"{house_url}")
#             break # done with this house_url