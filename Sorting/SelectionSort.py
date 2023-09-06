from typing import List


def swap(arr: List[int], i:int, j:int):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def SelectionSort(arr: List[int]):
    for i in range(0, len(arr) - 1):
        minIndex = i
        for j in range(i+1, len(arr)):
            if (arr[j] < arr[minIndex]):
                minIndex = j
        swap(arr, i, minIndex)
    
    return arr

if __name__ == "__main__":
    ts_case = [2,5,4,3,6]
    res = SelectionSort(ts_case)
    print(res)