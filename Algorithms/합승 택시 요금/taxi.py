import math
def solution(n, s, a, b, fares):
    answer = math.inf
    dis=[[math.inf]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        dis[i][i]=0
    for x,y,z in fares:
        dis[x][y] = z
        dis[y][x] = z
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dis[i][j] > dis[i][k] + dis[k][j]:         #dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])
                    dis[i][j] = dis[i][k] + dis[k][j]
    for i in range(1, n+1):
        answer = min(answer, dis[s][i] + dis[i][a] + dis[i][b])
    return answer