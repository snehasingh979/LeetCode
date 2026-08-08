class Solution:

    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            from collections import Counter

            count = Counter(nums)
            ans = 0

            for num in count:
                if count[num] >= 2:
                    ans += 1

            return ans

        num_set = set(nums)
        ans = 0

        for num in num_set:
            if num + k in num_set:
                ans += 1

        return ans        