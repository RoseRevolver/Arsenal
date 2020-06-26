'''
需求：
判断是否超载：
判断有没有钱：
判断钱够不够：
判断车上有没有座位：
决定站着或者坐着。
'''
people = 20
seat = 10
while people > 0:
    money=int(input('请输入你的钱数：'))
    if money < 2:
        print(f'您的钱数是：{money}元，爬。')
    else:
        print(f'您的钱数是：{money}元,尊敬的土豪，请上车。')
        if seat > 0:
            print(f'剩余座位数为：{seat}个,土豪请上座')
            people = people - 1
            print(f'等待人数为：{people}人')
            seat = seat - 1
        else:
            print(f'剩余座位数为：{seat}个，站在角落破口大骂')
            people = people - 1
            print(f'等待人数为：{people}人')
print('人满了，小葵花公交车发车啦。')