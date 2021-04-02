def isPalinrome(x):
    for i in range(len(x) // 2):
        if x[i] != x[-(i + 1)]:
            if x[i].lower() == x[-(i + 1)] or x[i].upper() == x[-(i + 1)]:
                continue
            return False
    return True

T = int(input())
for t in range(T):
    s = input()
    if isPalinrome(s):
        print(f'#{t + 1} YES')
    else:
        print(f'#{t + 1}NO')

