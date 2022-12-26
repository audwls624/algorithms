def permutation(arr, start):
    if start == len(arr)-1:
        print(arr)
        return

    for idx in range(start, len(arr)):
        arr[start], arr[idx] = arr[idx], arr[start]
        permutation(arr, start+1)
        arr[start], arr[idx] = arr[idx], arr[start]

# example
arr= [1, 2, 3]
permutation(arr, 0)
