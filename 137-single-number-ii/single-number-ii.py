class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_dict = Counter(nums)  # Creates a dictionary-like object with counts of each number
        for key, value in nums_dict.items():  # Iterate through each number and its count
            if value == 1:  # Check if the count is 1 (unique number)
                return key