class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for dst, src in prerequisites:
            adj_list[src].append(dst)
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True

            state[course] = 1
            for c in adj_list[course]:
                if not dfs(c):
                    return False
            state[course] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
