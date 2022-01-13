import requests
urls = ('http://talkpython.fm', 'http://pythonpodcast.com', 'http://python.org')


def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url


for item in (gen_from_urls(urls)):
    print(item)
