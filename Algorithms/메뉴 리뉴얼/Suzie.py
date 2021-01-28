from itertools import combinations

def solution(orders, course):
    answer = []
    menu, comb, result = {}, {}, {}
    
    for i in list(set([len(order) for order in orders])):
        for c in course:
            if i >= c:
                comb[(i, c)] = list(combinations(list(range(i)), c))
    
    for order in orders:
        for c in course:
            if len(order) >= c:
                for cb in comb[(len(order), c)]:
                    new = ''.join(sorted([order[i] for i in cb]))
                    menu[new] = menu.get(new, 0) + 1
                    if menu[new] > result.get(len(new), 0):
                        result[len(new)] = menu[new]
                        
    for m in menu:
        if menu[m] >= 2 and menu[m] == result[len(m)]:
            answer.append(m)
    
    return sorted(answer)
    
'''
아직 효율성 잘 몰라서 신경 못 썼습니다 ㅠㅠ,,
테스트 1 〉	통과 (0.26ms, 10.3MB)
테스트 2 〉	통과 (0.14ms, 10.2MB)
테스트 3 〉	통과 (0.27ms, 10.3MB)
테스트 4 〉	통과 (0.28ms, 10.1MB)
테스트 5 〉	통과 (0.27ms, 10.2MB)
테스트 6 〉	통과 (0.75ms, 10.2MB)
테스트 7 〉	통과 (0.81ms, 10.2MB)
테스트 8 〉	통과 (6.22ms, 10.4MB)
테스트 9 〉	통과 (4.05ms, 10.4MB)
테스트 10 〉	통과 (4.68ms, 10.6MB)
테스트 11 〉	통과 (2.52ms, 10.5MB)
테스트 12 〉	통과 (3.16ms, 10.5MB)
테스트 13 〉	통과 (4.33ms, 10.5MB)
테스트 14 〉	통과 (3.12ms, 10.5MB)
테스트 15 〉	통과 (4.36ms, 10.6MB)
테스트 16 〉	통과 (0.89ms, 10.2MB)
테스트 17 〉	통과 (0.84ms, 10.3MB)
테스트 18 〉	통과 (0.35ms, 10.3MB)
테스트 19 〉	통과 (0.05ms, 10.3MB)
테스트 20 〉	통과 (1.25ms, 10.2MB)
'''
