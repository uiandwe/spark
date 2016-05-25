__author__ = 'hyeonsj'


inputRDD = sc.textFile("./log1.log")
errorsRDD = inputRDD.filter(lambda x: "error" in x)
warningsRDD = inputRDD.filter(lambda x: "warning" in x)
badLinesRDD = errorsRDD.union(warningsRDD)

print("Input had" + str(badLinesRDD.count()) + "concerning lines")
print("Here are 10 examples:")

for line in badLinesRDD.take(10):
    print(line)

