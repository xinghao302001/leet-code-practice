from typing import List
import math

def swap(arr: List[int], i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def ShellSort(arr: List[int]):
    gap = 1
    while(gap < len(arr) / 3):
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(arr)):
            ### !!!!
            j = i
            while j >= gap:
                if arr[j] < arr[j-gap]:
                    temp = arr[j]
                    arr[j] = arr[j-gap]
                    arr[j-gap] = temp
                    j-= gap
                else:
                    break
        gap = math.floor(gap / 3)
    return arr



if __name__ == "__main__":
    ts_case = [2,5,4,3,6]
    res = ShellSort(ts_case)
    print(res)