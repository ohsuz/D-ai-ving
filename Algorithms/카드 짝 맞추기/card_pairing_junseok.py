import heapq
INF = 987654321
def solution(board, r, c):
    fr = [r,c]
    neighbors = getNeighbors(board)
    return recursive(fr, board, neighbors, 0)

def recursive(fr, board, neighbors, dist):
    distance = getDistance(fr, neighbors)
    print(distance)
    answer = INF
    isFinsish = True
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                num = board[i][j]
                board[i][j] = 0
                newdist = dist + distance[i][j]+1
                newneighbors = getNeighbors(board)
                newdistance = getDistance((i,j), newneighbors)
                pairIdx = findVal(num, board)
                newdist += newdistance[pairIdx[0]][pairIdx[1]] + 1
                board[pairIdx[0]][pairIdx[1]] = 0
                newneighbors = getNeighbors(board)
                result = recursive(pairIdx, board, newneighbors, newdist)
                answer = result if result < answer else answer 
                board[i][j], board[pairIdx[0]][pairIdx[1]]= num, num
                isFinsish = False
    if isFinsish:
        return dist  
    return answer

def findVal(val, board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == val:
                return (i,j)

def getDistance(fr, neighbors):
    distance = [[INF for __ in range(4)] for _ in range(4)]
    visited = [[False for __ in range(4)] for _ in range(4)]
    distance[fr[0]][fr[1]] = 0
    hq = [(0,fr)]
    while hq:
        _minDist, minIDX = heapq.heappop(hq)
        visited[minIDX[0]][minIDX[1]] = True
        for i, j  in neighbors[minIDX[0]][minIDX[1]]:
            if not visited[i][j]:
                distance[i][j] = distance[i][j] if distance[i][j] < distance[minIDX[0]][minIDX[1]] + 1 else (distance[minIDX[0]][minIDX[1]] + 1)
                heapq.heappush(hq,(distance[i][j],[i,j]))
    return distance

def getNeighbors(board):
    neighbors = [[[] for __ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            neighbors[i][j] = updateNeighbor(i,j,board)
    return neighbors

def updateNeighbor(i,j, board):
    delta = [(-1,0), (0, 1), (1,0), (0, -1)]
    neighbors = [(i+delta[k][0], j+delta[k][1]) for k in range(4) if i+delta[k][0] >= 0 and i + delta[k][0] < 4 and j+delta[k][1] >= 0 and j+delta[k][1] < 4]
    neighbors += [getCtrlNearest(i,j,delta[k],board) for k in range(4)]
    return neighbors

def getCtrlNearest(i,j, dir, board):
    while True:
        i += dir[0]
        j += dir[1]
        if not (i>=0 and i <4 and j >= 0 and j < 4):
            i -= dir[0]
            j -= dir[1]
            break
        elif not board[i][j] == 0:
            break
    return i, j

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))
print(solution([[3,0,0,2],[4,0,1,0],[0,1,0,0],[2,4,0,3]], 0, 1))
print(solution([[3,4,4,2],[5,0,1,0],[0,1,0,0],[2,5,0,3]], 0, 1))
print(solution([[3,4,4,2],[5,0,1,6],[0,1,6,0],[2,5,0,3]], 0, 1))