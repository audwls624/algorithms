# LZW 압축은 다음 과정을 거친다.

# 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
# 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
# w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
# 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
# 단계 2로 돌아간다.
# 압축 알고리즘이 영문 대문자만 처리한다고 할 때, 사전은 다음과 같이 초기화된다. 사전의 색인 번호는 정수값으로 주어지며, 1부터 시작한다고 하자.

def solution(msg):
    alpha_dic = dict(A=1,B=2,C=3,D=4,E=5,F=6,G=7,H=8,I=9,J=10,K=11,L=12,M=13,N=14,O=15,P=16,Q=17,R=18,S=19,T=20,U=21,V=22,W=23,X=24,Y=25,Z=26)
    max_num = max(alpha_dic.values())
    n = 1
    answer = []
    while msg:
        if alpha_dic.get(msg[:n]):
            if len(msg) == n:
                answer.append(alpha_dic.get(msg))
                break

            n += 1
            continue
        
        answer.append(alpha_dic.get(msg[:n-1]))
        alpha_dic[f'{msg[:n]}'] = max_num + 1
        max_num += 1
        msg = msg[n-1:]
        n = 1
    return answer

print(solution('TOBEORNOTTOBEORTOBEORNOT'))