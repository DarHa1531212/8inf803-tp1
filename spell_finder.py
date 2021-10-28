from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.sql.catalog import Column
from pyspark.sql.functions import lit, concat_ws, concat, collect_list, array
from utils import *
import json
import os


#--- Bidouille pour modifier le root ---

cwd = os.getcwd()
if '\TP1_BDR' not in cwd:
    cwd += '\TP1_BDR'
#print(cwd)


#--- Initialisation de spark ---

conf = SparkConf().setAppName('Spell Finder')
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")
spark = SparkSession(sc)

#--- Récupération des sorts contenus dans le .json et transformation en rdd puis en df ---
data = json.load(open(cwd + "/results/result.json"))
rdd = sc.parallelize(data)
df = rdd.toDF()


#--- Q2 : Récupération des sorts de niveau <= 4 avec composante verbale seulement ---

result1 = df.filter((df.level <= 4) & (df.level > 0) &
                    (df.components == array(*(lit(x) for x in ['V'])))).collect()
#print(type(result1))

rdd1 = sc.parallelize(result1)
df1 = rdd1.toDF()
df1.printSchema()
df1.show(20)
print(df1.count())


#--- Q3 : Idem que Q2 mais avec requêtes SQL ---

df.createTempView("spells_table")
result2 = spark.sql("SELECT * FROM spells_table WHERE level <= 4 AND level > 0 AND "
                    "components[0] == 'V' AND cardinality(components) == 1").collect()
#print(type(result2))

rdd2 = sc.parallelize(result2)
df2 = rdd1.toDF()
df2.printSchema()
df2.show(20)
print(df2.count())


#--- Sauvegarde des df filtrés au format .json ---

df1.toPandas().to_json(cwd + '/results/result1.json', orient='records', force_ascii=False, lines=True)
df2.toPandas().to_json(cwd + '/results/result2.json', orient='records', force_ascii=False, lines=True)

#alternative pour le format .csv
#df1.withColumn("components", stringify("components")).toPandas().to_csv(cwd + "/results/result1.csv", header=True)
#df2.withColumn("components", stringify("components")).toPandas().to_csv(cwd + "/results/result2.csv", header=True)