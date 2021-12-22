def led(w1, w2):
    m, n = len(w1), len(w2)
    if m == 0:
        return n
    if n == 0:
        return m
    edit = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        edit[i][0] = i

    for j in range(1, n + 1):
        edit[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if w1[i - 1] == w2[j - 1]:
                ju = 0
            else:
                ju = 1
            edit[i][j] = min(edit[i - 1][j - 1], min(edit[i - 1][j], edit[i][j - 1])) + ju
    return edit[m][n]


if __name__ == '__main__':
    A = input("输入字符串1：")
    B = input("输入字符串2：")
    print("最短编辑距离")
    print( led(A, B))
