x, b = map(int, input().split())
result = ''
while x:
    result = str(x % b) + result
