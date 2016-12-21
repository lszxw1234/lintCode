class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        i, j = 0,0
        ret = []
        while i < len(A) and j < len(B):    
            print (ret,i,j)
            if A[i] >B[j]:
                ret.append(B[j])
                j += 1
            else:
                ret.append(A[i])
                i += 1
        print (i,j)
        while i < len(A):
            ret.append(A[i])
            i += 1
        while j < len(B):
            ret.append(B[j])
            j += 1
        return ret
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        i, j = 0,0
        ret = []
        while i < m and j < n:    
            if A[i] >B[j]:
                ret.append(B[j])
                j += 1
            else:
                ret.append(A[i])
                i += 1
        while i < m:
            ret.append(A[i])
            i += 1
        while j < n:
            ret.append(B[j])
            j += 1
        return ret
    
print(Solution().mergeSortedArray([1,2,3], 3, [4,5], 2))
