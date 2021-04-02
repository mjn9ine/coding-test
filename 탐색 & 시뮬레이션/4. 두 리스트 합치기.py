n = int(input())

list_1 = list(map(int, input().split()))

m = int(input())

list_2 = list(map(int, input().split()))

# final_list = list_1 + list_2
# final_list.sort()
# 위의 방법은 nlogn의 시간복잡도.

final_list = []
p1, p2 = 0, 0
while p1 < n and p2 < m:
    if list_1[p1] < list_2[p2]:
        final_list.append(list_1[p1])
        p1 += 1
    else:
        final_list.append(list_2[p2])
        p2 += 1

if p1 < n:
    final_list += list_1[p1:]
else:
    final_list += list_2[p2:]

for i in final_list:
    print(i, end=' ')
