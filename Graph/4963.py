# 시작시간: 2022.05.07 20:44
# 종료시간: 2022.05.07 21:05
# 백준 4963번 https://www.acmicpc.net/problem/4963

from collections import deque
import sys

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

def bfs(a, b):
    global mapp, w, h
    mapp[a][b] = 0
    queue = deque()
    queue.append((a, b))
    while(queue):
        x, y = queue.popleft()
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if mapp[nx][ny] == 1:
                queue.append((nx, ny))
                mapp[nx][ny] = 0

while(True):
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0: break
    mapp = [[] for _ in range(h)]
    for i in range(h):
        line = map(int, sys.stdin.readline().split())
        for l in line:
            mapp[i].append(l)
    cnt = 0
    for i in range(h):
        for j in range(w):
            if mapp[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
