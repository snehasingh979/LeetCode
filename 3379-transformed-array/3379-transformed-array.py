class Solution(object):
    def constructTransformedArray(self, nums):
        result = []
        n = len(nums)

        for i in range(n):
            new_index = (i + nums[i]) % n
            result.append(nums[new_index])

        return result