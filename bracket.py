#해당 괄호를 완성하려면 필요한 괄호의 개수 구하기
letter=')))(((()(())(()(()()((((())))'
stack=[]
n=0
for i in letter:
    if i=='(':
        stack.append(i)
    else:
        if len(stack)==0:
            n+=1
        else:
            stack.pop()
print(n+len(stack))
