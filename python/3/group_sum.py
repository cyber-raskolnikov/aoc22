import sys
from typing import List, Tuple

GROUP_SIZE = 3

def read_group_backpacks() -> List[Tuple[str]]:
    lines = sys.stdin.read().splitlines()
    num_lines = len(lines)
    assert (num_lines%3 == 0)

    groups = [tuple(lines[slice_start:slice_start+GROUP_SIZE]) for slice_start in range(0,num_lines,GROUP_SIZE)]

    # print(groups)
    return groups

def find_shared_items(backpacks: List[Tuple[str]]) -> List[str]:
    return [list(set(backpack[0]).intersection(backpack[1]).intersection(backpack[2])) for backpack in backpacks]

def transform_to_priorities(items: List[str]) -> List[int]:
    priorities: List[int] = []

    for item in items:
        ordinal = ord(item[0])

        if ordinal >= 97: # minus case
            priority = ordinal - ord('a') + 1
        else: # mayus case
            priority = ordinal - ord('A') + 27
        
        priorities.append(priority)
    return priorities

groups = read_group_backpacks()
shared_items = find_shared_items(groups)
priorities = transform_to_priorities(shared_items)

print(sum(priorities))