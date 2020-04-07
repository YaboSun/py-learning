# coding:utf-8
# -*-coding:utf-8-*-
"""
Author: roguesir
Date: 2017/8/30
GitHub: https://roguesir.github.com
Blog: http://blog.csdn.net/roguesir
"""

import numpy as np

from matplotlib.font_manager import *
import matplotlib.pyplot as plt

myfont = FontProperties(fname='/usr/share/fonts/truetype/arphic-gbsn00lp/gbsn00lp.ttf')
print(matplotlib.matplotlib_fname())
x1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58]
y1 = [69.5, 69.2, 68.5, 67.3, 68.1, 62.3, 63.7, 65.5, 64.3, 63.5, 62.1, 66.5, 61.5, 60.5, 59.5, 59.7, 59.1, 58.5, 57.5, 55]
x2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58]
y2 = [72.1, 70.8, 71.2, 69.2, 68.2, 67.7, 66.2, 70.2, 71.2, 72.2, 73.2, 73.6, 74.2, 73.8, 73.2, 74.2, 72.8, 70.2, 73.2, 70.9]
# x3 = [30, 50, 70, 90, 105, 114, 128, 137, 147, 159, 170, 180, 190, 200, 210, 230, 243, 259, 284, 297, 311]
# y3 = [48, 48, 48, 48, 66, 173, 351, 472, 586, 712, 804, 899, 994, 1094, 1198, 1360, 1458, 1578, 1734, 1797, 1892]
x = np.arange(1, 60)
l1 = plt.plot(x1, y1, 'r--', label='Wang')
l2 = plt.plot(x2, y2, 'g--', label='Sun')
# l3 = plt.plot(x3, y3, 'b--', label='type3')
plt.plot(x1, y1, 'ro-', x2, y2, 'g^-')
plt.title('王嘉琦和孙亚博体重变化对照', fontproperties=myfont)
plt.xlabel('date')
plt.ylabel('weight/kg')
plt.legend()
plt.show()
