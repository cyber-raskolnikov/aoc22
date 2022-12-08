import sys
from typing import List, Tuple

def read_backpacks() -> List[Tuple[str,str]]:
    lines = sys.stdin.read().splitlines()

    backpacks = []
    for backpack in lines:
        assert (len(backpack)%2 == 0)

        comparment_size = len(backpack)//2
        # print(f"Reading backpack with two {comparment_size}-sized compartments")
        
        backpack = (backpack[:comparment_size], backpack[comparment_size:])
        backpacks.append(backpack)

    # print(backpacks)
    return backpacks

def find_shared_items(backpacks: List[Tuple[str,str]]) -> List[str]:
    return [list(set(backpack[0]).intersection(backpack[1])) for backpack in backpacks]

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

backpacks = read_backpacks()
shared_items = find_shared_items(backpacks)
priorities = transform_to_priorities(shared_items)

print(sum(priorities))