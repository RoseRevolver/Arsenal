str1 = 'woshinidie'
for i in str1 :
    if i == 'd':
        continue
    print(i)
    #这里可以看出continue会退出循环不打印调教成立的语句，但是会正常打印后面的语句，仅仅不打印条件成立的语句。