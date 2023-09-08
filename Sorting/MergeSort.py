from typing import List

def mergeSort(arr:List[int]) -> List[int]:
    if len(arr) > 1:
        mid = len(arr) // 2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i = i + 1
            else:
                arr[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j = j + 1
            k = k + 1
        
    return arr

if __name__ == "__main__":
    # ts_case = [2, 9, 7, 8, 5, 0, 1, 6, 4, 3]
    ts_case = [2,5,4,3,6]
    # build_heap(ts_case, len(ts_case))
    mergeSort(ts_case)
    print(ts_case)
        