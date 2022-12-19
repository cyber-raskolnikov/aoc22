# The scenic score of a tree is the product of the scenic score of its 4 sides

import sys
import numpy as np

treetops = sys.stdin.read().splitlines()
treetops = [list(row) for row in treetops]
treetops = np.array(treetops, int)

SCORES = np.ones_like(treetops)

GRID_SIDE = len(treetops)

for _ in range(4):

    for i in range(0, GRID_SIDE):

        for j in range(0, GRID_SIDE):
            current_value = treetops[i][j]
            SCENIC_SCORE = 0

            for z in range(j-1, -1, -1):
                SCENIC_SCORE += 1
                if (previous_value := treetops[i][z]) >= current_value:
                    break
            
            SCORES[i][j] *= SCENIC_SCORE
    
    # not relevant here as looking at all edges
    # but this spins counterclockwise (right-hand rule)
    treetops = np.rot90(treetops)
    SCORES = np.rot90(SCORES)

print(treetops, SCORES, SCORES.max(), sep='\n'*3)