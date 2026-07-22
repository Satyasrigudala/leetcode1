class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q=deque(students)
        count=0
        while q and count < len(q):
            if q[0] == sandwiches[0]:
                q.popleft()
                sandwiches.pop(0)
                count = 0         
            else:
                student = q.popleft()
                q.append(student)  
                count += 1         
        return len(q)

        
