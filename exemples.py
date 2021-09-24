from bs4 import BeautifulSoup
import requests

#Exemple 1
"""
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml') #lxml == parseur
jobs = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')

for job in jobs:
    published_date = jobs.find('span', class_='sim-posted').text.replace(' ', '')
    compagny_name = jobs.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
    skills = jobs.find('span', class_ = 'srp-skills').text.replace(' ', '')

    print(f'''
    Compagny Name: {compagny_name}
    Required Skills: {skills}
    Published Date: {published_date}
    ''')
"""


#Exemple 2
"""
html_text = requests.get('http://quotes.toscrape.com/').text
soup = BeautifulSoup(html_text, 'lxml')
quotes = soup.find_all('span', class_ = 'text')

for quote in quotes:
    print(quote.text)

print('end')
"""

# Shakespeare
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('MyFirstStandaloneApp')
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")

text_file = sc.textFile("C:/Users/user/Desktop/UQAC_3A/8INF803_Base_de_donnée_répartie/TP_BDR/TP1_BDR/shakespeare.txt")

counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)

print ("Number of elements: " + str(counts.count()))