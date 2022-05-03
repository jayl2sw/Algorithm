import re

def solution(words, queries):
    answer = []
    for query in queries:
        if query.count('?') == len(query):
            count = len([0 for word in words if len(word) == len(query)])
            answer.append(count)
            continue
        query = ' '+query.replace('?', '\w{1}') + ' '
        print(query)
        query_parser = re.compile(query)
        print(query_parser.findall(" "+"  ".join(words)+" "))
        answer.append(len(query_parser.findall(" "+"  ".join(words)+" ")))

    return answer
print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]))

# # 2
# import re
#
# def solution(words, queries):
#     answer = []
#     for query in queries:
#         l = len(query)
#         query = query.replace('?', '\w{1}')
#         query_parser = re.compile(query)
#         answer.append(len(query_parser.findall(" ".join([word for word in words if len(word)==l]))))
#
#     return answer
#
# print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))

# # 3
# import re
#
# def solution(words, queries):
#     answer = []
#     for query in queries:
#         l = len(query)
#         query = query.replace('?', '\w{1}')
#         query_parser = re.compile(query)
#         answer.append(len(query_parser.findall(" ".join([word for word in words if len(word)==l]))))
#
#     return answer

# 4
# from collections import defaultdict
# import re
#
# def solution(words, queries):
#     answer = []
#     d = defaultdict(list)
#     for word in words:
#         d[len(word)].append(word)
#
#     for query in queries:
#         l = len(query)
#         query = query.replace('?', '\w{1}')
#         query_parser = re.compile(query)
#         answer.append(len(query_parser.findall(" ".join(d[l]))))
#
#     return answer
# print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))