n = int(input().rstrip())

def find_multiple1(n):
    number = ''
    while True:
        number += '1'
        if int(number) % n == 0 :
            return len(number)

print(find_multiple1(n))
