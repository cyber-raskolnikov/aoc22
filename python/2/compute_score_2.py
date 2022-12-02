# (A, B, C) (X, Y, Z)
# A : OPPONENT ROCK       X : MY ROCK (1 POINT)
# B : OPPONENT PAPER      Y : MY PAPER (2 POINTS) 
# C : OPPONENT SCISSORS   Z : MY SCISSORS (3 POINTS)

# LOSE : 0 POINTS     DRAW : 3 POINTS     WIN : 6 POINTS

def compute_round_score(round: str) -> int:
    opponent_move: str = round[0]
    outcome: str = round[2]

    return compute_outcome_score(outcome) + compute_move_score(guess_move(opponent_move, outcome))

def compute_outcome_score(outcome: str):
    match outcome:
        case 'X': return 0
        case 'Y': return 3
        case 'Z': return 6
        case _: raise Exception("Non-valid outcome")

def compute_move_score(my_moves) -> int:
    score = 0

    match my_moves[0]:
        case 'A': score += 1
        case 'B': score += 2
        case 'C': score += 3
        case _: score += 0
    
    match my_moves[1]:
        case 'A': score += 1
        case 'B': score += 2
        case 'C': score += 3
        case _: score += 0
    
    return score

def guess_move(opponent_move, outcome):
    opponent_move = ord(opponent_move)
    match outcome:
        case 'Z':
            return (chr(opponent_move-2), chr(opponent_move+1))
        case 'Y':
            return (chr(opponent_move), '_')
        case 'X':
            return (chr(opponent_move-1), chr(opponent_move+2))

input_file = "./python/2/input/first.txt"

with open(input_file) as file:
    lines = file.read().split('\n')
    print(lines)
    scores = [compute_round_score(line) for line in lines]
    print(scores)
    print(sum(scores))