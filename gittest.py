
def sum_of_unique(nums):
    list1 = []
    for i in set(nums):
        if nums.count(i) == 1:
            list1.append(i)
    return sum(list1)

nums = [1,2,3,2]
print(sum_of_unique(nums))



'''

定义函数实现：输出100以内的孪生质数

学生质数就是指相差2的质数对，例如3和5,5和7,11和13


'''

def func(num):
    if num < 2:
        return False
    for i in range(2,num):
        if (num % i) == 0 :
            return False
        
    return True

def func2(n = 100): #  默认参数
    for i in range(n):
        if func(i) and func(i+2):
            print(i,i+2)


func2(200)





for right in range(1,10):
    for left in range(1,right + 1):
        print(f'{left}X{right}={left*right}',end='\t')
    print()
