cards = list(range(1, 21))

for _ in range(10):
    a, b = map(int, input().split())
    temp_list = cards[a - 1 : b]
    temp_list = temp_list[::-1]
    cards[a - 1 : b] = temp_list

for c in cards:
    print(c, end=' ')
