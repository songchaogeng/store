from numpy import *
temp=1
list=[]
while temp<=8:
    print("请输入您的第",temp,"课成绩:")
    score=input()
    score=int(score)
    list.append(score)
    temp=temp+1

sum_score=sum(list)
max_score=max(list)
min_score=min(list)
avg_score=mean(list)
print("您的总成绩为 %s" % sum_score)
print("您的最大成绩为 %s" % max_score)
print("您的最小成绩为 %s" % min_score)
print("您的平均成绩为 %s" % avg_score)
