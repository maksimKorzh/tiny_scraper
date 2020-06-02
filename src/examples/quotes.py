############################################################
#
# Script to scrape quotes from http://quotes.toscrape.com
#                using Tiny Scraper library
#
#                             by
#
#                      Code Monkey King
#
############################################################

# tiny scraper package (assuming ts.py is in CWD)
from ts import *

# target URL
url = 'http://quotes.toscrape.com'

# make HTTP request to target URL
content = parse(url)

# loop over card elements
for index in range(0, len(content)):
    # select all 'div' tags with a 'class="quote"'
    if content[index]['tag'] == 'div' and content[index]['attrs']['class'] == 'quote':
        
        # store current index
        current_index = index + 1
        
        while content[current_index]['tag'] == 'div' and content[current_index]['attrs']['class'] == 'quote':
            #print(current_index)
            # increment current index
            current_index += 1
        
        print(index, current_index - 1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
