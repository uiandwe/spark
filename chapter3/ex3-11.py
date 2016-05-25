__author__ = 'hyeonsj'

inputRDD = sc.textFile("log1.log")
errorsRDD = inputRDD.filter(lambda x: "error" in x)
warningsRDD = inputRDD.filter(lambda x: "warning" in x)
badLinesRDD = errorsRDD.union(warningsRDD)
badLinesRDD.count()