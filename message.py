import pywhatkit
from datetime import datetime, timedelta

from models import User


class WhatsappSendMessage(object):

    def send_message(self, user: User, message: str):
        today = datetime.now() + timedelta(seconds=60)
        print(f'Sending message to {user.name}')
        message = f'Hola {user.name}! Tu horoscopo semanal de {user.sign}: {message}'
        pywhatkit.sendwhatmsg(user.number, message,
                              today.hour, today.minute)
