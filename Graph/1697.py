# 시작시간: 2022.04.30 22:04
# 종료시간: 2022.04.30 22:37
# 백준 1697번 https://www.acmicpc.net/problem/1697

from collections import deque

N, K = map(int, input().split())

queue = deque()
count = 0
queue.append([N, count])
# 한번 방문한 좌표는 다시 큐에 넣지 않기 위해 visit 배열 생성
visit = [0]*100001
# 초기 위치 visit 1로 
visit[N] = 1

while(queue):
    n, c = queue.popleft()
    # queue에서 꺼낸 위치가 K라면 break
    if n == K:
        count = c
        break
    # n-1, n+1, 2*n을 queue에 저장
    if n-1 >= 0 and n-1 <= 100000 and visit[n-1] == 0:
        queue.append([n-1, c+1])
        visit[n-1] = 1
    if n+1 >= 0 and n+1 <= 100000 and visit[n+1] == 0:
        queue.append([n+1, c+1])
        visit[n+1] = 1
    if 2*n >= 0 and 2*n <= 100000 and visit[2*n] == 0:
        queue.append([2*n, c+1])
        visit[2*n] = 1
    
print(count)