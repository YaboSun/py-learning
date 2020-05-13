from functools import reduce

f = abs
print(f(-1))


def f(x):
    return x * x


r = map(f, [0, 1, 2, 3, 4, 5, 6, 7])
print(list(r))


# 将用户输入的不规范转化为首字母大写，其他小写
def normalize(name):
    ret = name[0].upper()
    for i in range(1, len(name)):
        ret = ret + name[i].lower()
    return ret


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 将字符串转化为数组，并得到最后的整数值，例如'13579'--[1,3,5,7,9]--13579
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


def fn(x, y):
    ret = x * 10 + y
    return ret


print(reduce(fn, map(char2num, '13579')))

# 将以上功能整理成一个计算str2int的函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def char2num(s):
        return DIGITS[s]

    def fn(x, y):
        return x * 10 + y

    return reduce(fn, map(char2num, s))


print(str2int('13579'))


# 练习2
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    def fn(x, y):
        return x * y

    return reduce(fn, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 练习3：利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
# 思路一：首先按照点将浮点数进行分割，将分割之后的数按照同样的处理方式，整数部分从前到后，小数部分从后到前
def str2float(s):
    l1, l2 = 0, 0

    def fn(x, y):
        return x * 10 + y

    def cn(x, y):
        return x * 0.1 + y

    def char2num(s):
        return DIGITS[s]

    for i in range(0, len(s)):
        if s[i] == '.':
            l1 = reduce(fn, map(char2num, s[:i]))
            # list从后往前取的过程
            # 特别要注意第二个冒号前的那个缺省值，如果什么都不填，则一直遍历到列表的index=0的位置；
            # 如果填0，则默认一直遍历到列表的index =1的位置，如果填1，则默认一直遍历到列表的index =2的位置，依次往后。
            # 而第一个冒号前的那个缺省值，默认是从index = n-1的位置（列表末位）开始数起，填几就从第几号索引开始。
            # 甚至可以填比n-1大的值，但是也还是从最后一位开始遍历
            l2 = reduce(cn, map(char2num, s[len(s) - 1:i - len(s):-1]))
    return l1 + l2 / 10


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('test passed!')
else:
    print('测试失败!')
