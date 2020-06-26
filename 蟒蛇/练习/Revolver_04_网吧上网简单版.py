# 分析：年龄大于等于18，输出：已经成年可以上网 —— 准备年龄的数据 和 18 作对比
age=int(input('请输入您的年龄: '))
if age >= 18:
    print(f'亲爱的Revolver{age}，您已经成年可以上网')
    print(type(age))
else:
    print(f'孩子你的年龄为{age}你还未成年，回家写5年高考3年模拟吧。')
print('祝您愉快。')