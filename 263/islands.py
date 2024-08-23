import itertools


def count_islands(grid):
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

    island_count = 0

    for i in range(0, len(grid)):
        if 1 not in grid[i]:
            continue

        for j in range(0, len(grid[i])):
            if grid[i][j] == 1:
                mark_island(i, j, grid)
                if grid[i][j] == ISLAND_MARKER:
                    island_count += 1

    return island_count


# solution ideas to see if there is even land:
# turn grid into string, see if contains '1'
# link grid together, sum up numbers if 0 then return.
# link grid in chain, 1 in chain then there is land.

# ideas for finding islands:
#     - loop over rows => get find index of value 1, check if has neighbouring land. x + - 1 y + - 1
#     - keep an island counter, mark land found as being part of island. (different number or something) number of the island. (first island) if not part of island mark 0
#     - continue finding 1, repeat till no more un

# definitions:
# island is neighbouring 1,1 or island marker.
# when 1 neighbours a 1 then new island.


# loop over i,j, if find a 1 mark island, if is is_marked then islandcounter ++: return counter.
ISLAND_MARKER = "#"


def neighbouring_land(i, j, grid):
    neighbours = []

    for y in range((i - 1), (i + 1) + 1, 2):

        # prevent out of grid range, index error
        if y < 0 or y > len(grid) - 1:
            continue

        if grid[y][j] == 1:
            neighbours.append((y, j))

    for x in range((j - 1), (j + 1) + 1, 2):
        # prevent out of grid range, index error
        if x < 0 or x > len(grid[i]) - 1:
            continue

        if grid[i][x] == 1:
            neighbours.append((i, x))

    return neighbours


def mark_island(i, j, grid):
    if grid[i][j] == 1:
        # mark current position as island.
        grid[i][j] = ISLAND_MARKER

        # get neigbouring land (part of same island)
        neighbours = neighbouring_land(i, j, grid)

        for neighbour in neighbours:
            mark_island(*neighbour, grid=grid)

        return


def mark_islands(i, j, grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visited islands as in-place operation.
    """

    island_count = 0

    for x in range(i, len(grid)):
        for y in range(j, len(grid[i])):
            if grid[x, y] == 1:
                island_count += 1
                mark_island(x, y, grid)

    return
