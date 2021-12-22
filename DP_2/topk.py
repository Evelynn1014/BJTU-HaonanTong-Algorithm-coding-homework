def topk(arr, k):
    a = len(arr)

    if k >= a:
        return arr
    buffer = []
    while arr:
        mark = arr.pop()
        less, greater = [], []
        for x in arr:
            if x <= mark:
                less.append(x)
            else:
                greater.append(x)

        if len(greater) == k:
            buffer.extend(greater)
            return buffer
        elif len(greater) < k:
            arr = [mark] + less
            buffer.extend(greater)
            k -= len(greater)
        else:
            arr = greater



if __name__ == '__main__':
    n = input('输入数据数量')
    n = int(n)
    w = []

    for i in range(0, int(n)):
        a = input("输入一个数据")
        w.append(int(a))

    k = input("输入top k 的k值：")

    print("topk: ", topk(w, int(k)))
