# 시작시간: 2022.04.29 21:10
# 종료시간: 2022.04.29 21:51
# 백준 7576번 https://www.acmicpc.net/problem/7576

"""
입력 형식
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
"""
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, input().split())
# 한 줄을 통째로 받고 N번 반복
box = [list(map(int, input().split())) for _ in range(N)]

def bfs(graph):
    queue = deque()
    # 처음에 익은 토마토가 있는 위치 큐에 삽입
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append((i, j))
    # print(queue)
    while(queue):
        x, y = queue.popleft()
        # 큐에서 pop하고, 그 주위 좌표 확인
        # 토마토 있으면 그 자리에 현재 좌표값+1 저장
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == -1:
                continue
            elif graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    
bfs(box)
result = 0
for row in box:
    for t in row:
        # 익지 않은 토마토가 있으면 -1 출력 후 프로그램 종료
        if t == 0:
            print(-1)
            exit(0)
    # 한 줄의 최대값 result에 저장
    result = max(result, max(row))
# result-1 출력
print(result-1)