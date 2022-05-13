# 시작시간: 2022.05.13 19:34
# 종료시간: 2022.05.13 20:31
# 백준 2206번 https://www.acmicpc.net/proablem/2206
# 벽 부수고 이동하기

import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    global N, M, mapp, visited
    queue = deque()
    queue.append((0, 0, 0))
    while queue:
        x, y, c = queue.popleft()
        if (x, y) == (N-1, M-1):
            return visited[x][y][c]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if mapp[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    queue.append((nx, ny, c))
                    visited[nx][ny][c] = visited[x][y][c] + 1
                elif mapp[nx][ny] == 1 and c == 0:
                    queue.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][c] + 1
    return -1

N, M = map(int, sys.stdin.readline().split())
mapp = []
for _ in range(N):
    mapp.append(list(map(int, sys.stdin.readline().strip())))
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

print(bfs())