<<<<<<< HEAD
def sum_of_unique(nums):
    list1 = []
    for i in set(nums):
        if nums.count(i) == 1:
            list1.append(i)
    return sum(list1)

nums = [1,2,3,2]
print(sum_of_unique(nums))


=======
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
>>>>>>> hot-fix

num=input('请输入一个非负整数：')
while len(num) > 1: # while循环在未知循环次数时使用
    total = 0 # 每次循环的时候累加变量重置为0
    for i in num: # 只有可迭代对象才可以遍历哈
        total += int(i) # 对可迭代对象的每个元素转化成int类型,进行累加
    num = str(total) # 只有可迭代对象才可以遍历哈
print(num) # 这里只能是num,因为如果输入的个位数,那么while就不会执行,也就不可能出现total变量啦
