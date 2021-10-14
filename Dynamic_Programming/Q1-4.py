#https://algo-method.com/tasks/305

def main():
    N = int(input())

    dp = [0] * 35

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4,N+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    
    print(dp[N])

if __name__=="__main__":
    main()