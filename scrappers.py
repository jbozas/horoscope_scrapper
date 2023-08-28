import requests

from bs4 import BeautifulSoup

from models import DataManager


class Scrapper(object):
    """ 
    Base class to each of the scrappers used.
    @url: which page search for.
    @headers: accept language.
    @component: wich one is the HTML component that has the info.
    """

    def __init__(self, url):
        """
        Initialize the Soup library data.
        """
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        }
        content = self._request_url().content
        self.soup = BeautifulSoup(content, "html.parser")

    def _request_url(self):
        return requests.get(url=self.url, headers=self.headers)

    def _initialize(self):
        pass

    def run(self):
        return self._initialize()


class HoroscopeScrapper(Scrapper):
    """
    Scrapper in charge of reading the Horoscopo semanal data.
    """

    def __init__(self):
        super().__init__(url='https://horoscoponegro.com/horoscopo-semanal/')
        self.dataclass = DataManager()

    def run(self):
        self._read_main_page()

    def _read_main_page(self):
        for star_sign in self.soup.find_all(class_='et_pb_column'):
            if star_sign.h2:
                sign = self.dataclass.get_sign(star_sign.h2.get_text())
                sign.url = star_sign.a['href']

        self._read_each_sign()

    def _read_each_sign(self):
        for sign in self.dataclass.signs:
            super().__init__(url=sign.url)
            info = self.soup.find(id='main-content')
            for text in info.find_all('p'):
                sign.message += text.get_text()

