def solution(id_list, reports, k):
    N = len(id_list)
    answer = [0] * N
    reported = [[] for _ in range(N)]
    for report in set(reports):
        g, p = report.split()
        reported[id_list.index(p)].append(g)

    for report in reported:
        if len(report) >= k:
            for person in report:
                answer[id_list.index(person)] += 1

    return answer

def solution2(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : [] for x in id_list}

    for r in set(report):
        p, q = r.split()
        reports[q].append(p)

    for v in reports.values():
        if len(v) >= k:
            for m in v:
                answer[id_list.index(m)] += 1
    return answer

def solution3(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))
print(solution2(id_list, report, k))
print(solution3(id_list, report, k))
