class Solution:

    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype sum: int
        """
        nums.sort()
        sum = 0
        first = 0
        while first < len(nums)-1:
            sum += min(nums[first], nums[first+1])
            first += 2

        return sum

sol = Solution()
print(sol.arrayPairSum([1,3,5,7]))