def solution(sizes):
    big = []
    small = []
    for size in sizes:
        if size[0] >= size[1]:
            big.append(size[0])
            small.append(size[1])
        else:
            big.append(size[1])
            small.append(size[0])
    return max(big) * max(small)
    # return max(max(x) for x in sizes) * max(min(x) for x in sizes)