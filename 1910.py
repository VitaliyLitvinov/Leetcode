class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        lst_part: list = list(part)
        coeff: int = len(part)
        lst: list = list(s)
        while ''.join(lst_part) in ''.join(lst):
            for idx in range(len(lst)):
                if lst[idx:idx + coeff] == lst_part:
                    del lst[idx:idx + coeff]
                    break
        return(''.join(lst))

