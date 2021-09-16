from bs4 import BeautifulSoup
import requests
import json
import re

#Crawler de sorts
html_text = requests.get('https://aonprd.com/Spells.aspx?Class=All')
soup = BeautifulSoup(html_text.content, 'html.parser')


for link in soup.find_all('a')[98:99]: #3137
    page = requests.get('https://aonprd.com/'+link.get('href'))
    soup_bis = BeautifulSoup(page.content, 'html.parser')
    #sort_html = soup_bis.find(id='ctl00_MainContent_DataListTypes_ctl00_LabelName') #.text.replace(' ', '')
    sort_html = soup_bis.find_all('span')[-1]
    for token in sort_html:
        print(token)

    #print(sort_html)
    #print('\n')


    """
    print("name:", sort_html.find("h1").text)
    print("level:", sort_html.get_text()[sort_html.get_text().find('Level ') + 6:sort_html.get_text().find('Casting')])
    print("components:", sort_html.get_text()[sort_html.get_text().find('Components ') + 11:sort_html.get_text().find('EffectRange')])
    print("spell_resistance:", True if ("Spell Resistance" in sort_html.get_text()) else False)
    print('\n')
    """

    """
    sort = {
        "name":sort_html.find("h1").text
        "level":sort_html.get_text()[sort_html.get_text().find('Level ')+6:sort_html.get_text().find('Casting')]
        "components":sort_html.get_text()[sort_html.get_text().find('Components ')+11:sort_html.get_text().find('EffectRange')]
        "spell_resistance":True if ("Spell Resistance" in sort_html.get_text()) else False
    }
    """



