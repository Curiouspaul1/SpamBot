#! python3
"""
Disclaimer: this script is to be used as a means to assist
in the outcry for justice in tandem with the ongoing
protest concerning unwarranted and wrongful police
brutality against young Nigerian youths. Edit the
message in the message.txt file if need be.
 
author: <Curiouspaul1>
github: https://github.com/Curiouspaul1
"""


import requests, json, os, time
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, PlainTextContent
from python_http_client.exceptions import HTTPError
from helpers import emailcheck

base_url = "http://ngleadersdb.herokuapp.com/api"

r = requests.get(f"{base_url}/senator/all")
data = r.json()
emails = [i['sen_email'] for i in data['data'] if emailcheck(i['sen_email'])]


def sendMail():
    message = Mail(
        from_email = os.getenv('hostemail'), # set sender email as envvar
        to_emails = emails,
        subject = "EMERGENCY!!",  # You can edit this
        plain_text_content = open('message.txt','r').read()
    )
    try:
        sg = SendGridAPIClient(os.environ.get('API_KEY')) # add your sendgrid api-key
        resp = sg.send(message)
        return True
    except HTTPError as e:
        print(e.to_dict)
        return False
    else:
        print(e.to_dict)
        return False


if __name__ == "__main__":
    not_ = input("Welcome Distinguished!, how many times do you want to send your message:: ")
    try:
        not_ = int(not_)
    except ValueError:
        print("Invalid entry, please enter a whole number")
    frequency = input("How often should the emails be sent (in seconds):: ")
    try:
        frequency = int(frequency)
    except ValueError:
        print("Invalid entry, please enter a whole number")
    for i in range(0,not_):
        print("Sending mails ...")
        sendMail()
        time.sleep(frequency)
    print("Done!")
    
    