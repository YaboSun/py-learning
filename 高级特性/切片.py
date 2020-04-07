"""
切片操作类似java中的substring，只是相对来说更方便简单
"""

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']


def getFirstNElement(n, L):
    r = []
    for i in range(n):
        r.append(L[i])
    return r


# 测试
print(getFirstNElement(2, L))
print(L[0:2])  # 使用切片slice
print(L[1:3])  # 注意的是切片选取是左闭右开[1,3)形式
print(L[-3:-1])  # 与数组一样同样支持倒数取数,倒数第一个数索引为-1
print(L[-2:])

L1 = list(range(100))  # 生成1-100数组
print(L1[:10])  # 取前10个数
print(L1[::5])  # 取所有数且每5个取一次


# 练习
def trim(s):
    # 非递归实现1
    if len(s) == 0:
        return s
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[0:-1]
    return s

    # 非递归实现2
    # for i in range(len(s)):
    #     if s[:1] == ' ':  # 这个处理比较巧妙，不是每次用s[0]
    #         s = s[1:]
    #     if s[-1:] == ' ':  # 这个处理比较巧妙，不是每次用s[-1]
    #         s = s[:-1]
    # return s

    # 递归实现
    # if s[:1] == ' ':
    #     return trim(s[1:])
    # if s[-1:] == ' ':
    #     return trim(s[:-1])
    # return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
