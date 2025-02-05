class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff: int = 0
        left = right = -1
        for idx in range(len(s1)):
            if s1[idx] != s2[idx]:
                diff += 1
                if left == -1: left = idx
                else: right = idx
        if diff == 0: return True
        elif diff != 2: return False
        return (s1[left] == s2[right]) and (s1[right] == s2[left])