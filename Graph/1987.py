# 시작시간: 2022.05.11 23:20
# 종료시간: 2022.05.11 23:42
# 백준 1987번 https://www.acmicpc.net/proablem/1987


import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]



R, C = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(R):
    matrix.append(sys.stdin.readline().rstrip())

queue = set()
queue.add((0, 0, matrix[0][0]))
cnt = 0
def bfs(q):
    global cnt
    while(q):
        x, y, sentence = q.pop()
        cnt = max(cnt, len(sentence))
        if cnt==26:
            return
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if matrix[nx][ny] not in sentence:
                    q.add((nx, ny, sentence + matrix[nx][ny]))
bfs(queue)

print(cnt)