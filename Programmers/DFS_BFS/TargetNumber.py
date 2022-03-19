def solution(numbers, target):
    global answer
    if not numbers:
        if target == 0:
            answer +=1

        return None

    solution(numbers[1:], target + numbers[0])
    solution(numbers[1:], target - numbers[0])


numbers = [4, 1, 2, 1]
target = 4
answer = 0

solution(numbers, target)
print(answer)
