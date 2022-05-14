# 시작시간: 2022.05.14 19:10
# 종료시간: 2022.05.14 22:11
# 백준 11725번 https://www.acmicpc.net/proablem/11725
# 트리의 부모 찾기

import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
root = list(-1 for _ in range(N+1))

def bfs():
    global graph, N, root
    queue = deque()
    # queue의 원소개수를 1개로 줄였더니 잘 돌아감.
    queue.append(1)
    while queue:
        now = queue.popleft()
        for c in graph[now]:
            if root[c] == -1:
                root[c] = now
                queue.append(c)

bfs()
s = ""

for r in root[2:]:
    s += (str(r) + '\n')
print(s)