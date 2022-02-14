croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

string = input()
count = 0
for word in croatia:
    if word == 'dz=':`
        count += 2
    elif word in string:
        count += 1

print(len(string) - count)

