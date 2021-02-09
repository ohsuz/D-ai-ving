def solution(numbers, target):
    sums = [sum(numbers[i:]) for i in range(len(numbers))]
    qs = [0]
    for idx in range(len(numbers)):
        tnum = numbers[idx]
        newq = []
        for q in qs:
            if not (q < target and q + sums[idx] < target) :
                newq.append(q+tnum)
            if not (q > target and q - sums[idx] > target):
                newq.append(q-tnum)
        qs = newq
    return qs.count(target)

print(solution([1,1,1,1,1], 3))