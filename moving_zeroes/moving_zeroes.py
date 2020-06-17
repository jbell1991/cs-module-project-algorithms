'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # function takes in an array of integers
    # new empty array
    new_arr = []
    # moves each non-zero integer to the left side of the array
    for i in arr:
        # if the integer != zero append it to the new list
        if i != 0:
            new_arr.append(i)
    for i in arr:
        # if the integer = zero append it after the non zero numbers
        if i == 0:
            new_arr.append(i)
    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")