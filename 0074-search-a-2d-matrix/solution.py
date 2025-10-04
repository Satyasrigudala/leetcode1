class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        n=rows*cols
        beg=0
        end=n-1
        while beg<=end:
            mid=(beg+end)//2
            i=mid//cols
            j=mid%cols
            if matrix[i][j]==target:
                return True
            elif target<matrix[i][j]:
                end=mid-1
            else:
                beg=mid+1
        return False            
