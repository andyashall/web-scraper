import requests
from lxml import html

url = 'https://andrewashall.com'

def get_parsed_page(url):
  response = requests.get(url, headers = {'User-agent': 'ws 0.1'})
  parsed_page = html.fromstring(response.content)
  return parsed_page

parsed_page = get_parsed_page(url)

post_urls = parsed_page.xpath('///h1/a/@href')

for post_url in post_urls:
    print('Post url:', post_url)
    
    parsed_post_page = get_parsed_page(f'{url}{post_url}')
    paragraph_titles = parsed_post_page.xpath('//h1/text()')
    paragraph_titles = map(lambda x: ' \n  ' + x, paragraph_titles)
    paragraphs = parsed_post_page.xpath('//p/text()')
    paragraphs = map(lambda x: ' \n  ' + x, paragraphs)
    print(''.join(paragraph_titles) + '\n')
    print(''.join(paragraphs) + '\n')