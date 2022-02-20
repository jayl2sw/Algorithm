def reverse_array(array):
    for i in range(5):
        for j in range(5):
            if i < j:
                array[i][j], array[j][i] = array[j][i], array[i][j]
    return array
def bingow(array):
    count = 0
    for i in range(5):
        if sum(array[i]) == 0:
            count += 1
    array2 = reverse_array(array)
    for j in range(5):
        if sum(array2[j]) == 0:
            count += 1
    sub = 0
    for i in range(5):
        sub += array[i][i]
    if sub == 0:
        count += 1

    sub = 0
    for i in range(5):
        sub += array[4-i][i]
    if sub == 0:
        count += 1

    if count >= 3:
        return True
    else:
        return False


def change(i):
    for a in range(5):
        for b in range(5):
            if bingo[a][b] == array[i]:
                bingo[a][b] = 0
                return

bingo = [list(map(int, input().split())) for _ in range(5)]
array = list(map(int, input().split()))
for _ in range(4):
    array.extend(list(map(int, input().split())))

for i in range(25):
    change(i)
    if bingow(bingo):
        print(i+1)
        break