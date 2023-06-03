# Candy

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy_array = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy_array[i] = candy_array[i-1] + 1
        ## stop_index = -1 !! 
        for j in range(len(ratings)-2, -1,-1):
            if ratings[j] > ratings[j+1]:
                candy_array[j] = max(candy_array[j+1] + 1, candy_array[j])
        return sum(candy_array)
