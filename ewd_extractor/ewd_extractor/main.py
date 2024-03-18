import sys
import json

from bs4 import BeautifulSoup

EWD_DOMAIN_ROOT = 'https://www.cs.utexas.edu/users/EWD/'

def extract_ewd_entries(index_html):
    parser = BeautifulSoup(index_html, 'html.parser')

    # TODO: Locate any hrefs that fail
    ewd_href = lambda tag: (tag.name == 'a') and (tag.has_attr('href')) and (tag['href'].startswith('ewd'))
    entries = parser.find_all(ewd_href)
    entry_json = [
        { 
            'title': entry.text,
            'link': EWD_DOMAIN_ROOT + entry['href']
        }
        for entry in entries
    ]

    return entry_json

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Required argument: ewd index html filename.', file=sys.stderr)
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as f:
            print(json.dumps((extract_ewd_entries(f.read()))))
    except FileNotFoundError:
        print(f'File {filename} does not exist.')
        sys.exit(1)