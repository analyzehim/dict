
import requests
'''
from requests.auth import HTTPProxyAuth

proxyDict = { 
          'http'  : '10.64.48.7', 
          'https' : 'proxy.avp.com'
        }
auth = HTTPProxyAuth('KL\Raev_e', 'Nwcfafnir123')

URL = 'https://api.telegram.org/bot' # HTTP Bot API URL
TOKEN = '119170444:AAGu9QuWoZ7WFAIQS-1q1Az4rhzHQdiFfDk' # My Token
ADMIN_ID = 74102915
text="Hello"
data = {'chat_id': ADMIN_ID, 'text': text} 
request = requests.post(URL + TOKEN + '/sendMessage', proxies=proxyDict, auth=auth)
print r.status_code
'''


r = requests.get('http://127.0.0.1:8000/polls/clean')
print r.text 


r=requests.get('http://127.0.0.1:8000/polls/parse')
print r.text
