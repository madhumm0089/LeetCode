class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)  # O(n) space, O(n) time to build
        i = 1
        while True:
            if i not in num_set:
                return i
                break
            i += 1
