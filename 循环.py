#!/usr/bin/env python3
names = ['Bob', 'Mike', 'wjq', 'weg']
for name in names:
    print(name)

n = 1
sum100 = 0
while n <= 100:
    sum100 = sum100 + n
    n = n + 1
print(sum100)

L = ['Bart', 'Lisa', 'Adam']
for name1 in L:
    print('hello,', name1)

L_len = len(L)
i = 0
while i < L_len:
    print('hello,', L[i])
    i = i + 1