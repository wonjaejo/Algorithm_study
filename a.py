import sys

input = sys.stdin.readline

n,l,r = map(int,input().split())
Map = [list(map(int,input().split())) for _ in range(n)]

def solve():
    result = 0
    dx = [-1,1,0,0]; dy = [0,0,-1,1];
    while(1):
        result += 1
        tmp = Map
        visited =[[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    visited_2 = [[i,j]]
                    visited[i][j] = True
                    queue = [[i,j]]
                    cnt = 1
                    num_p = Map[i][j]
                    while(queue):
                        cur_x,cur_y = queue.pop()
                        for k in range(4):
                            nx = cur_x + dx[k]; ny = cur_y + dy[k];
                            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                                if l<=abs(Map[nx][ny]-Map[cur_x][cur_y])<=r:
                                    queue.append([nx,ny]); visited[nx][ny] = True; visited_2.append([i,j]);
                                    cnt += 1; num_p += Map[nx][ny];
                    num_people = num_p//cnt
                    print(visited_2)
                    for x,y in visited_2:
                        Map[x][y] = num_people
        if Map == tmp:
            break
    return result
                                
              
print(solve())
