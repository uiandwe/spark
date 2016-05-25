__author__ = 'hyeonsj'

word = inputRDD.filter(lambda s: "error" in s)


def containsError(s):
    return "error" in s
word = inputRDD.filter(containsError)
