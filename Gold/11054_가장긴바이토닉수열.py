def max_length():
    global max_len
    if increase == 0 or decrease == 0:
        return
    length = increase + decrease + 1
    if max_len < length:
        max_len = length


n = int(input())

array = list(map(int,input().split()))

increase = 0
decrease = 0
max_len = 0
status = 'd' if array[0] > array[1] else 'i'

for i in range(n-1):
    if array[i] > array[i+1] :
        if status == 'i':
            max_length()
            decrease = 1
            status = 'd'
        else:
            decrease += 1


    elif array[i] < array[i+1]:
        if status == 'd':
            max_length()
            increase = 1
            status = 'i'
        else:
            increase += 1

    else:
        max_length()
        increase = 0
        decrease = 0
        status = ''
    print(i, increase, decrease, max_len)

print(max_len)