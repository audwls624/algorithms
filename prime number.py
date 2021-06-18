a=[5,10,1,1,20,1]
result=[]
while len(a)>0:
    num = 0
    for i in range(len(a)):
        if max(a[:i+1])==a[0]:
            num+=1
            if i+1==len(a):
                del a[:i+1]
        else:
            del a[:i]
            break
    result.append(num)
print(result)