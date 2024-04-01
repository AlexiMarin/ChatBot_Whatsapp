import requests
import configparser
import json

config = configparser.ConfigParser()
config.read('credentials.txt')
wsp = config['whatsapp']
token_ = wsp['token']
number = wsp['number']
def SendMessageWhatsapp(data):
    try:
        token = token_
        api_url = f'https://graph.facebook.com/v18.0/{number}/messages' 
        
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
        response = requests.post(api_url, data = json.dumps(data), headers = headers)

        if response.status_code == 200:
            return True
        
        return False
    except Exception as e:
        print('error wsp' + e)
        return False
