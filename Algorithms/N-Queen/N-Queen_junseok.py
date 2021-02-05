    
def solution(n):
    chess = [[0 for __ in range(n)] for _ in range(n)]
    answer = 0
    def setChess(i,j):
        for 
    def recur(q):
        nonlocal answer
        if q==4:
            answer += 1
            return
        for i in range(n):
            for j in range(n):
                if chess[i][j] == 0:                    
                    recur(q+1)
                
    
    
    return answer

print(solution(4))