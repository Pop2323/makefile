#!/usr/bin/python3
"""returns the perimeter of the island described in grid:"""
def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                res += 4
                if i > 0 and grid[i - 1][j] == 1:
                    res -= 2
                if i > 0 and grid[i][j - 1] == 1:
                    res -= 2
    return res


# grid = [
#         [0, 0, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0],
#         [0, 1, 1, 1, 0, 0],
#         [0, 0, 0, 0, 0, 0]
#     ]
# print(island_perimeter(grid))