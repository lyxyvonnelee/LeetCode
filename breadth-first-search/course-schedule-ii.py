class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        courses = defaultdict(list)
        pre = [0] * numCourses

        for dst, src in prerequisites:
            courses[src].append(dst)
            pre[dst] += 1

        queue = deque([i for i in range(numCourses) if pre[i] == 0])
        while queue:
            node = queue.popleft()
            res.append(node)

            for neighbor in courses[node]:
                pre[neighbor] -= 1
                if pre[neighbor] == 0:
                    queue.append(neighbor)
        
        return res if len(res) == numCourses else []