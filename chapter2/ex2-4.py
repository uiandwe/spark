__author__ = 'hyeonsj'
lines = sc.textFile("README.md")
pythonLines = lines.filter(lambda line: "Python" in line)
pythonLines.first()
#u'high-level APIs in Scala, Java, Python, and R, and an optimized engine that'

