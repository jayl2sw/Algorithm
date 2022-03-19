def dfs(tickets, start, used):
    if len(used) == len(tickets):
        result = used
        return result
    for ticket in tickets:
        if ticket[0] == start and ticket not in used:
            result = dfs(tickets, ticket[1], used + [ticket])
            if result:
                return result


def solution(tickets):
    global results
    tickets.sort()
    results = dfs(tickets, "ICN", [])
    answer = []
    for i in range(len(results)):
        if i == 0:
            answer = results[i]
        else:
            answer.append(results[i][1])

    return answer


tickets = [["ICN", "A"], ["ICN", "A"], ["A", "ICN"], ["A", "C"]]

print(solution(tickets))
