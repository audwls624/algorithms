from collections import Counter

weights = [2,2,2,2,3,3,5,6]
counts = Counter(weights)
print([{key:value} for key, value in dict(counts).items()])