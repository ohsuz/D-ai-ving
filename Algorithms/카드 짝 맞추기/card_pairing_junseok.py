INF = 987654321
def solution(board, r, c):
    answer = 0
    fr = [r,c]

    return answer

def getShortest(board, fr):
    dist = [[INF for i in range(4)] for j in range(4)]

    deltai = [-1, 0, 1, 0]
    deltaj = [-0, 1, 0, -1]
    for i in range(4):
        newdisti = fr[0] + deltai[i]
        newdistj = fr[1] + deltaj[i]
        if newdisti >= 0 and newdisti < 4 and newdistj >= 0 and newdistj < 4:
            dist[newdisti][newdistj] = 1

    deltai = [-1, -1, 1, 1]
    deltaj = [-1, 1, 1, -1]
    for i in range(4):
        newdisti = fr[0] + deltai[i]
        newdistj = fr[1] + deltaj[i]
        if newdisti >= 0 and newdisti < 4 and newdistj >= 0 and newdistj < 4:
            dist[newdisti][newdistj] = 2


    
# 어느 카드까지의 최소거리, 또는 전체 최소거리

# 어느 순번으로?

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))
