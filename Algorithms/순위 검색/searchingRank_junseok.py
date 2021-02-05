import bisect 
# bisect.insort(arr, 넣을언소) 정렬된 arrray에 넣어줌

def upper_bound(arr, score):
    return len(arr[bisect.bisect_right(arr,score-1):])

# (1 , 2, 3, 4, 5, 6)

# 10011(2) = 19
# language - fb - js - food
def solution(infos, querys):
    scores = [[] for _ in range(1<<5)]
    appdict= {
        "chicken": 0,
        "junior": 1,
        "backend": 2,
        "cpp" : 3,
        "java": 4,
    }
    for info in infos:
        lang, job, car, food, score = info.split()
        score = int(score)
        info_list = [lang, job, car, food]        
        result = 0
        for app in info_list:
            if app in appdict:
                result = result ^ (1 << appdict[app])
        scores[result].append(score)    
    for score in scores:
        score.sort()

    answer = []
    memoization = {}
    for query in querys:
        query = query.replace('and', '')
        lang, job, car, food, score = query.split()
        score = int(score)
        query_list = [food, car, job, lang]
        results = [0]
        if memoization.get(''.join(query_list)) == None:
            results = getNeedToCheck(appdict, results, query_list)
            memoization[''.join(query_list)] = results
        else:
            results = memoization[''.join(query_list)]
        passedAppl = 0            
        for result in results:
            if score == "_":
                passedAppl += len(scores[result])
            else:
                passedAppl += upper_bound(scores[result],score)
        answer.append(passedAppl)
    return answer

def getNeedToCheck(appdict, results, query_list):
        for appidx in range(len(query_list)):
            if query_list[appidx] == "-":
                results = doubleCheck(results, appidx)
                if appidx == 3:
                    appidx += 1          
                    results = doubleCheck(results, appidx)
            else:
                if query_list[appidx] in appdict:
                    for idx in range(len(results)):
                        results[idx] = results[idx] ^ (1 << appdict[query_list[appidx]])
        return results

def doubleCheck(results, appidx):
    newresults = [i for i in results]
    for resultidx in range(len(results)):
        results[resultidx] = results[resultidx] ^ (1 << appidx)
    newresults += results
    results = newresults
    return results

infos = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
querys = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
10110
# solution(infos, querys)
print(solution(infos, querys))
