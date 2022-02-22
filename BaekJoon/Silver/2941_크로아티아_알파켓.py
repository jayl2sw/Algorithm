croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

string = input()
count = 0
for word in croatia:
    string = string.replace(word, 'p')

print(len(string))
