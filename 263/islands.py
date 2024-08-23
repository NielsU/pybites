def count_islands(grid: list[list]) -> int:
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continuously
        connected vertically or horizontally  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    # islands = 0         # var. for the counts
    # .....some operations.....
    # mark_islands(r, c, grid)
    # return islands

    islands = 0

    def island_gen(grid: list[list]):
        for i in range(0, len(grid)):
            while True:
                try:
                    yield (i, grid[i].index(1))  # next island position in grid.
                except ValueError:
                    break

    for island in island_gen(grid):
        islands += 1
        mark_island(*island, grid)

    return islands


def is_new_land(i: int, j: int, grid: list[list]) -> bool:
    """New land is any unmarked (is)land"""

    # prevent postion out of grid range, index error
    if i < 0 or i > len(grid) - 1:
        return False

    # prevent postion out of grid range, index error
    if j < 0 or j > len(grid[i]) - 1:
        return False

    return grid[i][j] == 1


def neighbouring_land(i: int, j: int, grid: list[list]) -> list[tuple]:
    """retuns the positions of adjecent unmarked/new land"""
    neighbours = []

    # check prev/next row (above/below current position)
    for y in range((i - 1), (i + 1) + 1, 2):
        if is_new_land(y, j, grid):
            neighbours.append((y, j))

    # check prev next position in same row
    for x in range((j - 1), (j + 1) + 1, 2):
        if is_new_land(i, x, grid):
            neighbours.append((i, x))

    return neighbours


def mark_island(i: int, j: int, grid: list[list]) -> None:
    """Mark an entire island starting from given i,j postion in grid"""
    ISLAND_MARKER = "#"

    # mark current position as island.
    grid[i][j] = ISLAND_MARKER

    # get postitions of neighbouring land which are not yet marked.
    neighbours = neighbouring_land(i, j, grid)

    for neighbour in neighbours:
        mark_island(*neighbour, grid=grid)

    return
