from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    # course에 들어갈 수 있는 음식의 갯수 별로, 가장 많이 주문된 조합을 고른다
    for course_len in course:
        possible_menus = []
        for order in orders:
            # order에서 course_len 갯수의 음식으로 만들 수 있는 메뉴들 추출한다
            for comb in combinations(order, course_len):
                possible_menus.append(''.join(sorted(comb)))
        
        menu_counts = Counter(possible_menus) # 사용자가 주문한 음식을 기반으로 만들어 낸 코스 요리의 갯수를 센다
        # 만약 그런 조합 메뉴가 존재하고, 한 명 이상의 사용자에게서 주문 되었다면, 가장 많이 주문된 조합 메뉴를 골라 정답에 넣는다
        if possible_menus and max(menu_counts.values()) > 1:
            max_count = max(menu_counts.values())
            answer.extend([menu for menu, menu_count in menu_counts.items() if menu_count == max_count])
        
    answer = sorted(list(set(answer)))
    
    return answer

            
if __name__ == "__main__":
    assert(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]) == ["AC", "ACDE", "BCFG", "CDE"])
    assert(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]) == ["ACD", "AD", "ADE", "CD", "XYZ"])
    assert(solution(["XYZ", "XWY", "WXA"], [2,3,4]) == ["WX", "XY"])

    print("All samples passed")