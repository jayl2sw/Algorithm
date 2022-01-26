numbers = int(input())

stack = [0]
for i in range(1,numbers):
    number = int(input())
    if stack[-1] < number:
        stack.push(i)
        print("+")
    else:
        while stack[-1] == number:
            stack.pop(i)
            print("-")
    

