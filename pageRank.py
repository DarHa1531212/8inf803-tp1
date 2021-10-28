from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from page import Page
import psutil

conf = SparkConf().setAppName('PageRank')
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")
spark = SparkSession(sc)

A = Page('A', ['C', 'B'], 1)
B = Page('B', ['C'], 1)
C = Page('C', ['A'], 1)
D = Page('D', ['C'], 1)

nodeList = [('A', A), ('B', B), ('C', C), ('D', D)]
graph_RDD = sc.parallelize(nodeList)
test = []

def map_to_page(page, new_page_rank):
    page.pageRank = new_page_rank
    return page

for i in range(20):
    message_RDD = graph_RDD.flatMap(lambda page: page[1].send_messages()).reduceByKey(lambda a, b: a + b)\
        .mapValues(lambda page_rank: page_rank * 0.85 + 0.15)
    print('-------------------------------------------------------------------')
    print('Iteration ' + str(i + 1) + ':')
    print(message_RDD.take(4))
    print('-------------------------------------------------------------------')
    graph_RDD = graph_RDD.join(message_RDD)\
        .mapValues(lambda page_tuple: map_to_page(page_tuple[0], page_tuple[1])).cache()
