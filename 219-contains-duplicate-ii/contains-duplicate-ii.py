class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n= len(nums)
        seen = set()
        for i in range(n):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            if len(seen) > k:
                seen.remove(nums[i - k])
        return False
