'''
    https://velog.io/@blush0722/%EC%88%9C%EC%9C%84-%EA%B2%80%EC%83%89
    원래 코드도 통과하긴 했지만 가독성이 떨어지고 볼 필요가 없을 것 같아서
    깔끔히 푸신 분꺼 올렸습니다.
'''

from collections import defaultdict
import bisect
def solution(info, query):
    answer = list()
    arr = defaultdict(list)
    
    for person in map(lambda x: x.split(), info):
        bisect.insort(arr[tuple(person[:-1])],int(person[-1]))
    
    for q in map(lambda x: x.replace("and", "").split(), query):
        search_keys = list(arr.keys())
        
        for idx, what in enumerate(q[:-1]):
            if what != '-':
                search_keys = [tmp for tmp in search_keys if tmp[idx] == what]
        
        answer.append(sum([len(arr[idx]) - bisect.bisect_left(arr[idx], int(q[-1])) for idx in search_keys]))
    return answer