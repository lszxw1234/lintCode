class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if len(A) <= 1:
            return len(A)
        i = len(A)-1
        while i >=0:
            if A[i] == A[i-1]:
                del A[i]
            i -=1
        return len(A)
