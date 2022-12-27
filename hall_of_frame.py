def solution(k, score):
    answer = []
    state = []
    for i in range(len(score)):
        if i < k:
            state.append(score[i])
            answer.append(min(state))
        else:
            if min(state) >= score[i]:
                answer.append(min(state))
            else:
                state.sort(reverse=True)
                state.pop()
                state.append(score[i])
                answer.append(min(state))

solution(3, [10, 100, 20, 150, 1, 100, 200])