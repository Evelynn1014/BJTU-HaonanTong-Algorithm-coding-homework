
def package(n,c,w,v):
    # n = 物品数 c = 背包最大承重 w = 物品重量 v= 物品价值
    value = [[0 for j in range(c+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range (1,c+1):
         #   value[i][j] = value[i - 1][j]
            for k in range(j//w[i-1] + 1):
                if  value[i][j] < value[i-1][j-k*w[i-1]] + k*v[i-1]:
                    value[i][j] =  value[i-1][j-k*w[i-1]] + k*v[i-1]
    return value


def show(n, c, w,value):
    print("最大价值：", value[n][c] )
    x = [False for i in range(n)]
    j = c
    for i in range(n, 0, -1):
        if value[i][j] > value[i-1][j]:
            x[i-1] = True
            j -= w[i-1]
    print('背包中物体： ')
    for i in range(n):
        if x[i]:
            print(i+1, ' ')





if __name__ == '__main__':
    n = input('输入物品数量')
    c = input('输入背包最大承重')
    w = []
    v = []
    for i in range(0,int(n)  ):
        a, b = input("输入一组物品的重量和价值：").split()
        w.append(int(a))
        v.append(int(b))
    value = package(int(n),int(c),w,v)
    print("最大价值：", value[int(n)][int(c)])
    #show(int(n),int(c),w,value)

