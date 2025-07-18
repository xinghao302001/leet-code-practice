# 索引下标
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        in_degree = [0] * numCourses

        for to_course, pre_course in prerequisites:
            if pre_course not in graph:
                graph[pre_course] = []
            graph[pre_course].append(to_course)
            in_degree[to_course] += 1

        queue = []
        ## [1,2],[2,1] => queue: 0
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        completed = 0
        while queue:
            course = queue.pop()
            completed += 1
            nghs = graph.get(course, [])
            for ngh in nghs:
                in_degree[ngh] -= 1
                if in_degree[ngh] == 0:
                    queue.append(ngh)
        return completed == numCourses
