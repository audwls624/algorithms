# 물건의 종류 , 무게, 길이 세가지가 각각 항목별로 주어졌을때
# duplicate 의 개수를 구하여라
# 예) A, B, A, C, A, B 이면 duplicate 는 A 2개 B 1개 여서 총 3개이다.

def solution(name,weight,length):
    arr = [(name[i],weight[i],length[i]) for i in range(len(name))]
    return len(arr)-len(list(set(arr)))