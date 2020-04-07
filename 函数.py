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
