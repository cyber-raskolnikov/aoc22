# (A, B, C) (X, Y, Z)
# A : OPPONENT ROCK       X : MY ROCK (1 POINT)
# B : OPPONENT PAPER      Y : MY PAPER (2 POINTS) 
# C : OPPONENT SCISSORS   Z : MY SCISSORS (3 POINTS)

# LOSE : 0 POINTS     DRAW : 3 POINTS     WIN : 6 POINTS

def compute_round_score(round: str) -> int:
    opponent_move: str = round[0]
    my_move: str = round[2]

    return compute_base_score(my_move) + compute_outcome_score(opponent_move, my_move)

def compute_base_score(my_move: str):
    match my_move:
        case 'X': return 1
        case 'Y': return 2
        case 'Z': return 3
        case _: raise Exception("Non-valid move")

def compute_outcome_score(opponent_move, my_move) -> int:
    offset: int = ord('X') - ord('A')
    opponent_move: str = chr(ord(opponent_move) + offset)

    diff = ord(opponent_move) - ord(my_move)
    match diff:
        case (-2|1): return 0
        case 0: return 3
        case (-1|2): return 6

input_file = "./python/2/input/first.txt"

with open(input_file) as file:
    lines = file.read().split('\n')
    print(lines)
    scores = [compute_round_score(line) for line in lines]
    print(scores)
    print(sum(scores))