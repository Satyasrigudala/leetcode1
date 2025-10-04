class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        valid = set(range(1, n+1))   # {1, 2, ..., n}

        # Check rows
        for row in matrix:
            if set(row) != valid:
                return False

        # Check columns
        for col in zip(*matrix):  # transpose
            if set(col) != valid:
                return False

        return True
        
