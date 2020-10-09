import requests, json, os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail, PlainTextContent,
    HtmlContent, SendGridException
)
from python_http_client.exceptions import HTTPError

base_url = "http://ngleadersdb.herokuapp.com/api"

r = requests.get(f"{base_url}/senator/all")
data = r.json()
#emails = [i['sen_email'] for i in data['data']]
emails = ['asalupaul36@gmail.com']
print(open('message.txt','r'))

def sendMail():
    message = Mail(
        from_email = os.getenv('hostemail'),
        to_emails = emails,
        subject = "EMERGENCY!!",
        plain_text_content = open('message.txt','r').read()
    )
    try:
        sg = SendGridAPIClient(os.environ.get('API_KEY'))
        resp = sg.send(message)
        return True
    except HTTPError as e:
        #print(f"{resp.status_code}'\n'{resp.body}'\n'{resp.headers}")
        print(e.to_dict)
        return False
    else:
        print(e.to_dict)
        return False

if __name__ == "__main__":
    sendMail()
    
    
    