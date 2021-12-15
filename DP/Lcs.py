def LCS(a, b):
    print('\n')
    n = len(a)
    m = len(b)
    a = '0' + a
    b = '0' + b
   # a.insert(0, '0')
    #b.insert(0, '0')
    C = [([0] * (m + 1)) for i in range(n + 1)]
    rec = [([0] * (m + 1)) for i in range(n + 1)]
    for x in range(0, n + 1):
        for y in range(0, m + 1):
            if (x == 0 or y == 0):

                C[x][y] = 0
            elif a[x] == b[y]:
                C[x][y] = (C[x - 1][y - 1] + 1)
                rec[x][y] = 0
            elif C[x - 1][y] >= C[x][y - 1]:
                C[x][y] = C[x - 1][y]
                rec[x][y] = 1
            else:
                C[x][y] = C[x][y - 1]
                rec[x][y] = -1

        print(x)
        print(C[x])


    return C[n][m], rec, n, m


def printLCS(c, a, x, y):
    if (x == 0 or y == 0):
        return 0
    if c[x][y] == 0:
        printLCS(c, a, x - 1, y - 1)
        print(a[x-1])
    elif c[x][y] == 1:
        printLCS(c, a, x - 1, y)
    else:
        printLCS(c, a, x, y - 1)


if __name__ == '__main__':
    a = input('输入字符串a')
    b = input('输入字符串b')
    length, rec, x, y = LCS(a, b)
    print('最长公共子序列长度为：', length)
    print('最长公共子序列为：')
    printLCS(rec, a, x, y)