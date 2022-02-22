n = int(input())
array = list(map(int,input().split()))

array.sort()
AVG = sum(array)/len(array)
result = AVG * 100/ array[-1]

print(result)