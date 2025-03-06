class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        dict_grid: dict = {}
        list_numbers = list(range(1, len(grid)**2 + 1))
        a_b: list = [0, 0]
        for i in grid:
            for j in i:
                dict_grid[j] = dict_grid.get(j, 0) + 1
        for i in list_numbers:
            if i not in dict_grid.keys(): a_b[1] = i
            elif dict_grid[i] == 2: a_b[0] = i
        return a_b