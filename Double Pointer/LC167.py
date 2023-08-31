## two Sum
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            sum_res = numbers[left] + numbers[right]
            if sum_res == target:
                return [left+1, right+1]

            elif sum_res < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]
    

if __name__ == "__main__":
    test_case = [2,7,11,15]
    target = 9
    sol = Solution()
    res = sol.twoSum(test_case, target)
    print(res)