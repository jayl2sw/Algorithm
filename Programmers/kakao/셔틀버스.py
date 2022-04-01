def solution(n, t, m, timetable):
    answer = ''
    start = 9 * 60
    departs = []
    for i in range(n):
        departs.append(start+t*i)

    timetable = sorted(list(map(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1]), timetable)), reverse=True)

    i = 0
    for depart in departs:
        num = 0
        while i < len(timetable)-1 and timetable[i] < depart and num <= m:
            i += 1
            num += 1
            if i == len(timetable)-1:
                if num == m:
                    last = timetable[i]-1
                else:
                    last = depart
            elif timetable[i] == timetable[i + 1]:
                last = timetable[i]-1
            else: last = timetable[i]



    return str(last//60).zfill(2)+':'+str(last%60).zfill(2)


n = 1
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
print(solution(n, t, m, timetable))