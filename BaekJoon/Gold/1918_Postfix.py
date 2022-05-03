expression = input()
stack = []
result = ''

for char in expression:
    if char.isalpha():
        # 무조건 result로 보냄
        result += char
    elif char == '(':
        # 무조건 스택에 쌓음
        stack.append(char)
    elif char == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()
    elif char in ['*', '/']:
        while stack and stack[-1] in ['*', '/']:
            result += stack.pop()
        stack.append(char)
    elif char in ['+', '-']:
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.append(char)



while stack:
    result += stack.pop()

print(result)