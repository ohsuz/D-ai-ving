def DFS(i,numbers,total,target,string):
    global answer
    if i==len(numbers):
        if total==target:
            answer+=1
            # print(string)
        return
    else:
        DFS(i+1,numbers,total+numbers[i],target,string+'+'+str(numbers[i]))
        DFS(i+1,numbers,total-numbers[i],target,string+'-'+str(numbers[i]))
        
    


def solution(numbers, target):
    global answer
    answer = 0
    total=0
    string=''
    DFS(0,numbers,total,target,string)
    return answer