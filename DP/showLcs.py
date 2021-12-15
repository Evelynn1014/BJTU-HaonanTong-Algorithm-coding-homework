def LCS(a, b):
    print('\n')
    n = len(a)
    m = len(b)
    a = '0' + a
    b = '0' + b
    rs = 0
    p = 0
    q = 0
    C = [([0] * (m + 1)) for i in range(n + 1)]
    rec = [([0] * (m + 1)) for i in range(n + 1)]
    for x in range(0, n + 1):
        for y in range(0, m + 1):
            if (x == 0 or y == 0):
                C[x][y] = 0
            elif a[x] == b[y]:
                C[x][y] = (C[x - 1][y - 1] + 1)
                rec[x][y] = 0

            else:
                C[x][y] = 0
                rec[x][y] = -1
            rs = max(rs,C[x][y])
            if(rs < C[x][y]):
                p = x
        print(x)
        print(C[x])


    return rs, p



if __name__ == '__main__':
    a = input('输入字符串a')
    b = input('输入字符串b')
    rs, p = LCS(a, b)
    print('最长公共子串长度为：', rs)
    print('最长公共子串为：')
    for i in range(p, p+rs):
        print (a[i+1])