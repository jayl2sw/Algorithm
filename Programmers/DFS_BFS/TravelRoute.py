def dfs(tickets, start, used, N):
    if len(used) == N:
        result = used
        return result
    for ticket in tickets:
        if ticket[0] == start and ticket not in used:
            result = dfs(tickets, ticket[1], used + [ticket], N)
            if result:
                return result


def solution(tickets):
    tickets.sort()
    N = len(tickets)
    results = dfs(tickets, "ICN", [], N)
    answer = []
    for i in range(len(results)):
        if i == 0:
            answer = results[i]
        else:
            answer.append(results[i][1])

    return answer


tickets = [["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]

print(solution(tickets))
