def count(check, start, end):
    cnt = 0
    for c in check:
        if c[0] < end and c[1] >= start:
            cnt += 1
    return cnt


def solution(lines):
    check = []
    for line in lines:
        date, time, duration = line.split()
        h, m, s = time.split(':')
        duration = duration[:-1]

        end = (int(h) * 3600 + int(m) * 60 + float(s)) * 1000
        start = end - float(duration) * 1000 + 1

        check.append((start, end))

    result = 0

    for c in check:
        result = max(result, count(check, c[0], c[0]+1000), count(check, c[1]-1, c[1]+999))

    return result

lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
print(solution(lines))