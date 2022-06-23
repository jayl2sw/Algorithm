# string = input()
# pattern = input()
#
# while pattern in string:
#     string = string.replace(pattern, "")
#
# if string:
#     print(string)
# else:
#     print("FLURA")


string = input()
pattern = input()

stack = []

for char in string:
    stack.append(char)
    if char == pattern[-1] and ''.join(stack[-len(pattern):]) == pattern:
        for _ in range(len(pattern)):
            stack.pop()
if stack:
    print(f"{''.join(stack)}")
else:
    print('FRULA')
