# 시작시간: 2022.05.15 23:27
# 종료시간: 2022.05.15 23:39
# 백준 11726번 https://www.acmicpc.net/proablem/11726
# 2×n 타일링

n = int(input())

dp = [0, 1, 2]
for i in range(3, 1001):
    dp.append(dp[i-2] + dp[i-1])
print(dp[n] % 10007)