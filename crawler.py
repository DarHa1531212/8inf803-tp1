from bs4 import BeautifulSoup
import requests
from utils import *
import json
import re

#Crawler de sorts
main_page = requests.get('https://aonprd.com/Spells.aspx?Class=All')
soup = BeautifulSoup(main_page.content, 'lxml')

for link in soup.find_all('a')[98:110]: #[105:108] #3137
    page = requests.get('https://aonprd.com/'+link.get('href'))
    soup_bis = BeautifulSoup(page.content, 'lxml')
    table_html = soup_bis.find_all('table')[-1]
    #print(table_html)

    spans_html = table_html.find_all('span')
    #print(len(spans_html))

    for i in range(len(spans_html)):
        try:
            span = spans_html[i].get_text()
            #print(span)
        except:
            pass
        try:
            print("name:", spans_html[i].find_all("h1")[i].text).strip()
        except:
            pass
        try:
            if (findnth(span, 'Level', i) != -1):
                print("level:", span[findnth(span, 'Level ', i)+6:findnth(span, 'Casting', 2*i)]) # la bidouille ~(-_-)~
        except:
            pass
        try:
            if (findnth(span, 'Components', i) != -1):
                print("components:", span[findnth(span, 'Components ', i)+11:findnth(span, 'EffectRange', i)])
        except:
            pass
        try:
            if (findnth(span, 'Components', i) != -1):
                print("spell_resistance:", True if ("Spell Resistance" in span[findnth(span, 'Effect', i):findnth(span, 'Description', i)]) else False)
                print("\n")
        except:
            pass



