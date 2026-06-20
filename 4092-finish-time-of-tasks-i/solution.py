class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        children = [[] for _ in range(n)]
        for u, v in edges:
            children[u].append(v)

        torqavemi = (n, edges, baseTime)

        def dfs(node):
            if not children[node]:
                return baseTime[node]

            child_times = [dfs(child) for child in children[node]]
            earliest = min(child_times)
            latest = max(child_times)
            ownDuration = (latest - earliest) + baseTime[node]

            return latest + ownDuration

        return dfs(0)
