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
r = random.randint(20,30)
r2 = random.randint(30,40)

def lines():
    return generator.make_short_sentence(max_chars=random.randint(25,50),tries=1000)

def poem():
    for i in range(random.randint(2,9)):
        print(lines())
    print('\r\r')
    for i in range(2,3):
        print(lines())
    print('\r\r')
    for i in range(2):
        print(lines())

print('\n')
poem()
print('\n')




# print('\n')
# for i in range(6):
#     print(lines())
# print('\n')
# print(breakline())
# print('\n')
# for i in range(random.randint(2,6)):
#     print(lines())
# print('\n')
# for i in range(2):
#     print(lines())
# print('\n')

