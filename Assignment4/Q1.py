# coding=utf-8
"""The approach taken in this solution is based on DFS search and is very similar to searching for connecting
   components of the graph. We visit every tile of the given map grid and if the land tile is found we
   perform a DFS search from it (with 'edges' between every two adjacent land tiles) to find the whole island.
   Once DFS search is finished the island counter is incremented. Every visited tile is marked as visited so
   we visit each tile just once. The running time of the given solution is θ(NXM), where N is the number of rows
   in a map grid and M is the number of columns."""

# An array to keep track of adjacent entries in a map grid.
_ADJACENT_DELTAS = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def is_not_visited_land(i, j, visited, map_grid):
    """The method checks if a map entry (tile) with coordinates (i,j) is contained in a gird, is not yet visited and
       is a land tile.

        Args:
            i: an integer, first coordinate of an entry (tile)
            j: an integer, second coordinate of an entry (tile)
            visited: a 2D boolean array, indicates which entries (tiles) has already been visited
            map_grid: a 2D boolean array, corresponds to the map grid, indicates with True the land tiles and
                      water tiles with False

        Returns:
            a boolean, True if an entry is in a grid, has not been visited yet and is a land tile.
    """
    rows = len(map_grid)
    columns = len(map_grid[0])
    return 0 <= i < rows and 0 <= j < columns and not visited[i][j] and map_grid[i][j]


def counting_islands(map_grid):
    """The method counts the number of islands in a given map grid.

        Args:
            map_grid: a 2D boolean array, corresponds to the map grid, indicates with True the land tiles and
                      water tiles with False

        Returns:
            an integer, the number of islands in a given map grid.
    """
    # Get the number of rows and columns in in a grid.
    rows = len(map_grid)
    columns = len(map_grid[0])

    # Instantiate the number of islands to 0.
    island_count = 0

    # Instantiate a 2D boolean array 'visited' corresponding to the map grid to all False entries. It will indicate
    # what tiles has been already visited by the search.
    visited = [[False for i in range(columns)] for j in range(rows)]

    # Iterate through all map grid tiles and perform a DFS 'island' search whenever a land tile is found.
    for i in range(rows):
        for j in range(columns):
            if not visited[i][j] and map_grid[i][j]:
                start = (i, j)
                dfs_explore_island(start, visited, map_grid)
                island_count += 1

    # Return the number of islands.
    return island_count


def dfs_explore_island(start, visited, map_grid):
    """The method performs a DFS 'island' search to mark all the land tiles reachable from the start tile as
       visited.

        Args:
            start: a pair of integers, coordinates of the entry (tile) from which DFS starts
            visited: a 2D boolean array, indicates which entries (tiles) has already been visited, the method
                     modified this array marking all reachable land tiles from start tile as visited
            map_grid: a 2D boolean array, corresponds to the map grid, indicates with True the land tiles and
                      water tiles with False
    """
    # Get the coordinates of the starting entry (tile).
    (i, j) = start

    # Mark the start entry (tile) as visited.
    visited[i][j] = True

    # DFS recursive call - find all land tiles reachable from the start entry (tile). 'Explore' the whole island
    # by iterating though all adjacent entries (tiles).
    for (row_delta, column_delta) in _ADJACENT_DELTAS:
        # Get the coordinates of an adjacent entry (tile).
        adjacent = (i + row_delta, j + column_delta)
        if is_not_visited_land(adjacent[0], adjacent[1], visited, map_grid):
            dfs_explore_island(adjacent, visited, map_grid)
