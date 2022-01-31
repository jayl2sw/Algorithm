def find_alpha(array):
    alpha = (array[2] - array[1]) / (array[1] - array[0])
    return alpha

def check_array(array, alpha):
    if alpha == 0:
        for i in range(1, len(array)-1):
            if array[i-1]+array[i+1] != array[i]*2:
                return False
    else:
        for i in range(1, len(array)):
            if array[i] != array[0] + (array[1]-array[0]) * (alpha**i - 1) / (alpha - 1):
                return False
    return True


def find_next(array, alpha, n):
     next = array[0] + (array[1]-array[0])*(alpha ** n - 1) / (alpha - 1)
     return int(next)

n = int(input())
array = list(map(int,input().split()))

if n < 1:
    print('A')
elif n == 2:
    if array[0] == array[1]:
        print(array[0])
    else:
        print("A")
else:
    alpha = find_alpha(array)
    if check_array(array, alpha) == False:
        print("B")
    else:
        print(find_next(array, alpha, n))
