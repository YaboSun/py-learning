names = {'Apple': 50, 'Google': 60, 'Microsoft': 70}
print(names['Apple'])

names['Nokia'] = 80
print(names['Nokia'])

print(names.get('Google'))
print(names.get('HW'))
print(names.get('wjq', "Nothing"))

print(names.pop('Apple'))
print(names)

names['Google'] = 70
print(names)

dictNames = {'Apple': 50, 'Google': 60, 'Microsoft': 70, 'Google': 90}
print(dictNames)
dictNames.__delitem__('Apple')  # 这个和pop有什么区别，魔术方法？
print(dictNames)

s1 = {1, 1, 2, 2, 3}
print(s1)  # 不会有重复
s1.add(7)
print(s1)
s1.remove(1)
print(s1)

s2 = {2, 3, 4, 8}
print(s1 & s2)
print(s1 | s2)

# s1.add([1, 2, 3, 5, 10])
s1.add((1, 2, 3))  # 不会报错，因为tuple不可变
print(s1)
s1.add((1, 2, 8, [2, 3, 5]))  # 报错，虽然tuple可变，但是其中元素list是可变的
