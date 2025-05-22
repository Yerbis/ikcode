import requests

def gen_from_urls(urls: tuple):     # Unused, just a test
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url

urls = ('http://ikcodeii.pythonanywhere.com', 'http://youtube.com', 'http://statefarm.com') # LIKE A GOOD NEIGHBOR STATE FAARM IS THEREE

for resp in (requests.get(url) for url in urls):
    print(len(resp.content), '->', resp.status_code, '->', resp.url)
