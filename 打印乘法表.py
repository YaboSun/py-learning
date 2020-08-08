for i in range(1, 10):
    for j in range(1, i + 1):
        if i == j:
            print("%d*%d=%d" % (j, i, i * j), end="\n")  # i == j 则做换行处理
        else:
            print("%d*%d=%d" % (j, i, i * j), end="\t")  # 其他的作\t间隔
