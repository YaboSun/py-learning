g = (x * x for x in range(1, 10))
print(g)
print(next(g))


# 斐波那契实现
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


# 从以上可以看出对应的fib有规律，可以利用generator实现
# 最简单实现方式就是将以上代码中的print(b)直接换成yield b
def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

def odd():
    print('step1')
    yield 1
    print('step2')
    yield 3
    print('step3')
    yield 5

o = odd()
print(next(o))
print(next(o))
print(next(o))




