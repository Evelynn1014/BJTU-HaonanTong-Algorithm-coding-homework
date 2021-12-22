def maxsub(w, n):
    b = 0
    # sum = w[0]
    sum = 0
    b = 0
    for i in range(n):
        b = b + w[i] if b > 0 else w[i]
        if b > sum:
            sum = b

    print('最大子段和：', sum)


def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    return c


def mergeSort(w):
    if len(w) <= 1:
        return w
    middle = len(w) // 2
    left = mergeSort(w[:middle])
    right = mergeSort(w[middle:])
    return merge(left, right)


def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]

    for j in range(low, high):

        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)





if __name__ == '__main__':
    n = input('输入数据数量')
    n = int(n)
    w = []
    arr = []



    for i in range(0, int(n)):
        a = input("输入一个数据")
        w.append(int(a))

    for i in range(0, int(n)):
        arr.append(w[i])

    maxsub(w, int(n))
    print("源数据：    ", w)
    print("merge sort:",mergeSort(w))
    print("源数据：    ", arr)
    quickSort(arr, 0, n - 1)
    a = []
    for i in range(n):
        a.append(arr[i])
    print("quick sort:",a)

    c = input("输入前k大中的k值")
