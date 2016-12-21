class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                mynums = nums[i:j+1]
                sum = 0
                for num in mynums:
                    sum += num
                if sum == 0:
                    return [i,j]



print(Solution().subarraySum([1,-1]))
