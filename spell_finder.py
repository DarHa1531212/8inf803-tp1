from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
import json

from pyspark.sql.catalog import Column
from pyspark.sql.functions import lit, concat_ws, concat, collect_list, array

conf = SparkConf().setAppName('Spell Finder')
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")
spark = SparkSession(sc)

data = json.load(open("results/result.json"))
rdd = sc.parallelize(data)
df = rdd.toDF()

result = df.filter(df.level <= 4)
result = result.where(df.components == array(*(lit(x) for x in ['V']))).collect()

# print(type(result))
rdd2 = sc.parallelize(result)
df2 = rdd2.toDF()
df2.printSchema()
df2.show(truncate=False)


def stringify(c: Column):
    return concat(concat_ws(",", c))


df2.withColumn("components", stringify("components")).toPandas().to_csv("results/result2.csv", header=True)
