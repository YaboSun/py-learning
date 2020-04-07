#!/usr/bin/env python3
age = 18
if age >= 20:
    print('your age is', age)
    print('adult')

else:
    print('your age is', age)
    print('teenager')
birth = input('birth:')
b = int(birth)
if b < 2000:
    print('00前')
else:
    print('00后')

# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数
height = 1.78
weight =70.5
bmi = weight / (height * height)
print(bmi)
if bmi <= 18.5:
    print('不是人，太轻了')
elif 18.5 < bmi <= 25:
    print('牛批，是个正常人')
elif 25 < bmi <= 28:
    print('有点重了')
elif 28 < bmi <= 32:
    print('兄弟，这就有点胖了')
elif bmi > 32:
    print('这太肥了')