# 시작시간: 2022.04.28 21:50
# 종료시간: 2022.04.28 22:26
# 백준 1012번 https://www.acmicpc.net/problem/1012

from collections import deque

def bfs(graph, a, b, m, n):
    # 탐색에 사용
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    
    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            # index 검사
            if new_x < 0 or new_x >=n or new_y < 0 or new_y >= m:
                continue
            if ground[new_x][new_y] == 1:
                # 값이 1이면 큐에 집어넣고 0으로 바꿈
                queue.append((new_x, new_y))
                ground[new_x][new_y] = 0
    
    

T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())
    # M * N 배열 생성
    ground = [[0] * M for _ in range(N)]
    count = 0
    
    for j in range(K):
        Y, X = map(int, input().split())
        ground[X][Y] = 1
        
    for x in range(N):
        for y in range(M):
            if ground[x][y] == 1:
                bfs(ground, x, y, M, N)
                # bfs 하고 나면 현재 x, y 주변을 모두 탐색했으므로 count += 1
                count += 1
    print(count)
    
    
