from cmath import pi
from typing import List
import heapq
import random


class Solution:
    ## heap
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]

    ## quick sort
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        def quickSelect(nums, k) -> int:
            pivot = random.choice(nums)
            big, equal, small = [], [], []
            # 将大于、小于、等于 pivot 的元素划分至 big, small, equal 中
            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)
            if k <= len(big):
                # 第 k 大元素在 big 中，递归划分
                return quickSelect(big, k)
            if (
                len(nums) - len(small) < k
            ):  ## len(nums) - len(small): how many elements >= pivot
                # 第 k 大元素在 small 中，递归划分
                return quickSelect(
                    small, k - len(nums) + len(small)
                )  # k - len(nums) + len(small): 你要跳过前面这 len(nums) - len(small) 个比它大的，再从 small 里找排在第几的。
            # 第 k 大元素在 equal 中，直接返回 pivot
            return pivot

        return quickSelect(nums, k)

    def findKthSmallest(nums, k):
        heapq.heapify(nums)  # 转成最小堆
        for _ in range(k - 1):
            heapq.heappop(nums)  # 弹出前 k-1 小的 heappop这个方法弹出之后会自动调整
        return heapq.heappop(nums)  # 第 k 小的元素
