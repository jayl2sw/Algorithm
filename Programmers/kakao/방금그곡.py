# 시작과 끝 차이 찾아내는 함수
def difference(start, end):
    eh, em = map(int, end.split(':'))
    sh, sm = map(int, start.split(':'))
    return (eh-sh)*60 + em-sm

# #들어가는 음을 다른 문자열로 변환
def preprocess(notes):
    result = ''
    for i in range(len(notes)):
        if notes[i] == '#':
            continue
        elif i < len(notes) - 1 and notes[i+1] == '#':
            result += str(chr(ord(notes[i])+7))
        else:
            result += str(notes[i])
    return result


def solution(m, musicinfos):
    # 기본 answer값 초기화
    answer = '(None)'
    ansTime = 0
    m = preprocess(m)
    for music in musicinfos:
        start, end, name, notes = music.split(',')
        notes = preprocess(notes)
        time = difference(start, end)
        # 최종적으로 라디오에서 송출된 총 notes 구함
        notes = notes * (time//len(notes)) + notes[:time % len(notes)]

        # 안에 있고 ansTime보다 time이 크면 갱신
        if m in notes and ansTime < time:
            answer = name
            ansTime = time

    return answer

musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
m = "CC#BCC#BCC#BCC#B"

print(solution(m, musicinfos))