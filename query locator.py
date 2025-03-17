#Tells you if the inputted query (word or url) exists on the target page

import urllib.request
import re

# URL + Headers
url = input('what\'s the url: ')
if len(url) < 1:
    url = 'https://www.levels.com/blog/can-eating-carbs-last-reduce-blood-sugar-spikes'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Search Query
search = input('search term? (url, word, or phrase): ')
if len(search) < 1:
    print("yo there's no search term")
    pass

else:
    # New Request
    req = urllib.request.Request(url, headers=headers)

    # Read and decode HTML
    html = urllib.request.urlopen(req).read().decode('utf-8')

    # Check if search term exists
    if re.search(re.escape(search), html):
        print(f"\n✅ yo i found '{search}' in the webpage.")
    else:
        print(f"\n❌ soz bro i didn\'t find '{search}' in the webpage.")

