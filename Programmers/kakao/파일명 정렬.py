# 문제점 => 사전순으로 정렬한다
# '.', '-', ' '

numbers = list(map(str, range(10)))

def preprocess(file):
    start_num = 0
    start_tail = len(file)
    for i in range(len(file)):
        if file[i] in numbers:
            start_num = i
            break

    for j in range(i + 1, len(file)):
        if file[j] not in numbers or j == i + 5:
            start_tail = j
            break

    HEAD = file[:start_num]
    NUMBER = int(file[start_num:start_tail])
    return HEAD, NUMBER, file


def solution(files):
    answers = []
    for file in files:
        answers.append(preprocess(file))

    answers.sort(key=lambda x: (x[0].lower(), x[1]))


    return [x[2] for x in answers]

files = ["A킼나15642sae","SADSAD2314", "A015643sae", "A1564sa62", "A1564sa63"]
print(solution(files))
