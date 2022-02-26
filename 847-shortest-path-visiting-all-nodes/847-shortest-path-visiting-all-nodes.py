class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)
        INF = 10 ** 10
        dist = [[INF] * N for _ in range(N)]
        
        for i, edges in enumerate(graph):
            dist[i][i] = 0
            for edge in edges:
                dist[i][edge] = 1
                
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        @cache
        def visit (node, visited):
            if visited == (1 << N) - 1:
                return 0
            best = INF
            for i in range(N):
                if ((1 << i) & (visited)) == 0:
                    best = min(best, visit(i, (1 << i) | visited) + dist[node][i])
            return best
        
        best = INF
        for i in range(N):
            best = min(best, visit(i, (1 << i)))
        return best