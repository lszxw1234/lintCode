class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        #if A[i] == B[j], the length for substring is c[i-1][j-1] +1
        ret = 0
        cache = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
        index = 0
        for i in range(1,len(A) + 1):
            for j in range(1, len(B) + 1):
                cache[i][j] = cache[i - 1][j - 1] + 1 if A[i - 1] == B[j - 1] else 0
                #ret = max(cache[i][j],ret)
                if cache[i][j] > ret:
                    index = i
                    ret = cache[i][j]
        return ret,A[index - ret:index]


A = "testforABC"
B = 'testsforABCD'


print (Solution().longestCommonSubstring(A,B))
