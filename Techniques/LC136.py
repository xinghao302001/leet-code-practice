from typing import List
import operator
from functools import reduce


# def xor(a,b):
#     return (a and not b) or (not a and b)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(operator.xor, nums)
