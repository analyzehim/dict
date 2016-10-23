import requests
r = requests.get('http://127.0.0.1:8000/polls/test')
print r.text
#print word

'''
import os
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print BASE_DIR
sys.path.append('/home/l4rs/Documents/python/dict/dict/dict/settings.py')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from models import Word
word = Word.objects.values('id').order_by('-coef')[:10]


'''