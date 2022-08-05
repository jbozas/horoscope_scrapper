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
        self.headers = {"Accept-Language": "en-US, en;q=0.5"}
        self.soup = BeautifulSoup(self._request_url().content, "html.parser")

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
        for star_sign in self.soup.find_all(class_='fusion-column-wrapper'):
            if star_sign.h2:
                sign = self.dataclass.get_sign(star_sign.h2.get_text())
                sign.url = star_sign.find(class_='fusion-imageframe').a['href']

        self._read_each_sign()

    def _read_each_sign(self):
        for sign in self.dataclass.signs:
            super().__init__(url=sign.url)
            info = self.soup.find(class_='fusion-text')
            for text in info.find_all('p'):
                sign.message += text.get_text()
        # self._send_bulk_sms()

    # def _send_bulk_sms(self):
    #     for user in self.USERS:
    #         for sign in self.DATA:
    #             if sign.get('sign') == user.sign:
    #                 self._send_sms(sign.get('url'), user)
    #                 break


HoroscopeScrapper().run()
