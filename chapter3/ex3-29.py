__author__ = 'hyeonsj'


lines = sc.parallelize(["hello world", "hi"])
words = lines.flatMap(lambda line: line.split(" "))
words.first()

#'hello'