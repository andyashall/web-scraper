import requests
from lxml import html

url = 'https://andrewashall.com'

def get_parsed_page(url):
  r = requests.get(url, headers = {'User-agent': 'ws 0.1'})
  if r.ok:
    page = html.fromstring(r.content)
  else:
    page = False
  return page

parsed_page = get_parsed_page(url)

post_urls = parsed_page.xpath('///h1/a/@href')

file_name = url.replace('https://', '').replace('.com', '')

file = open(f'{file_name}.txt', 'a')

for post_url in post_urls:
    print(f'Post url: {post_url}', file=file)
    
    parsed_post_page = get_parsed_page(f'{url}{post_url}')
    paragraph_titles = parsed_post_page.xpath('//h1/text()')
    paragraph_titles = map(lambda x: ' \n  ' + x, paragraph_titles)
    paragraphs = parsed_post_page.xpath('//p/text()')
    paragraphs = map(lambda x: ' \n  ' + x, paragraphs)
    print(''.join(paragraph_titles) + '\n', file=file)
    print(''.join(paragraphs) + '\n', file=file)
    file.flush()