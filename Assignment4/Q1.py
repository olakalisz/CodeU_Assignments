def is_not_visited_land(i, j, visited, map_grid):
    rows = len(map_grid)
    columns = len(map_grid[0])
    return 0 <= i < rows and 0 <= j < columns and not visited[i][j] and map_grid[i][j]


def counting_islands(map_grid):
    rows = len(map_grid)
    columns = len(map_grid[0])

    island_count = 0

    visited = [[False for i in range(columns)] for j in range(rows)]

    for i in range(rows):
        for j in range(columns):
            if not visited[i][j] and map_grid[i][j]:
                start = (i, j)
                dfs_explore_island(start, visited, map_grid)
                island_count += 1

    return island_count


def dfs_explore_island(start, visited, map_grid):
    (i, j) = start
    visited[i][j] = True

    rows_adjacent = [-1, 1, 0, 0]
    columns_adjacent = [0, 0, -1, 1]

    for k in range(4):
        adjacent = (i + rows_adjacent[k], j + columns_adjacent[k])
        if is_not_visited_land(adjacent[0], adjacent[1], visited, map_grid):
            dfs_explore_island(adjacent, visited, map_grid)
