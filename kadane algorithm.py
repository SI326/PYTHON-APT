def max_subarray(arr):
    max_sum = arr[0]
    current_sum = 0
    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum

        if current_sum < 0:
            current_sum = 0
    return max_sum
arr =[-2,1,-4,6,-4,-1,3,5]
print(max_subarray(arr))