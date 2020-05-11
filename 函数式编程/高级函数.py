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
