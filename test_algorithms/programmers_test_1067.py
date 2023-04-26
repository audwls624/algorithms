import numpy as np

def solution(arr, k, t):
    n = len(arr)
    dp = np.zeros((n+1, k+1), dtype=int)
    dp[0][0] = 1
    
    for i in range(1, n+1):
        for j in range(k+1):
            if arr[i-1] <= t:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1] if j > 0 else dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][k]