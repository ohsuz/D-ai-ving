def strToSecs(time):
    h,m,s = map(int, time.split(':'))
    return h*3600 + m*60+s

def secsToStr(Secs):
    h, Secs = Secs//3600, Secs%3600
    m, Secs = Secs//60, Secs%60
    return '{:02d}:{:02d}:{:02d}'.format(h,m,Secs)

def solution(play_time, adv_time, logs):
    play_time, adv_time= strToSecs(play_time), strToSecs(adv_time)
    play_arr = [0 for _ in range(play_time+1)]
    for log in logs:
        start, end = map(strToSecs,log.split("-"))
        play_arr[start] += 1
        play_arr[end] -= 1
    maxVal, maxTime, nowVal, start, adder = 0, 0, 0, 0, 0
    for end in range(play_time +1):
        adder += play_arr[end]
        nowVal += adder
        play_arr[end] = adder
        if end >= adv_time:
            nowVal -= play_arr[start]
            start += 1
        if nowVal > maxVal:
            maxVal, maxTime = nowVal, start
    return secsToStr(maxTime)

print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00","50:00:00",["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))