from lib2to3.pgen2.pgen import generate_grammar
import markovify
import re
import random
import warnings
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

def lines():
    x = random.randint(30,50)
    return generator.make_short_sentence(max_chars=x,tries=50)

print('\n')
for i in range(4):
    print(lines())
print('\n')
print(lines())
print('\n')
for i in range(2):
    print(lines())
print('\n')
