import requests
from bs4 import BeautifulSoup
from fake_useragent import FakeUserAgent

headers = {'User-Agent': FakeUserAgent()}

def main():
    session = requests.get('https://twitter.com/elonmusk', headers=headers)
    page = BeautifulSoup(session.content, 'lxml')
    print(page.text)
    


if __name__ == '__main__':
    main()