from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tmp_list = nums1 + nums2
        tmp_list = sorted(tmp_list)
        list_len = len(tmp_list)
        if list_len % 2 == 0:
            idx_1 = int(len(tmp_list) / 2) - 1
            idx_2 = idx_1 + 1
            return (tmp_list[idx_1] + tmp_list[idx_2]) / 2
        else:
            idx = int(len(tmp_list) // 2)
            return tmp_list[idx]


class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get_kth_element(k):
            index1, index2 = 0, 0
            while True:
                if index1 == len(nums1):
                    return nums2[index2 + k - 1]
                if index2 == len(nums2):
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                new_index1 = min(index1 + k // 2 - 1, len(nums1) - 1)  ## index
                new_index2 = min(index2 + k // 2 - 1, len(nums2) - 1)
                pivot1 = nums1[new_index1]
                pivot2 = nums2[new_index2]

                if pivot1 <= pivot2:
                    k -= new_index1 - index1 + 1
                    index1 = new_index1 + 1
                else:
                    k -= new_index2 - index2 + 1
                    index2 = new_index2 + 1

        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 1:
            return get_kth_element((total_len + 1) // 2)
        else:
            return (
                get_kth_element(total_len // 2) + get_kth_element(total_len // 2 + 1)
            ) / 2
