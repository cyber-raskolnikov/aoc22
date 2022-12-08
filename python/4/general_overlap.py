import sys
from typing import List, Tuple

def read_pairs() -> List[Tuple[Tuple[int,int],Tuple[int,int]]]:
    return format_pairs(sys.stdin.readlines())

def format_pairs(pairs: List[str]) -> List[Tuple[Tuple[int,int],Tuple[int,int]]]:
    format_pairs = []
    
    for pair in pairs:
        elves_sections = pair.split(',')
        formatted_section = [(int(section_range.split('-')[0]),int(section_range.split('-')[1])) for section_range in elves_sections]
        format_pairs.append(tuple(formatted_section))
    
    return format_pairs

def flag_contained_pairs(pairs: List[Tuple[Tuple[int,int],Tuple[int,int]]]) -> List[bool]:
    return [is_contained(pair) for pair in pairs]

def is_contained(pair: Tuple[Tuple[int,int],Tuple[int,int]]) -> bool:
    if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][0]:
        return True
    elif pair[0][0] >= pair[1][0] and pair[0][0] <= pair[1][1]:
        return True
    return False

pairs = read_pairs()
is_pair_contained = flag_contained_pairs(pairs)
# print(is_pair_contained)
print(sum(is_pair_contained))