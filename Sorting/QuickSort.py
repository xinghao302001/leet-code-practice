from typing import List


def partiton(arr, start, end):
    pivot = arr[start]

    while start < end:
        while start< end and arr[end] >= pivot:
            end-= 1
        arr[start] = arr[end]
        while start < end and arr[end] <= pivot:
            start+= 1
        arr[end] = arr[start]
    
    arr[start] = pivot
    return start

def quick_sort(arr: List[int], start: int, end: int):
    if start >= end:
        return
    middle = partiton(arr, start, end)
    quick_sort(arr, start, middle-1)
    quick_sort(arr, middle+1, end)



def QuickSort(arr):
    quick_sort(arr, 0, len(arr)-1)


if __name__ == "__main__":
    # ts_case = [2, 9, 7, 8, 5, 0, 1, 6, 4, 3]
    ts_case = [2,5,4,3,6]
    # build_heap(ts_case, len(ts_case))
    QuickSort(ts_case)
    print(ts_case)