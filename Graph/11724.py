# 시작시간: 2022.05.01 22:40
# 종료시간: 2022.05.01 23:12
# 백준 11724번 https://www.acmicpc.net/problem/11724

from collections import deque
import sys
# 시간초과나서 input()대신 sys.stdin.readline()사용

# bfs로 연결된 노드 검사
def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while(queue):
        a = queue.popleft()
        for i in graph[a]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

# 방향이 없는 그래프이므로 양쪽에 추가
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)