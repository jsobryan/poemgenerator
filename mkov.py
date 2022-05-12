import tweepy
import markovify
import re
import random
import warnings
import names
warnings.filterwarnings('ignore')

#utility function for text cleaning
def text_cleaner(text):
  text = re.sub(r'--', ' ', text)
  text = re.sub('[\[].*?[\]]', '', text)
  text = re.sub(r'(\b|\s+\-?|^\-?)(\d+|\d*\.\d+)\b','', text)
  text = ' '.join(text.split())
  return text

with open('poemfodder.txt','r') as f:
    content = f.read()


data = text_cleaner(content)

generator = markovify.Text(data,state_size=1)

#utility function for text cleaning
def text_cleaner(text):
  text = re.sub(r'--', ' ', text)
  text = re.sub('[\[].*?[\]]', '', text)
  text = re.sub(r'(\b|\s+\-?|^\-?)(\d+|\d*\.\d+)\b','', text)
  text = ' '.join(text.split())
  return text

with open('poemfodder.txt','r') as f:
    content = f.read()

data = text_cleaner(content)

generator = markovify.Text(data,state_size=1)

def lines():
    return generator.make_short_sentence(max_chars=random.randint(15,30),tries=1000)

def stanzas():
    for i in range(random.randint(3,6)):
        print(lines())
def shortstanza():
    for i in range(random.randint(1,3)):
        print(lines())
def lnbreak():
    print('\r\r')

stanzas()
lnbreak()
stanzas()
print('\n')



 
