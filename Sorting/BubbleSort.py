from typing import List


def swap(arr: List[int], i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def BubbleSort(arr: List[int]):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
    return arr

if __name__ == "__main__":
    ts_case = [2,5,4,3,6]
    res = BubbleSort(ts_case)
    print(res)
