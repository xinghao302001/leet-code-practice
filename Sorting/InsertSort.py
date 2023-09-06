from typing import List


def swap(arr: List[int], i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def InsertSort(arr: List[int]):
    for i in range(1, len(arr)):
        j = i
        while arr[j] < arr[j-1] and j >= 1:
            swap(arr, j, j-1)
            j -= 1

    return arr

if __name__ == "__main__":
    ts_case = [2,5,4,3,6]
    res = InsertSort(ts_case)
    print(res)
