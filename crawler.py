from bs4 import BeautifulSoup
import requests
from utils import *
import json
import re

#Crawler de sorts
main_page = requests.get('https://aonprd.com/Spells.aspx?Class=All')
soup = BeautifulSoup(main_page.content, 'lxml')

spell = {
        "name": "NA",
        "level": "NA",
        "components": "NA",
        "spell_resistance": False,
    }

spells = []
cpt = 0

for link in soup.find_all('a')[98:3137]: #[105:108] #3137
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
            spell["name"] = spans_html[i].find_all("h1")[i].text.strip()
            #print("name:", spans_html[i].find_all("h1")[i].text.strip())
        except:
            spell["name"] = "NA"
        try:
            if (findnth(span, 'Level', i) != -1):
                spell["level"] = span[findnth(span, 'Level ', i)+6:findnth(span, 'Casting', 2*i)]
                #print("level:", span[findnth(span, 'Level ', i)+6:findnth(span, 'Casting', 2*i)]) # la bidouille ~(-_-)~
        except:
            spell["level"] = "NA"
        try:
            if (findnth(span, 'Components', i) != -1):
                spell["components"] = span[findnth(span, 'Components ', i)+11:findnth(span, 'EffectRange', i)]
                #print("components:", span[findnth(span, 'Components ', i)+11:findnth(span, 'EffectRange', i)])
        except:
            spell["components"] = "NA"
        try:
            if (findnth(span, 'Components', i) != -1):
                spell["spell_resistance"] = True if ("Spell Resistance" in span[findnth(span, 'Effect', i):findnth(span, 'Description', i)]) else False
                #print("spell_resistance:", True if ("Spell Resistance" in span[findnth(span, 'Effect', i):findnth(span, 'Description', i)]) else False, "\n")
        except:
            spell["spell_resistance"] = False

        if(spell["name"] != "NA"):
            spells.append(spell.copy())

    cpt += 1
    if(cpt%50 == 0):
        print(round(cpt/(3137-98)*100),'%')

print(round(cpt/(3137-98)*100),'%')

with open('C:/Users/user/Desktop/UQAC_3A/8INF803_Base_de_donnée_répartie/TP_BDR/TP1_BDR/results/result.json', 'w') as fout:
    fout.write('[' + ',\n'.join(json.dumps(i) for i in spells) + ']\n')