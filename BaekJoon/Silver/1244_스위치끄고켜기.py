def on_off(a):
    return abs(a - 1)


# 총 스위치 개수
number_of_switch = int(input())

# 스위치 상태
switches = [-1] + list(map(int, input().split()))
switches.append(-1)



# 학생 수
number_of_student = int(input())

# 학생 상태 합
for _ in range(number_of_student):
    gender, number = map(int, input().split())
    if gender == 1:
        j = number_of_switch // number
        for k in range(1, j+1):
            switches[k * number] = on_off(switches[k * number])
        # for i in range(number, number_of_switch, number):
        #     switches[i] = on_off(switches[i])
    else:
        j = 0
        switches[number] = on_off(switches[number])
        while switches[number - j] == switches[number + j]:
            switches[number - j] = on_off(switches[number - j])
            switches[number + j] = on_off(switches[number + j])
            j += 1

for i in range(1, number_of_switch+1):
    print(str(switches[i]), end=' ')
    if i % 20 == 0:
        print()