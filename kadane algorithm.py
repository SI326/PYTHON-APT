def max_subarray(arr):
    max_sum = arr[0]
    current_sum = 0
    for num in arr:
        current_sum += num