from itertools import combinations

def solution(orders, course):
    answer = []
    menu, comb, max_order = {}, {}, {}
    
    # 1. orders에서 가능한 코스별 인덱스 조합들을 미리 comb 딕셔너리에 저장
    for i in set([len(order) for order in orders]):
        for c in course:
            if i >= c:
                comb[(i, c)] = list(combinations(list(range(i)), c))
    
    # 2-1. 각 주문별로 만들 수 있는 코스 조합들을 menu 딕셔너리에 저장하고 count
    # 2-2. count한 수가 동일 단품메뉴 개수를 가진 코스 中 최대이면 max_order 딕셔너리에 업데이트
    for order in orders:
        for c in course:
            if len(order) >= c:
                for cb in comb[(len(order), c)]:
                    new = ''.join(sorted([order[i] for i in cb]))
                    menu[new] = menu.get(new, 0) + 1
                    if menu[new] > max_order.get(len(new), 0):
                        max_order[len(new)] = menu[new]
    
    # 4. 코스의 단품메뉴가 2개 이상이고 
    #    코스의 주문 개수가 동일 단품메뉴 개수 코스 中 최대이면 정답   
    for m in menu:
        if menu[m] >= 2 and menu[m] == max_order[len(m)]:
            answer.append(m)
    
    return sorted(answer)
    
'''
아직 효율성 잘 몰라서 신경 못 썼습니다 ㅠㅠ,,
테스트 1 〉	통과 (0.24ms, 10.2MB)
테스트 2 〉	통과 (0.14ms, 10.2MB)
테스트 3 〉	통과 (0.25ms, 10.3MB)
테스트 4 〉	통과 (0.25ms, 10.1MB)
테스트 5 〉	통과 (0.25ms, 10.3MB)
테스트 6 〉	통과 (0.77ms, 10.2MB)
테스트 7 〉	통과 (0.93ms, 10.2MB)
테스트 8 〉	통과 (6.11ms, 10.3MB)
테스트 9 〉	통과 (3.86ms, 10.4MB)
테스트 10 〉	통과 (4.46ms, 10.6MB)
테스트 11 〉	통과 (2.64ms, 10.4MB)
테스트 12 〉	통과 (3.11ms, 10.6MB)
테스트 13 〉	통과 (4.16ms, 10.6MB)
테스트 14 〉	통과 (3.02ms, 10.5MB)
테스트 15 〉	통과 (4.39ms, 10.6MB)
테스트 16 〉	통과 (1.47ms, 10.3MB)
테스트 17 〉	통과 (0.88ms, 10.3MB)
테스트 18 〉	통과 (0.34ms, 10.1MB)
테스트 19 〉	통과 (0.05ms, 10.2MB)
테스트 20 〉	통과 (1.09ms, 10.1MB)
'''
