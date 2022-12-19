import sys
import numpy as np

treetops = sys.stdin.read().splitlines()
treetops = [list(row) for row in treetops]
treetops = np.array(treetops)

GRID_SIDE = len(treetops)

VISIBLE_TREES = []

# reading direction
for i in range(0,GRID_SIDE,1):
    CACHE_HEIGHT = '!' # as its ordinal value is lower than digits
    for j in range(0,GRID_SIDE,1):
        #print(f"Position {i},{j} : {treetops[i][j]}")
        if treetops[i][j] > CACHE_HEIGHT:
            CACHE_HEIGHT = treetops[i][j]
            position = f"{i}:{j}->{CACHE_HEIGHT}"
            VISIBLE_TREES.append(position)

# arabic reading
for i in range(0,GRID_SIDE,1):
    CACHE_HEIGHT = '!' # as its ordinal value is lower than digits
    for j in range(GRID_SIDE-1,-1,-1):
        if treetops[i][j] > CACHE_HEIGHT:
            CACHE_HEIGHT = treetops[i][j]
            position = f"{i}:{j}->{CACHE_HEIGHT}"
            VISIBLE_TREES.append(position)

for j in range(0,GRID_SIDE,1):
    CACHE_HEIGHT = '!' # as its ordinal value is lower than digits
    for i in range(0,GRID_SIDE,1):
        #print(f"Position {i},{j} : {treetops[i][j]}")
        if treetops[i][j] > CACHE_HEIGHT:
            CACHE_HEIGHT = treetops[i][j]
            position = f"{i}:{j}->{CACHE_HEIGHT}"
            VISIBLE_TREES.append(position)

for j in range(0,GRID_SIDE,1):
    CACHE_HEIGHT = '!' # as its ordinal value is lower than digits
    for i in range(GRID_SIDE-1,-1,-1):
        if treetops[i][j] > CACHE_HEIGHT:
            CACHE_HEIGHT = treetops[i][j]
            position = f"{i}:{j}->{CACHE_HEIGHT}"
            VISIBLE_TREES.append(position)



print(set(VISIBLE_TREES))
print(len(set(VISIBLE_TREES)))


