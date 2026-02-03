def fun(arr):
    arr[0] += arr[-1] + 10
    for i in range(1, len(arr)-1):
        arr[i] += 10
    print(i)
arr =[12,34,56]
   
fun(arr)
print(arr)