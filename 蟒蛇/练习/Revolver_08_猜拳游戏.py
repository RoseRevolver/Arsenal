'''
1.出拳（玩家手动输入）
2.判断胜负（随机出拳）
'''
player=int(input('请出拳,0--剪刀 1--石头 2--布：'))
computer = 0
if(player == 0) and (computer == 2) or (player == 1) and (computer == 0) or (player == 2) and (computer == 1):
    print('Revolver果然名不虚传。')
elif(player == 0) and (computer == 0) or (player == 1) and (computer == 1) or (player == 2) and (computer == 2):
    print('不要跑，决战到天亮！')
elif(player == 0) and (computer == 1) or (player == 1) and (computer == 2) or (player == 2) and (computer == 0):
    print('我赌你的枪里没有子弹。')
else:
    print('请输入合法数字。')
print('游戏结束')
