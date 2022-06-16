from itertools import combinations


for tc in range(50):
    N = int(input())
    answer = input()

    arr = [input() for _ in range(N)]

    n = 1
    while n <= N:

        cases = combinations(arr, n)
        for case in cases:
            for i in range(len(answer)):
                for line in case:
                    if line[i] == answer[i]:
                        break
                else:
                    break
            else:
                print(n)
                break
        else:
            n += 1
            continue
        break

    else:
        print(-1)

    if tc == 49:
        pass
    else:
        dump= input()