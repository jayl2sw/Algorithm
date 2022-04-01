# 3 <= len(id) <= 15
# - _ . 소문자 숫자
# .는 중간에만 사용, 연속 사용 x
def solution(new_id):
    # 1단계
    tmp = new_id.lower()
    # 2단계
    new_id = ''
    for char in tmp:
        if char in ['-','_','.'] or ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9'):
           new_id += char
    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    # 4단계
    if new_id and new_id[0] == '.':
        new_id = new_id[1:] if len(new_id) > 1 else ''
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1] if len(new_id) > 1 else ''

    # 5단계
    if new_id == '':
        new_id = 'a'
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1] if len(new_id) > 1 else '.'
    # 7단계
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
