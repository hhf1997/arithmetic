def bubbleSort(arr):
    # 限制循环的次数
    for i in range(1, len(arr)):
        # 对循环内的元素进行便利比较
        for j in range(0, len(arr)-i):
            # 对元素进行判断
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr=[4,5,3,2,1,9,8,7]
b=bubbleSort(arr)
print(b)
