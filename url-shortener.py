import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

url_to_shorten = 'https://www.example.com'
short_url = shorten_url(url_to_shorten)
print(short_url)