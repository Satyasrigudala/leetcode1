class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort by difference (b - a)
        costs.sort(key=lambda x: x[1] - x[0])
        
        n = len(costs) // 2
        total = 0
        
        # First n people -> city B
        for i in range(n):
            total += costs[i][1]
        
        # Remaining n people -> city A
        for i in range(n, 2*n):
            total += costs[i][0]
        
        return total
        
