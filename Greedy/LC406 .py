## Queue Reconstruction by Height

from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ### If the first elements are equal, then the second element
        ## dim: -x[0] ---> ascending sort
        people.sort(key=lambda x:(-x[0], x[1]))
        que = []

        for p in people:
            que.insert(p[1], p)
            
        return que