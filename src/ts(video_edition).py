##########################################
#
#              Tiny Scraper
#
#    A minimalist web scraping library
#         (created just for fun)
#
#                   by
#
#            Code Monkey King
#
##########################################

# packages
from urllib.request import Request
from urllib.request import urlopen
import json
import re

# parser
def parse(url, *args, **kwargs):
    try:
        # create request object
        request = Request(url, **kwargs)
        
        # handle method keyword availability
        try:
            request.__dict__['method']
        
        except:
            request.__dict__['method'] = 'GET'

        # print request info
        print(' Tiny Scraper: HTTP "%s" to URL: %s' % 
                 (request.__dict__['method'], url))

        # make HTTP request to the target URL
        response = urlopen(request)

        # print response status code
        print(' Tiny Scraper: Response %s' % response.getcode())

        # extract HTML text from response
        response = response.read().decode(encoding='utf-8', errors='ignore')

        # init regex to parse HTML
        regex = r'''(< *\w+( +\w+( *= *[\"|'][^\"|^']+[\"|'])?)* */? *>)([^<]*)'''        

        # try custom regular expresiion if available
        try:
            regex = args[0]
            print(' Tiny Scraper: using custom regular expression %s', regex)
        
        except:
            pass
            
        # parse content
        content = [
            {
                'tag': item[0].strip('<>').split()[0],
                'attrs': [
                    {
                        attr.split('=')[0]: attr.split('=')[-1]
                                                .strip('"')
                                                .strip("'")
                    }
                    for attr in
                    item[0].replace(': ', ':').strip('>').split()[1:]
                ],
                'text': item[-1]
            }
            for item in
            re.findall(regex, response)
        ]
        
        # fix tag attributes type
        for item in content:
            try:
                item['attrs'] = item['attrs'][0]
            
            except:
                item['attrs'] = {}
        
        # init available attrs for emty tags
        all_attrs = []
        
        # loop over all tags
        for item in content:
            # store all available tag attributes
            [
                all_attrs.append(attr)
                for attr in
                list(item['attrs'].keys())
            ]
        
        # init unique attributes
        all_attrs = dict.fromkeys(all_attrs, '')
        
        # apply unique attributes
        for item in content:
            if item['attrs'] == {}:
                item['attrs'] = all_attrs
                
        # return parsed content
        return content
    
    except Exception as e:
        print(' Tiny Scraper: error', e)

# tests
if __name__ == '__main__':
    # parse quotes
    content = parse('http://quotes.toscrape.com')

    # print all tag names
    print('\n\nAll tag names:\n')
    for item in content:
        print(item['tag'])
    
    # print all tag attributes
    print('\n\nAll tag attributes:\n')
    for item in content:
        print(item['attrs'])
    
    # print all tag textual nodes
    print('\n\nAll tag text:\n')
    for item in content:
        print(item['text'])
    
    # print all tag elements
    print('\n\nAll tag elements:\n')
    print(json.dumps(content, indent=2))
    
    
    # print all quotes
    print('\n\nExtracted quotes:\n')
    quotes = [
        print(item['text'])
        for item in content
        if item['tag'] == 'span' and
           item['attrs']['class'] == 'text'
    ]
    
    # print all authors
    print('\n\nExtracted authors:\n')
    authors = [
        print(item['text'])
        for item in content
        if item['tag'] == 'small' and
           item['attrs']['class'] == 'author'
    ]
    
    # print all author links
    print('\n\nAuthor detail URLs:\n')
    links = [
        print(item['attrs']['href'])
        for item in content
        if item['tag'] == 'a' and
           item['text'] == '(about)'
    ]












