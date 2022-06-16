def strint(string):
    h, m, s = map(int, string.split(':'))
    return h * 3600 + m * 60 + s

def solution(play_time, adv_time, logs):
    play_time = strint(play_time)
    adv_time = strint(adv_time)
    onair = [0] * (play_time + 1)

    starts = []
    for log in logs:
        start, end = log.split('-')
        start = strint(start)
        end = strint(end)
        onair[start] += 1
        onair[end] -= 1
        starts.append((start, start+adv_time))
        starts.append((end-adv_time, end))

    for i in range(1, len(onair)):
        onair[i] += onair[i-1]

    for i in range(1, len(onair)):
        onair[i] += onair[i - 1]

    _max = 0
    answer = 0

    for s, e in starts:
        temp = onair[e] - onair[s]
        if temp > _max:
            _max = temp
            answer = start

    answer = max(answer, 0)
    min_start = play_time - adv_time
    answer = min(min_start, answer)
    h = str(answer // 3600).zfill(2)
    m = str(answer % 3600 // 60).zfill(2)
    s = str(answer % 60).zfill(2)

    return h+':'+m+':'+s


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time, adv_time, logs))