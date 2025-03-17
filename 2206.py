class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        digits: list = []
        for i in nums:
            if i in digits:
                digits.remove(i)
            else:
                digits.append(i)
        return len(digits) == 0
