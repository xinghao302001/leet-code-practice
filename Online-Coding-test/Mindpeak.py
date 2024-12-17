def rotateArray(n, k, arr):
    # Reduce k to its effective value to prevent unnecessary rotations
    k = k % n

    # Rotate the array using a deque for efficient rotation
    from collections import deque

    arr_deque = deque(arr)
    arr_deque.rotate(k)

    return list(arr_deque)


# Example usage


def rotateArray2(n, k, arr):
    # Reduce k to its effective value to prevent unnecessary rotations
    k = k % n

    # Rotate the array in place using reverse
    def reverse(sub_arr, start, end):
        while start < end:
            sub_arr[start], sub_arr[end] = sub_arr[end], sub_arr[start]
            start += 1
            end -= 1

    # Reverse the entire array
    reverse(arr, 0, n - 1)
    # Reverse the first k elements
    reverse(arr, 0, k - 1)
    # Reverse the remaining elements
    reverse(arr, k, n - 1)

    return arr


def rotate_array(n, k, arr):
    # Write your code here
    k = k % n
    rotated_arr = arr[-k:] + arr[:-k]
    return rotated_arr


def rotate_array2(n, k, arr):
    # Write your code here
    k = k % n
    rotated_arr = [0] * n
    for i in range(n):
        rotated_arr[(i + k) % n] = arr[i]
    return rotated_arr


n = 5
k = 2
arr = [1, 2, 3, 4, 5]
result = rotateArray(n, k, arr)
print(result)  # Output: [4, 5, 1, 2, 3]
