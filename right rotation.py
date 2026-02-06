def right_rotate(arr, d):
    n = len(arr)
    d = d % n
    return arr[n-d:] + arr[:n-d]

arr = [1, 2, 3, 4, 5]
print(right_rotate(arr, 4))  