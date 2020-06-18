'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    max = 0
    new_arr = []
    for i in range(len(nums) - k + 1):
        max = nums[i]
        for j in range(0, k):
            if nums[i + j] > max:
                max = nums[i + j]
        new_arr.append(max)
    return new_arr   


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
