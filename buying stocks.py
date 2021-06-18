# 문제 : 주어진 금액 amount 를 사용하여 주식 종목을 원하는 비율만큼 매수하고자 한다.
# 원하는 비율을 최대한 지키면서 주어진 금액을 최대한 사용하여 각 종목당 매수할수 있는 주식수를 구하는 알고리즘을 구하세요. 
# 단 최적의 알고리즘이 아니더라도 빠르게 결과를 찾는 sub-optimal을 찾는 알고리즘 구현하는것도 괜찮습니다. ( 알고리즘에 대한 간단한 설명 포함 필수 )
# 아래의 예시를 참고하여 일반적인 해법을 찾는 알고리즘을 구하세요

# 예시
# Input : 100만원
# 매수 조건 :  A주식 36% (11.5만원/1주), B주식 50% (5.1만원/1주), C주식 14% (2만원/1주)
# 단 각각의 주식별 자산 비율의 합은 항상 100% 이다. 즉 36% + 50% + 14% = 100% 
# Output : 
# A주식 : 3주 
# B주식 : 10주 
# C주식 : 7주 
# 남는 돈 : 5천원 

#-----------------------------풀이1
# ----- 세팅
budget              = 1000000
names               = ['A', 'B', 'C']
prices              = [115000, 51000, 20000]
optimal_ratio       = [36, 50, 14]
optimal_balances    = [budget * optimal_ratio[i] / 100 for i in range(len(prices))] # 이상적인 매수 결과

print('budget: ', budget)
print('target ratio: ', optimal_ratio)
print('target balance: ', optimal_balances)
print('prices: ', prices)
print('  ------------')

balance             = budget # 남아있는 예수금
wallet              = [0, 0, 0] #매수한 주식 수

# 살 수 있는 게 하나라도 있으면 계속 진행
while any([balance >= price for price in prices]):

    action = None
    min_diff = 9999999999

    # 매수할 종목 선택(optimal과의 오차가 제일 작은)
    for i in range(len(prices)):

        if balance < prices[i]: 
            continue  # 잔고 부족 : 스킵

        # i 번째 종목 살 경우의 optimal balance 와의 오차 계산
        diff_sum = 0
        for j in range(len(prices)):
            if i == j:
                diff = optimal_balances[j] - prices[j] * (wallet[j] + 1)  # i 번째 종목 1주 매수 가정
            else:
                diff = optimal_balances[j] - prices[j] * wallet[j]
            diff_sum += abs(diff)

        if diff_sum < min_diff:
            min_diff = diff_sum
            action = i

    # 종목 매수
    balance -= prices[action]
    wallet[action] += 1

print('남은 돈:', balance)
for i in range(len(prices)):
    print('종목명:',names[i],', 종목수: ',wallet[i])


#------이상적인 매수 금액 이하로 최대한 매수
limit_buy    = [(optimal_balances[i] // prices[i]) * prices[i] for i in range(len(prices))] #최대 매수 금액
wallet       = [(optimal_balances[i] // prices[i]) for i in range(len(prices))] # 종목 수
budget_left  = budget-sum(limit_buy) # 최대 매수 후 남은 금액
min_diff     = budget_left

#---------------------------------풀이2
#최대 매수 후 남은 금액으로 매수
while any([budget_left >= price for price in prices]):
    
    for i in range(len(prices)):
        # 이상 비율에 해당되는 종목 제외
        if optimal_balances[i] - limit_buy[i] == 0:
            continue

        diff = abs(optimal_balances[i] - (limit_buy[i]+prices[i])) # 종목 매수시 이상 매수 금액과의 오차

        if diff < min_diff and (budget_left-prices[i])>0: # 종목 매수시 이상 매수 금액과의 오차가 제일 적어지는 종목 매수
            diff = min_diff
            action = i

    wallet[action]+=1
    budget_left -= prices[action]

print('남은 돈: ', budget_left)
for i in range(len(prices)):
    print('종목: ',names[i],'종목 수: ',wallet[i])