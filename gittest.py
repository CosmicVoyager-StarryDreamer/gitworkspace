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
