def change(n):
    switches[n] = abs(switches[n] - 1)
    return


number_of_switches = int(input())

switches = [-1] + list(map(int, input().split())) + [-1]

number_of_students = int(input())

for _ in range(number_of_students):
    gender, n = map(int, input().split())

    if gender == 1:
        for i in range(n, number_of_switches + 1, n):
            change(i)
    else:
        change(n)
        d = 1
        while switches[n - d] == switches[n + d]:
            change(n - d)
            change(n + d)
            d += 1

for i in range(1, number_of_switches+1):
    print(switches[i], end=' ')
    if i % 20 == 0:
        print()