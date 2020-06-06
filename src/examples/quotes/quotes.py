##############################################################
#
# Script to scrape quotes from http://quotes.toscrape.com
#        using Tiny Scraper web scraping library
#
#                           by
#
#                    Code Monkey King
#
##############################################################

# import Tiny Scraper assumong it's located in the same directory
from ts import *

'''
# make HTTP request to target URL
#content = parse(url)

# store HTML response locally
with open('quotes.html', 'w') as f:
    f.write(content['text'])
'''

# quotes list
quotes = []

# handle pagination
for page in range(1, 3):
    # target URL
    url = 'http://quotes.toscrape.com/page/' + str(page)
    
    # crawl next page
    content = parse(url)['tags']

    # loop over all the tags list
    for index in range(0, len(content)):
        if (
            content[index]['tag'] == 'div' and
            content[index]['attrs']['class'] == 'quote'
        ):
            
            # init current index
            current_index = index + 1

            # loop over card until hit another card
            while not (
                content[current_index]['tag'] == 'div' and
                content[current_index]['attrs']['class'] == 'quote'
            ):
                # break on <nav> tag
                if content[current_index]['tag'] == 'nav':
                    break 
                  
                # incerement curent index
                current_index += 1
            
            # extract data by card
            features = {
                'quote': ''.join([
                             content[sub_index]['text']
                             for sub_index in range(index, current_index)
                             if content[sub_index]['tag'] == 'span' and
                                content[sub_index]['attrs']['class'] == 'text'
                         ]),
                
                'author': ''.join([
                             content[sub_index]['text']
                             for sub_index in range(index, current_index)
                             if content[sub_index]['tag'] == 'small' and
                                content[sub_index]['attrs']['class'] == 'author'
                         ]),
                
                'url': ''.join([
                             content[sub_index]['attrs']['href']
                             for sub_index in range(index, current_index)
                             if content[sub_index]['tag'] == 'a'
                         ][0]),
                
                'tags': [
                            {
                                'tag': content[sub_index]['text'],
                                'url': content[sub_index]['attrs']['href']
                            }
                            for sub_index in range(index, current_index)
                            if content[sub_index]['tag'] == 'a' and
                               content[sub_index]['attrs']['class'] == 'tag'
                        ],
            }
            
            # append card data to quotes list variable
            quotes.append(features)    

# loop over quote cards
for quote in quotes:
    print(json.dumps(quote, indent=2))

# store quotes to CSV file
with open('quotes.csv', 'w') as f:
    # create CSV dictionary writer
    writer = csv.DictWriter(f, fieldnames=quotes[0].keys())
    
    # write column names
    writer.writeheader()
    
    # write data
    writer.writerows(quotes)

# store data to JSON file
with open('quotes.json', 'w') as f:
    f.write(json.dumps(quotes, indent=2))
          





















