class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(dict)
        for (a, b), weight in zip(equations, values):
            graph[a][b] = weight
            graph[b][a] = 1 / weight

        def dfs(a, b, visited):
            if a not in graph or b not in graph:
                return -1.0

            if a == b:
                return 1.0

            visited.add(a)
            for neighbor, value in graph[a].items():
                if neighbor not in visited:
                    result = dfs(neighbor, b, visited)
                    if result != -1.0:
                        return result * value
            return -1.0

        result = []
        for a, b in queries:
            result.append(dfs(a, b, set()))

        return result
