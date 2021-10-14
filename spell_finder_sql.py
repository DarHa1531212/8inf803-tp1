from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
import json

from pyspark.sql.catalog import Column
from pyspark.sql.functions import lit, concat_ws, concat, collect_list, array

import os

cwd = os.getcwd()
if '\\TP1_BDR' not in cwd:
    cwd += '/TP1_BDR'

conf = SparkConf().setAppName('Spell Finder')
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")
spark = SparkSession(sc)

data = json.load(open(cwd + "/results/result.json"))
#data = json.load(open('./results/result.json'))
rdd = sc.parallelize(data)
df = rdd.toDF()

df.createTempView("spells_table")

result = spark.sql("SELECT * FROM spells_table WHERE level <= 4 AND components[0] == 'V' AND cardinality(components) == 1").collect()
rdd2 = sc.parallelize(result)
df2 = rdd2.toDF()

df2.show(20)

