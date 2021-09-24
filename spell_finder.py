from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('MyFirstStandaloneApp')
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")

rdd = sc.parallelize("./results/result.json")
df = rdd.toDF()
result = df.filter(df.level <= 4).collect()
print(result)
