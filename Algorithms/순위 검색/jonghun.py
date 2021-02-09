from bisect import bisect_left

def solution(info, query):
    info_dict = {}
    score, score_num = [], []
    for num, spec in enumerate(info):
        l, j, c, f, s = spec.split()
        cases = []
        for spec1 in [l, '-']:
            for spec2 in [j, '-']:
                for spec3 in [c, '-']:
                    for spec4 in [f, '-']:
                        case = ' and '.join([spec1, spec2, spec3, spec4])
                        if case in info_dict.keys():
                            idx = bisect_left(info_dict[case], int(s))
                            info_dict[case].insert(idx, int(s))
                        else:
                            info_dict[case] = [int(s)]
                            
    answer = []
    for q in query:
        q = q.split()
        s = q.pop()
        case = ' '.join(q)
        if case in info_dict.keys():
            info = info_dict[case]
            idx = bisect_left(info, int(s))
            answer.append(len(info)-idx)
        else:
            answer.append(0)
    return answer