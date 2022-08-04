import datetime

#import dateutil.parser
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup


class Scrapper(object):
    """ 
    Base class to each of the scrappers used.
    @url: which page search for.
    @headers: accept language.
    @component: wich one is the HTML component that has the info.
    """

    def __init__(self, url, cinema=None):
        """
        Initialize the Soup library data.
        """
        self.url = url
        self.headers = {"Accept-Language": "en-US, en;q=0.5"}
        self.events = []
        self.soup = BeautifulSoup(self._request_url().content, "html.parser")
        self.cinema = cinema

    def _request_url(self):
        return requests.get(url=self.url, headers=self.headers)

    def _initialize(self):
        pass

    def _read_event(self):
        pass

    def _create_event(self, event):
        self.events.append(event)

    def run(self):
        return self._initialize()


class User(object):
    name: str
    number: int
    sign: str

    def __init__(self, name, number, sign):
        self.name = name
        self.number = number
        self.sign = sign


class Sign(object):
    name: str
    url: str
    message: str


class HoroscopeScrapper(Scrapper):
    """
    Scrapper in charge of reading the Horoscopo semanal data.
    """

    STAR_SIGNS = [
        'ARIES', 'TAURO', 'GÉMINIS',
        'CÁNCER', 'LEO', 'VIRGO', 'LIBRA',
        'ESCORPIO', 'SAGITARIO', 'CAPRICORNIO',
        'ACUARIO', 'PISCIS',
    ]
    DATA = []
    USERS = []
    TO = [
        {
            'name': 'Julian',
            'number': 5493517712831,
            'sign': 'SAGITARIO'
        },
        {
            'name': 'Tabaporri',
            'number': 5491122959804,
            'sign': 'TAURO'
        },
        {
            'name': 'Nicorri',
            'number': 5493547560104,
            'sign': 'GÉMINIS'
        },
        {
            'name': 'Negrito',
            'number': 5493585601719,
            'sign': 'VIRGO'
        },
        {
            'name': 'Franirani',
            'number': 5493513666150,
            'sign': 'GÉMINIS'
        },
        {
            'name': 'Nico',
            'number': 5493512421306,
            'sign': 'LEO'
        },
        {
            'name': 'Tulo(facha)',
            'number': 5493412278025,
            'sign': 'TAURO'
        }
    ]

    def __init__(self):
        super().__init__(url='https://horoscoponegro.com/horoscopo-semanal/')
        for dest in self.TO:
            self.USERS.append(
                User(dest.get('name'), dest.get('number'), dest.get('sign')))

    def run(self):
        self._read_main_page()
        return self.events

    def _read_main_page(self):
        for star_sign in self.soup.find_all(class_='fusion-column-wrapper'):
            sign = star_sign.h2.get_text() if star_sign.h2 else ''
            if sign in self.STAR_SIGNS:

                self.DATA.append({
                    'sign': sign,
                    'url': star_sign.find(class_='fusion-imageframe').a['href'],
                    'message': ''
                })
        self._read_each_sign()

    def _read_each_sign(self):
        for data in self.DATA:
            super().__init__(url=data.get('url'))
            info = self.soup.find(class_='fusion-text')
            for text in info.find_all('p'):
                data['message'] = data['message'] + text.get_text()
        self._send_bulk_sms()

    def _send_bulk_sms(self):
        for user in self.USERS:
            for sign in self.DATA:
                if sign.get('sign') == user.sign:
                    self._send_sms(sign.get('url'), user)
                    break

    def _send_sms(self, message: str, user: User):
        url = "https://d7sms.p.rapidapi.com/secure/send"

        payload = {
            "content": f'Hola {user.name}! Tu horoscopo semanal: {message}. No te olvides de fumar churro!',
            "from": "D7-Rapid",
            "to": user.number
        }
        headers = {
            "content-type": "application/json",
            "Authorization": "Basic dmF5eDcwNjM6cGZ2RGx3blM=",
            "X-RapidAPI-Key": "c272f856c8msh4a9e73f7c5b655ap17f3f2jsn21868c6a561d",
            "X-RapidAPI-Host": "d7sms.p.rapidapi.com"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        if response.status_code == 200:
            print(f'message succes to {user.name}')
            return
        print(f'failed to send message to {user.name}')


HoroscopeScrapper().run()
