n=0
arr = [1,2,3,9,10,12]


while min(arr) <= 7:
    arr.sort(reverse=True)
    minimum = arr.pop()
    minumum_2 = arr.pop()
    arr.append(minimum + (minumum_2 *2))
    n+=1

print(arr)

print(n)
        
