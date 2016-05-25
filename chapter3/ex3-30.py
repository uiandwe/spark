__author__ = 'hyeonsj'


nums = sc.parallelize([1, 2, 3, 3])

squared = nums.map(lambda x: x+1).collect()

for num in squared:
    print("%i " % (num))

squared = nums.filter(lambda x: x != 1).collect()

for num in squared:
    print("%i " % (num))


squared = nums.distinct().collect()

for num in squared:
    print("%i " % (num))

nums1 = sc.parallelize([1, 2, 3])
nums2 = sc.parallelize([3, 4, 5])

squared = nums1.union(nums2).collect()

for num in squared:
    print("%i " % (num))

squared = nums1.intersection(nums2).collect()

for num in squared:
    print("%i " % (num))


squared = nums1.subtract(nums2).collect()

for num in squared:
    print("%i " % (num))


