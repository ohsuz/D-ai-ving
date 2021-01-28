from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    menuDict = defaultdict(lambda: 0)
    for order in orders:
        for courseLen in course:
            for m in combinations(order, courseLen):                               
                menuDict[''.join(sorted(list(m)))] += 1

    answer = defaultdict(lambda: [])
    for courseLen in course:
        maxNum = 0
        for menu in menuDict:
            if len(menu) == courseLen and menuDict[menu] > 1 and menuDict[menu] >= maxNum:
                if menuDict[menu] > maxNum:
                    answer[courseLen] = []
                    maxNum = menuDict[menu]
                answer[courseLen].append(menu)
                
    result = []
    for _, vs in answer.items():
        for v in vs:
            result.append(v)
    return sorted(result)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))