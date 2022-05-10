# 시작시간: 2022.05.10 12:50
# 종료시간: 2022.05.10 13:10
# 백준 10026번 https://www.acmicpc.net/proablem/10026

from collections import deque
from itertools import count
import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(a, b, color):
    global pic, N, visited
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if pic[nx][ny] == color and visited[nx][ny] == False:
                queue.append((nx, ny))
                visited[nx][ny] = True

N = int(sys.stdin.readline())
pic = [[] for _ in range(N)]
for i in range(N):
    line = sys.stdin.readline()
    for c in line[:-1]:
        pic[i].append(c)
visited = [[False] * N for _ in range(N)]

normal = 0
weak = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i, j, pic[i][j])
            normal += 1
            
RBpic = []
for p in pic:
    RBpic.append(list(map(lambda x: x.replace("G","R"), p)))
pic = RBpic
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i, j, pic[i][j])
            weak += 1
print(normal)
print(weak)