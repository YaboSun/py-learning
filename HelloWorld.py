#!/usr/bin/env python3
name = input("please input your name:")
print('hello', name)
print("hello world")

print('hello python')
print('''line1
line2
line3''')

a = 'ABC'
b = b'ABC'

print(a, b)

print('中文测试')

print('Hello, %s' % 'world')

print('hi %s,your bill is ￥%d.' % ('wjq', 10000))

print('%02d-%02d' % (3, 1))
s1 = 72
s2 = 85
r = (s2 - s1)/s1 * 100
print('{0}成绩提升了{1:.1f}%'.format('小明', r))
print('%s成绩提升了%.1f%%' % ('小明', r))
