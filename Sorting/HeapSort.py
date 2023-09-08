from typing import List


def heap_adjust (arr: List[int], start:int, end:int):
    left = 2*start + 1
    right = 2*start + 2
    max_index = start 
    if left < end and arr[left] > arr[max_index] :
        max_index = left
    if right < end and arr[right] > arr[max_index]:
        max_index = right
    if max_index != start:
        temp = arr[start]
        arr[start] =arr[max_index]
        arr[max_index] = temp
        heap_adjust(arr,max_index,end)

def build_heap(arr: List[int], end:int):
    for i in range(end//2,-1,-1):
        #### !!!!s
        heap_adjust(arr,i,end)     

def heap_sort(arr:List[int]):
    size = len(arr)
    build_heap(arr, size)
    for i in range(len(arr)-1, 0, -1):
        temp = arr[i]
        arr[i] = arr[0]
        arr[0] = temp
        heap_adjust(arr, 0, i)
    return arr

if __name__ == "__main__":
    # ts_case = [2, 9, 7, 8, 5, 0, 1, 6, 4, 3]
    ts_case = [2,5,4,3,6]
    # build_heap(ts_case, len(ts_case))
    res = heap_sort(ts_case)
    print(res)