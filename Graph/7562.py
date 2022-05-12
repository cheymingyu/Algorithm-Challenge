# 시작시간: 2022.05.12 21:46
# 종료시간: 2022.05.12 22:06
# 백준 7562번 https://www.acmicpc.net/proablem/7562


import sys
from collections import deque

dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

def bfs():
    global l, cx, cy, gx, gy
    queue = deque()
    count = 0
    visited = [[False] * l for _ in range(l)]
    queue.append((cx, cy, count))
    visited[cx][cy] = True
    while queue:
        x, y, cnt = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == False:
                if (nx, ny) == (gx, gy):
                    return cnt + 1
                else:
                    queue.append((nx, ny, cnt + 1))
                    visited[nx][ny] = True

N = int(sys.stdin.readline())

for _ in range(N):
    l = int(sys.stdin.readline())
    # current
    cx, cy = map(int, sys.stdin.readline().split())
    # goal
    gx, gy = map(int, sys.stdin.readline().split())
    if (cx, cy) == (gx, gy): print(0)
    else: print(bfs())
    
    