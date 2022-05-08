# 시작시간: 2022.05.08 21:10
# 종료시간: 2022.05.08 21:51
# 백준 2468번 https://www.acmicpc.net/proablem/2468

from collections import deque
from itertools import count
import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(a, b, h):
    global space, N, visit
    queue = deque()
    queue.append((a, b))
    visit[a][b] = True
    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if space[nx][ny] > h and visit[nx][ny] == False:
                queue.append((nx, ny))
                visit[nx][ny] = True

N = int(sys.stdin.readline())
space = [list(map(int, input().split())) for _ in range(N)]
maxh = 0
for s in space:
    maxh = max(maxh, max(s))

count_max = 0
for h in range(maxh):
    visit = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if space[i][j] > h and visit[i][j] == False:
                bfs(i, j, h)
                cnt += 1
    count_max = max(count_max, cnt)


print(count_max)