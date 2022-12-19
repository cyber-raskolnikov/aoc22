# A tree is visible if it can be seen from ANY of the 4 edges of the grid
# The concept of matrix notation applies well to the grid transformations needed here

# Rotating both the grid AND the results grid results in
# not needing to deal with i,j index arithmetic

import sys
import numpy as np

treetops = sys.stdin.read().splitlines()
treetops = [list(row) for row in treetops]
treetops = np.array(treetops, int)

visibility = np.zeros_like(treetops)

GRID_SIDE = len(treetops)

for _ in range(4):

    for i in range(0, GRID_SIDE):
        HEIGHT_CACHE = -1

        for j in range(0, GRID_SIDE):
            if treetops[i][j] > HEIGHT_CACHE:
                HEIGHT_CACHE = treetops[i][j] # marking as tallest seen in row
                visibility[i][j] = 1 # marking as visible by at least an edge
    
    # not relevant here as looking at all edges
    # but this spins counterclockwise (right-hand rule)
    treetops = np.rot90(treetops)
    visibility = np.rot90(visibility)

print(treetops, visibility, visibility.sum(), sep='\n'*3)

