from scrappers import HoroscopeScrapper
from message import WhatsappSendMessage


def main():
    sender = WhatsappSendMessage()
    scrapper = HoroscopeScrapper()
    scrapper.run()
    data = scrapper.dataclass
    for user in data.users:
        sign = data.get_sign(user.sign)
        sender.send_message(user=user, message=sign.message)


if __name__ == "__main__":
    main()
