
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        adj_list = defaultdict(list)

        # Step 1: Build adjacency list for the graph
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # Union-Find setup with path compression
        parents = list(range(n))
        size = [1] * n

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])  # Path compression
            return parents[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    parents[rootY] = rootX
                    size[rootX] += size[rootY]
                else:
                    parents[rootX] = rootY
                    size[rootY] += size[rootX]

        # Step 2: Group nodes by their values
        nodes_by_value = defaultdict(list)
        for i in range(n):
            nodes_by_value[vals[i]].append(i)

        count = 0

        # Step 3: Process nodes value by value
        for value in sorted(nodes_by_value.keys()):
            # First, union all nodes that have the same value
            for node in nodes_by_value[value]:
                for neighbor in adj_list[node]:
                    if vals[neighbor] <= value:  # Union only neighbors with the same or lower value
                        union(node, neighbor)

            # Count the good paths in each component
            component_count = defaultdict(int)
            for node in nodes_by_value[value]:
                root = find(node)
                component_count[root] += 1

            # For each component, count good paths (single node + pairs)
            for root in component_count:
                k = component_count[root]
                count += k  # Each node is a valid single-node path
                if k > 1:
                    count += (k * (k - 1)) // 2  # Add the paths formed by pairs of nodes in the same component

        return count