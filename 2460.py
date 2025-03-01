class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]: nums[i] *= 2; nums[i + 1] = 0
        zero_end = [0] * len(nums)
        count = 0
        for j in range(len(nums)):
            if nums[j]: zero_end[count] = nums[j]; count += 1
        return zero_end

