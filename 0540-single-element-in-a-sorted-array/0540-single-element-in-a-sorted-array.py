class Solution:
    def singleNonDuplicate(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # mid ko even index banate hain
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                # Pair correct hai, single element right mein hai
                left = mid + 2
            else:
                # Pair break ho gaya, single element left mein hai
                right = mid

        return nums[left]        