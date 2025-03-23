class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        more = []
        same = []


        for i in nums:
            if i > pivot:
                more.append(i)
            elif i < pivot:
                less.append(i)
            else:
                same.append(i)

        return less + same + more