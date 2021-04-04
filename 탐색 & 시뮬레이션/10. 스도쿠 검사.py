def check(x):
    for i in range(9):
        # check_list_1은 행, check_list_2는 열과 비교해준다.
        check_list_1 = [0] * 10
        check_list_2 = [0] * 10

        for j in range(9):
            check_list_1[x[i][j]] = 1
            check_list_2[x[j][i]] = 1

        if sum(check_list_1) != 9 or sum(check_list_2) != 9:
            return False

    for i in range(3):
        for j in range(3):
            # check_list_3은 각 그룹(3 * 3 모양의 9개 그룹)과 비교해준다.
            check_list_3 = [0] * 10
            for k in range(3):
                for l in range(3):
                    check_list_3[x[i * 3 + k][j * 3 + l]] = 1

            if sum(check_list_3) != 9:
                return False
    return True

sudoku = [list(map(int, input().split())) for _ in range(9)]

if check(sudoku):
    print("YES")
else:
    print("NO")