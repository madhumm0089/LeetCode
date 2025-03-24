from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_count_element = 0
        max_count = 0
        for key, value in counter.items():
            if value > max_count:
                max_count = value
                max_count_element = key

        return max_count_element
        