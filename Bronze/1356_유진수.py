def multiply(string):
    result = 1
    for char in string:
        result *= int(char)
    return result

def seperate(string):
    for i in range(1, len(string)):
        front = string[:i]
        back = string[i:]

        if multiply(front) == multiply(back):
            return "YES"

    return "NO"

n = input()
print(seperate(n))