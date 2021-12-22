def mcm(p, n):
    d = [[0] * (100) for _ in range(100)]
    rec = [[0] * (100) for _ in range(100)]

    for i in range(1, n):
        d[i][i] = 0
        d[i][i + 1] = p[i - 1] * p[i] * p[i + 1]
        rec[i][i] = 0

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            d[i][j] = d[i + 1][j] + p[i - 1] * p[i] * p[j];
            rec[i][j] = i;
            for k in range(i + 1, j):
                temp = d[i][k] + d[k + 1][j] + p[i - 1] * p[j] * p[k]
                if temp < d[i][j]:
                    d[i][j] = temp
                    rec[i][j] = k
    print("最优：", d[1][n])
    return rec


def show(b, rec, i, j):
    if i == j:
        print(b[i],end = " ")
        return None
    print("(", end = "")
    show(b, rec, i, rec[i][j])
   # print(')(', end = "")
    show(b, rec, rec[i][j] + 1, j)
    print(')', end = "")


if __name__ == '__main__':
    n = input('输入矩阵数量')
    n = int(n)
    w = []
    b = []
    for i in range(0, int(n)+1):
        a = input("输入一个数值")
        w.append(int(a))
        b.append("a" + str(i))
    b.append("a" + str(n))
    rec = mcm(w, n)

   # print(b)
    show(b, rec, 1, n)
