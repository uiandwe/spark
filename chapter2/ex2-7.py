__author__ = 'hyeonsj'

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf = conf)

lines = sc.textFile("/tmp/spark/spark-1.5.2/README.md")

print(lines.count())