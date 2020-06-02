# Tiny Scraper
Beginners friendly WEB SCRAPING library intended to improve your python data structures referencing skills

# Documentation
    FUNCTION:
        parse(uri, *args, **kwargs)
            uri - target URL or local file PATH to request, e.g. "http://quotes.toscrape.com", "local.html"
          *args - REGEX string, e.g. r'your_regex' - supposed to be the ONLY non-keyword argument
       **kwargs - keyword arguments wraping urllib.request.Request arguments, e.g. (method="POST", headers={'accept': '*'})
       
    RETURNS:
        Dictionary with the following keys: ['response'], ['text'], ['tags'] where
            response - is a urllib.request.urlopen() response object
                text - response text in "utf-8" encoding
                tags - list of dictionaries with the following keys: ['tag'], ['attrs'], ['text'] where
                           tag - tag name
                         attrs - dictionary of tag attributes, e.g. {'class': 'text', 'id': 'card'}
                          text - textual node of a tag

# How to use it (CHEAT SHEET)
```python
# # import Tiny Scraper assuming it's located in the same directory
from ts import *

# make HTTP request
content = parse('http://quotes.toscrape.com')

# get response object
print('\n\nResponse object:\n', content['response'])

# get response text
print('\n\nHTML document:\n', content['text'])

# print all tag elements
print('\n\nAll tag elements:\n')
print(json.dumps(content['tags'], indent=2))

# print all tag names
print('\n\nAll tag names:\n')
for item in content['tags']:
    print(item['tag'])

# print all tag attributes
print('\n\nAll tag attributes:\n')
for item in content['tags']:
    print(item['attrs'])

# print all tag textual nodes
print('\n\nAll tag text:\n')
for item in content['tags']:
    print(item['text'])    

# print all quotes
print('\n\nExtracted quotes:\n')
quotes = [
    print(item['text'])
    for item in content['tags']
    if item['tag'] == 'span' and
       item['attrs']['class'] == 'text'
]

# print all authors
print('\n\nExtracted authors:\n')
authors = [
    print(item['text'])
    for item in content['tags']
    if item['tag'] == 'small' and
       item['attrs']['class'] == 'author'
]

# print all author links
print('\n\nAuthor detail URLs:\n')
links = [
    print(item['attrs']['href'])
    for item in content['tags']
    if item['tag'] == 'a' and
       item['text'] == '(about)'
]

# print all tags
print('\n\nAll tags:\n')
tags = [
    print(item['text'], item['attrs']['href'])
    for item in content['tags']
    if item['tag'] == 'a' and
       item['attrs']['class'] == 'tag'
]

```

# Tiny Scraper CRASH COURSE (Basic)
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/btlVL8J6TiY/0.jpg)](https://www.youtube.com/watch?v=btlVL8J6TiY)

# Tiny Scraper CRACH COURSE (Advanced)
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/1s0cevhIcAw/0.jpg)](https://youtu.be/1s0cevhIcAw)


