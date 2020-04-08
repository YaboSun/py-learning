"""
作业，返回一个list中的最大值和最小值
方便起见，默认输入符合要求
"""


def findMinAndMax(L):
    if not L:
        # if len(L) == 0: # 等效，但是为啥呢？
        return None, None
    lMin = L[0]
    lMax = L[0]

    for i in L:
        lMin = min(i, lMin)
        lMax = max(i, lMax)
    return lMin, lMax


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
