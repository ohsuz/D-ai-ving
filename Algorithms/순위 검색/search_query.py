#효율성 똥망
def solution(info, query):
    answer = []
    table=[]
    for i in info:
        table.append(i.split())
    for q in query:
        splited=q.split()
        language,job,career,food,score=splited[0],splited[2],splited[4],splited[6],splited[7]
        cnt=0
        for tup in table:
            if (language=='-' or language==tup[0]) and (job=='-' or job==tup[1]) and (career=='-' or career==tup[2]) and (food=='-' or food==tup[3]) and (score=='-' or int(score)<=int(tup[4])):
                cnt+=1
        answer.append(cnt)
                 
    return answer