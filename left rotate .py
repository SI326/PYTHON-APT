def left_rotate(arr, d):

    n = len(arr)
    d = d % n  
    return arr[d:] + arr[:d]
arr = [1, 2, 3, 4, 5]
print(arr[1:] + arr[:1]) 
print("Original:", arr)
print("Rotate by 1:", left_rotate(arr, 1))
print("Rotate by 2:", left_rotate(arr, 2))  
print("Rotate by 3:", left_rotate(arr, 3))  