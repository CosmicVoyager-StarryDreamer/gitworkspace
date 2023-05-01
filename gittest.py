def sum_of_unique(nums):
    list1 = []
    for i in set(nums):
        if nums.count(i) == 1:
            list1.append(i)
    return sum(list1)

nums = [1,2,3,2]
print(sum_of_unique(nums))


