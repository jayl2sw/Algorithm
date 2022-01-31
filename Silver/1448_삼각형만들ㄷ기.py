n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)

triangle = array[:3]
rest = array[3:]

for i in range(len(rest)+1):
    if triangle[0] >= triangle[1] + triangle[1]:
        if len(rest) == 0:
            print(-1)
            break
        else:
            del triangle[0]
            triangle.append(rest[0])
            del rest[0]

    else:
        print(sum(triangle))
        break










