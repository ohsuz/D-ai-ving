def strToSecs(time):
    h,m,s = map(int, time.split(':'))
    return s + m*60+ h*3600

def secsToStr(Secs):
    h, Secs = Secs//3600, Secs%3600
    m, Secs = Secs//60, Secs%60
    return ("00" if h==0 else "{:02d}".format(h)) + ":" + ("00" if m==0 else "{:02d}".format(m)) + ":" + ("00" if Secs==0 else "{:02d}".format(Secs))
    
def solution(play_time, adv_time, logs):
    play_time, adv_time= strToSecs(play_time), strToSecs(adv_time)
    play_arr = [0 for _ in range(play_time+1)]
    for log in logs:
        start, end = map(strToSecs,log.split("-"))
        for t in range(start, end+1):
            play_arr[t] += 1

    maxVal, maxTime = sum(play_arr[:adv_time+1]), 0
    nowVal, start = maxVal, maxTime
    for end in range(adv_time+1, play_time+1):
        nowVal += play_arr[end] - play_arr[start]
        start += 1
        if nowVal > maxVal:
            maxVal, maxTime = nowVal, start

    return secsToStr(maxTime)

print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00","50:00:00",["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))