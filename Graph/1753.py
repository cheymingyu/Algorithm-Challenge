# 시작시간: 2022.05.06 22:47
# 종료시간: 2022.05.06 23:59
# 백준 1753번 https://www.acmicpc.net/problem/1753

import heapq
import sys

INF = int(1e9)

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

distance = [INF] * (V+1)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while(queue):
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(queue, (cost, next[0]))
            
dijkstra(K)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])