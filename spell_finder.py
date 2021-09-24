from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
import json

conf = SparkConf().setAppName('Spell Finder')
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")
spark = SparkSession(sc)

data = json.load(open("C:/Users/user/Desktop/UQAC_3A/8INF803_Base_de_donnée_répartie/TP_BDR/TP1_BDR/results/result.json"))
rdd = sc.parallelize(data)
df = rdd.toDF()
"""
df.printSchema()
df.show(truncate=False)
"""
result = df.filter(df.level.contains("wizard 1")
                   | df.level.contains("wizard 2")
                   | df.level.contains("wizard 3")
                   | df.level.contains("wizard 4")).collect()

#result = df.filter(df.level <= 4).collect()

#print(type(result))
rdd2 = sc.parallelize(result)
df2 = rdd2.toDF()
df2.printSchema()
df2.show(truncate=False)



"""
result = df.filter(df.level <= 4).collect()
print(result)
"""
