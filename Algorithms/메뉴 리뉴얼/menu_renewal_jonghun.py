from itertools import combinations as combin

def solution(orders, course):
    n = len(orders)
    orders = [set(order) for order in orders]
    course_list = {}
    for c in course:
        course_list[c] = {}
    
    for i in range(n-1):
        order1 = orders[i]
        for j in range(i+1, n):
            order2 = orders[j]
            same_order = order1 & order2
            m = len(same_order)
            for c in course:
                if c > m: continue
                same_order = sorted(list(same_order))
                cases = list(map(''.join, combin(same_order, c)))
                for case in cases:
                    if case in course_list[c].keys():
                        course_list[c][case] += 1
                    else:
                        course_list[c][case] = 1

    answer = []
    for c in course:
        candidate_orders = course_list[c]
        if len(candidate_orders.values()) == 0: continue
        max_count = max(candidate_orders.values())
        for order, count in candidate_orders.items():
            if count == max_count:
                answer.append(order)
    answer.sort()
    return answer