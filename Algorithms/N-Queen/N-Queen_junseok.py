    
def solution(n):
    col = [False for _ in range(n)]
    rightUp = [False for _ in range(2*n-1)]
    leftUp = [False for _ in range(2*n-1)]
    answer = 0
    def recur(q):
        nonlocal answer
        if q==n:
            answer += 1
            return
        for i in range(n):
            if col[i] == False and rightUp[i+q] == False and leftUp[n + q - i - 1] == False:                    
                col[i], rightUp[i+q], leftUp[n + q - i - 1] = True, True, True
                recur(q+1)                                
                col[i], rightUp[i+q], leftUp[n + q - i - 1] = False, False, False
    recur(0)    
    return answer

print(solution(4))