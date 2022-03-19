
def solution(begin, target, words):
    if target not in words:
        return 0

    q = [(0, begin)]
    v = []
    while q:
        time, now = q.pop(0)
        if now == target:
            return time
        v.append(now)
        for word in words:
            count = 0
            for i in range(len(word)):
                if word[i] != now[i]:
                    count += 1
            if count == 1 and word not in v:
                q.append((time+1, word))
    return 0


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]


print(solution(begin,target,words))
