import ipdb
import requests

url = "https://d7sms.p.rapidapi.com/secure/send"

payload = {
    "content": "Test Message",
    "from": "D7-Rapid",
    "to": '+5493517712831'
}
headers = {
    "content-type": "application/json",
    "Authorization": "undefined",
    "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
    "X-RapidAPI-Host": "d7sms.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

ipdb.set_trace()
print(response.text)
