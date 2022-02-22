array = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
result = ''
for times in range(2):
    k = input()
    for i in range(len(array)):
        if k == array[i]:
            result += str(i)
k = input()
for i in range(len(array)):
    if k == array[i]:
        result += str(0) * i

print(int(result))
