n = int(input())
book_list = []
for i in range(n):
    book_list.append(input())

book_list.sort()

book_times = []
sub_total = 1
for idx in range(len(book_list)-1):
    if book_list[idx] == book_list[idx+1]:
        sub_total += 1
    else:
        book_times.append(sub_total)
        sub_total = 1
book_times.append(sub_total)

mx = max(book_times)

where = 0
for i in range(len(book_times)):
    if book_times[i] == mx:
        break
    where += book_times[i]


print(book_list[where])


