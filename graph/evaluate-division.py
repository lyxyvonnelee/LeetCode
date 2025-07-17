class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            visited.add(start)
            for neighbor, val in graph[start].items():
                if neighbor in visited:
                    continue

                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return result * val

            return -1.0

        return [dfs(a, b, set()) for a, b in queries]
