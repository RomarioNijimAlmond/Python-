nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(type(nums2))
print(len(nums))
print(len(nums2))

nums_duplicate = {1, 2, 2, 3}
print(nums_duplicate)

# true is duplicate of 1 and false is duplicate of 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

morenums = {5, 6, 7}
nums.update(morenums)
print(nums)


one = {1, 2, 3}
two = {5, 6, 7}

mynew = one.union(two)
print(one)
print(two)
print(mynew)
