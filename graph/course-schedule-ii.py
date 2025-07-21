class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        visited = set()
        visiting = set()
        result = []

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)
            for c in graph[course]:
                if not dfs(c):
                    return False
                   
            visiting.remove(course)
            visited.add(course)
            result.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return result
