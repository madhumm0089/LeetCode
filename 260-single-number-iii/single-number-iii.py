class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        single_ele_list = []
        nums_dict = Counter(nums)  # Creates a dictionary-like object with counts of each number
        for key, value in nums_dict.items():  # Iterate through each number and its count
            if value == 1:  # Check if the count is 1 (unique number)
                single_ele_list.append(key)

        return single_ele_list