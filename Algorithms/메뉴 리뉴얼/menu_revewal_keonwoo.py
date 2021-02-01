from itertools import combinations

def solution(orders, course):
    answer = []
    for i in course:
        dic = dict()
        for j in orders:
            for s in combinations(sorted(j),i):
                dic[''.join(s)] = dic.get(''.join(s),0)+1
        if not dic:
            continue
        max_num = max((dic.values()))
        for tup in dic.items():   #tup=('AB',1),('AC',4)...
            if tup[1]==max_num and max_num>=2:
                answer.append(tup[0])
    return sorted(answer)