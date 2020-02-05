#练习题1：计算1-2之和。
#注意range的函数解释
total = 0
for i in range(1, 3):
    total += i
print(total)

#练习题2：打出1-20的质数
#思路：构建一个是否能除被除的函数,并返回true，false
def judge(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

for i in range(2,21):
    if judge(i) == 1:
        print(i)

#数据结构
#堆