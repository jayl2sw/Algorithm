# 모든 1/1000초를 비교할 수 없으니 특정 시간만 확인
# 시작하자마자 확인, 끝나기 직전 확인

def count(times, start):
    cnt = 0
    for t in times:
        # 1초의 시작보다 늦게 끝나고 1초의 마지막보다 일찍 끝남
        if t[1] >= start and t[0] < start + 1000:
            cnt += 1
    return cnt


def solution(lines):
    times = []
    for line in lines:
        # 받은 데이터를 date, time, duration으로 나누고
        date, time, duration = line.split()
        # h,m,s 로 나누고
        h, m, s = time.split(':')
        # duration에 s 없애줌
        duration = duration[:-1]

        # 1/1000초를 단위로 변환해서
        # 끝나기 직전 구하고
        end = int((int(h) * 3600 + int(m) * 60 + float(s)) * 1000)
        # 시작하자마자 구함
        start = int(end - float(duration) * 1000 + 1)

        times.append((start, end))

    result = 0

    for t in times:
        # atStart = count(times, t[0])
        # atEnd = count(times, t[1])
        # if result < atStart and atEnd <= atStart:
        #     result = atStart
        # elif result < atEnd and atStart <= atEnd:
        #     result = atEnd
        result = max(result, count(times, t[0]), count(times, t[1]))

    return result

lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
print(solution(lines))