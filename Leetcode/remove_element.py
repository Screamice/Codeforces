class Solution:

    def removeElement(self, A, elem):
        front, back = 0, 0
        while front < len(A):
            if A[front] != elem:
                # Not to be removed
                A[back] = A[front]
                back += 1
            front += 1
        return back
        
sol = Solution()
print(sol.removeElement([0,1,2,2,3,0,4,2], 2))