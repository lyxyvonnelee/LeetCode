class Solution:
    from collections import defaultdict
    import heapq
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        result = []
        self.dfs('JFK', graph, result)
        return result[::-1]
    
    def dfs(self, node, graph, res):
        heap = graph[node]
        while heap:
            next = heapq.heappop(heap)
            self.dfs(next, graph, res)
        res.append(node)


