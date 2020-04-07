import math

"""
python函数调用比较简单，直接使用对应的函数名加参数即可
"""

print(abs(-20))
print(max(1, 10, -2, 11))  # 求最大值

print(int('123'))  # 数据类型转换

a = abs  # 函数名实际上就是指向一个对象的引用，可以将其引用用变量a代替，相当于起别名
print(a(-1))

n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))

"""
自定义函数
"""


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('输入数据类型不正确')
    if x >= 0:
        x = x
    else:
        x = -x

    return x


def fun1(x, y):
    pass


print(my_abs(-1))

"""
定义可以返回多个值的函数
例如在游戏中计算物体移动位置，通过给定的坐标点，移动位移以及移动角度
返回新的位置
"""


def getXYCoordinate(x, y, step, angle):
    x = x + step * math.cos(angle)
    y = y + step * math.sin(angle)

    return x, y


x = 3
y = 5
step = 4
angle = 0
print(getXYCoordinate(x, y, step, angle))

"""
作业，实现给定a,b,c计算一元二次方程组的解
"""


def quadratic(a, b, c):
    if not isinstance(a, (int, float)) \
            or not isinstance(b, (int, float)) \
            or not isinstance(c, (int, float)):
        raise TypeError('参数类型不匹配')
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return '此方程无解'
    else:
        tmp = math.sqrt(delta)
        x1 = (-b + tmp) / (2 * a)
        x2 = (-b - tmp) / (2 * a)

    return x1, x2


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
print(quadratic(2, 1, 3))
# print(quadratic(1, 'abc', 3))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

"""
默认参数使用，例如计算x的n次方
"""


def power(x, n=2):
    p = 1
    while n > 0:
        p = p * x
        n = n - 1
    return p


# 对应测试函数
# print(power(2)) 为啥会报错？
a = power(2)
print(a)
print(power(2, 2))

"""
默认参数的坑，默认参数必须指向不可变对象
"""


def add_end(L=[]):
    L.append('END')
    return L


'''
可以看出每次针对默认参数添加的都是基于上一次的计算结果
这显然是不符合实际应用的，对于list默认指向一个对象，
而每次对其操作因为其是可变对象，所以指向的内容都发生了变化
'''
print(add_end())  # ['END']
print(add_end())  # ['END', 'END']
print(add_end())  # ['END', 'END', 'END']

"""
优化实现，用None这个不变对象实现
好处是可以避免在并发环境中的读写问题
"""

# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L


"""
可变参数函数定义
"""


def calc(*numbers):
    s = 0
    for i in numbers:
        s = s + i ** 2
    return s


# call
# print(calc([1, 2, 3]))
print(calc(1, 2, 3))
print(calc(*[1, 2, 3]))  # 当使用可变参数同样想传入一个list或tuple可以使用该形式

"""
关键字参数
关键字参数定义形式和可变参数类似，不同的是关键字参数将对应的参数转化为dict而不是list或tuple
"""


def student(name, age, **other):
    print('name:', name)
    print('age:', age)
    print('other', other)


student('wjq', 20, gender='Male', city='hebei')

"""
命名关键字参数
利用*进行分隔，*后的参数视为命名关键字参数
"""


def student1(name, age, *, city, job):
    print(name, age, city, job)


# 如果参数列表有一个可变参数，则后面命名关键字参数不需要加*
def student2(name, age, *department, city, job):
    print(name, age, department, city, job)


student1('wjq', 15, city='zjk', job='t')
'''
TypeError: student1() takes 2 positional arguments but 3 positional arguments 
(and 1 keyword-only argument) were given
'''
# student1('wjq', 15, 'zjk', job='t') 实现了关键字参数名称限制

'''
TypeError: student2() missing 1 required keyword-only argument: 'city'
可以看到从可变参数之后的参数都为命名关键字参数
'''
# student2('wjq', 15, 'zjk', job='t')


'''
练习
'''


def product(*args):
    if len(args) == 0:
        raise TypeError("no nums to calculate")
    mul = 1
    for i in args:
        if not isinstance(i, (int, float)):
            raise TypeError("par not format")
        mul = mul * i

    return mul


# 测试
# product()
# product('abc')
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
