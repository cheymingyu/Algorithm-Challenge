# 시작시간: 2022.05.14 19:10
# 종료시간: 2022.05.14
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
    # queue에 원소를 두개씩 넣고 돌렸더니 93%에서 시간초과가 발생함
    for c in graph[1]:
        queue.append((1, c))
    while queue:
        parent, child = queue.popleft()
        root[child] = parent
        for c in graph[child]:
            if root[c] == -1:
                queue.append((child, c))

bfs()
s = ""
for r in root[2:]:
    s += (str(r) + '\n')
print(s)