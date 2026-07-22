class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g=defaultdict(list)
        course=prerequisites
        for a,b in course:
            g[a].append(b)
        visiting=1
        visited=2
        unvisited=0
        states=[unvisited]*numCourses
        order=[]
        def dfs(node):
            state=states[node]
            if state==visited:
                return True
            elif state==visiting:
                return False
            states[node]=visiting
            for nei in g[node]:
                if not dfs(nei):
                    return False
            states[node]=visited
            order.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return[]
        return order                    

        
