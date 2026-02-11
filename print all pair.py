arr =[1,2,36,3,5,1,36]
for i in range (len(arr)):
    for j in range (i+1,len(arr)):
        if arr[i] == arr[j]:
            print(arr[j])