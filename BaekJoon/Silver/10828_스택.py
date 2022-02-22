n = int(input())

array = []

for i in range(n):
    input_data = input()
    if input_data[1] == 'u':
        input_data, x = input_data.split()
        array.append(x)
    elif input_data == 'top':
        if bool(array):
            print(array[-1])
        else:
            print(-1)
    elif input_data == 'pop':
        if bool(array):
            x = array.pop()
            print(x)
        else:
            print(-1)
    elif input_data == 'empty':
        print(int((bool(array)-1)**2))
    else:
        print(len(array))



