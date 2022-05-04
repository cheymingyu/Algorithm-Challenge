# 시작시간: 2022.05.04 22:30
# 종료시간: 2022.05.04 23:14
# 백준 14502번 https://www.acmicpc.net/problem/14502

from collections import deque
import sys
import copy

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = 0
virus_list = []

# virus가 있는 위치를 찾아 virus_list를 만들었다.
for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            virus_list.append([i, j])

def bfs(new_lab):
    global answer
    queue = deque()
    # 미리 찾은 virus의 위치를 queue에 삽입
    for virus in virus_list:
        queue.append(virus)
    # virus와 인접한 모든 칸을 전염
    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            else:
                if new_lab[nx][ny] == 0:
                    new_lab[nx][ny] = 2
                    queue.append([nx, ny])
    safe = 0
    # 0이 있는 위치를 count
    for l in new_lab:
        for area in l:
            if area == 0: safe += 1
    answer = max(answer, safe)

def make_wall(cnt, startRow, startCol):
    # 벽을 3개 세웠으면 bfs함수 호출
    if cnt == 3:
        lab2 = copy.deepcopy(lab)
        bfs(lab2)
        return
    else:
        # make_wall을 호출할 때, cnt만 넘겼더니 시간초과가 났다.
        # [1,2,3], [3,1,2] 이런 식으로 벽의 위치는 동일한데
        # bfs를 계속 호출해서, 이미 검사한 벽을 다시 검사하지 않도록
        # 범위를 조절했다.
        for i in range(startRow, N):
            for j in range(startCol, M):
                if lab[i][j] == 0:
                    lab[i][j] = 1
                    make_wall(cnt+1, i, j+1)
                    lab[i][j] = 0
            startCol = 0

answer = 0
make_wall(0, 0, 0)
print(answer)