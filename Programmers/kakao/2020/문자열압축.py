def Alzip(string, start, size):
    if string[start:start+size] == string[start+size:start+size*2]:
        return Alzip(string, start+size, size) + 1
    else:
        return 1

def solution(s):
    min_length = len(s)
    for size in range(1, len(s)//2+2):
        idx = 0
        length = 0
        while idx + size < len(s):
            n = Alzip(s, idx, size)
            if n > 1:
                idx += size * n
                length += size + len(str(n))
            else:
                idx += size * n
                length += size * n
            print(length)
        length += len(s) - idx
        print(length)
        print('size:',size, 'length:', length)
        if length < min_length:
            min_length = length
    return min_length

print(solution("aaaaaaaaaaaaaaaaaaaaa"))