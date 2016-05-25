__author__ = 'hyeonsj'



nums = sc.parallelize([1, 2, 3, 4])

squared = nums.map(lambda x: x*x).collect()

for num in squared:
    print("%i " % (num))


"""
1
4
9
16
"""