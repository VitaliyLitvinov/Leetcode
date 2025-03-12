class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n: int = len(nums)
        neg: int = 0
        pos: int = 0
        for num in nums:
            if num < 0: neg += 1
            elif num > 0: pos += 1
        return max(neg, pos)