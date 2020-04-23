"""
生成[1*1,2*2,...5*5]的列表
"""

l = []
for i in range(1, 6):
    l.append(i * i)
print(l)

"""
利用列表生成式实现
"""
print([x * x for x in range(1, 6)])

# 生成全排列
print([m + n for m in 'ABC' for n in 'EFG'])
