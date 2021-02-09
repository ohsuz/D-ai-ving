def check(x):
    for j in range(x):
        if row[x] == row[j] or abs(row[x] - row[j]) == x - j:
            return False
    return True
def DFS(x,n):
    global result
    
    if x == n:
        # print(row)
        result += 1
        return
    
    for i in range(n):
        row[x] = i
        if check(x):
            DFS(x + 1,n)
    
def solution(n):
    global row,result
    row = [0] * n
    result = 0
    DFS(0,n)
    print(result)