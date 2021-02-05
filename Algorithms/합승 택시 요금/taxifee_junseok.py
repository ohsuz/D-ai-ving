def solution(n, s, a, b, fares):
    answer = 1e10
    graph = [[1e10 if i != j else 0 for i in range(n+1)] for j in range(n+1)]    
    for fare in fares:
        fr, to, fee = fare[0], fare[1], fare[2]
        graph[fr][to] = fee
        graph[to][fr] = fee
    for mid in range(1, n+1):
        for start in range(1, n+1):
            for end in range(1, n+1):
                if graph[start][end] > graph[start][mid] + graph[mid][end]:
                    graph[start][end] = graph[start][mid] + graph[mid][end]   
    for mid in range(1, n+1):
        answer = answer if graph[s][mid]+graph[mid][a]+graph[mid][b] > answer else graph[s][mid]+graph[mid][a]+graph[mid][b]    
    return answer

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7,3,4,1,	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))