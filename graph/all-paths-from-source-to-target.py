class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []

        def dfs(node, path):
            if node == len(graph)-1:
                result.append(path[:])
                return
            
            for n in graph[node]:
                path.append(n)
                dfs(n, path)
                path.pop()

        dfs(0, [0])
        return result
                