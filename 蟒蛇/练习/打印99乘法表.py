j = 1
while j <= 9 :
    i = 1
    while i <= j :
        print(f'{i} * {j} = {i*j}',end = '\t')
        # \t为制表符  用来对齐。
        i += 1
    print()
    # 这里的print(),实际上（）里的内容为end = '\n'，\n表示为换行符。
    j += 1
