# 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

import math
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
day_cost = [math.ceil((100-progresses[i]) / speeds[i]) for i in range(len(speeds))]
arr=[]
while len(day_cost)!=0:
    n=0
    des=day_cost[0]
    for i in range(len(day_cost)):
        day_cost[i]-=des
    for i in day_cost:
        if i<=0:
            n+=1
        else:
            break
    for j in range(n):
        day_cost.pop(0)
    arr.append(n)
print(arr)