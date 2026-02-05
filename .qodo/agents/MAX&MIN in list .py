arr = [2,3,4,5,5,6,1]
maximum = arr[0]
minimum = arr[0]

for num in arr:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
    
    print ("max", maximum)
    print ("min",minimum)