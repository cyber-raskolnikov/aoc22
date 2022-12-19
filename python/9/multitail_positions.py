import sys
import copy

ROPE = [[0,0]] * 10

TAIL_REGISTER = []

def move_head(head, direction):
    match direction:
        case 'U': return [head[0]-1, head[1]]
        case 'R': return [head[0], head[1]+1]
        case 'D': return [head[0]+1, head[1]]
        case 'L': return [head[0], head[1]-1]

def check_if_legal_position(head, tail):
    row_condition = abs(head[0] - tail[0]) < 2
    col_condition = abs(head[1] - tail[1]) < 2

    return (row_condition and col_condition)

def correct_tail_position(head, tail):
    row_condition = abs(head[0] - tail[0]) < 2
    col_condition = abs(head[1] - tail[1]) < 2

    if (head[0] - tail[0]) * (head[1] - tail[1]) != 0:
        correction = 1 if (head[0] - tail[0]) > 0 else -1
        tail[0] += correction

        correction = 1 if (head[1] - tail[1]) > 0 else -1
        tail[1] += correction

    elif not row_condition:
        correction = 1 if (head[0] - tail[0]) > 0 else -1
        tail[0] += correction
    
    elif not col_condition:
        correction = 1 if (head[1] - tail[1]) > 0 else -1
        tail[1] += correction
    
    return tail

for line in sys.stdin.readlines():
    direction = line.rstrip().split(' ')[0]
    times = int(line.rstrip().split(' ')[1])

    print(f"move {direction} {times} times")

    for _ in range(times):
        for i in range(9):
            print(ROPE)
            print(f"USING NODE {i} {ROPE[i]} AS HEAD")
            HEAD = copy.deepcopy(ROPE[i])
            TAIL = copy.deepcopy(ROPE[i+1])

            if i == 0:
                HEAD = move_head(HEAD, direction)

            LEGAL_POSITION = check_if_legal_position(HEAD, TAIL)
        
            if not LEGAL_POSITION:
                if i == 8:
                    print("MOVING REAL TAIL")
                elif i > 1:
                    print(f"Moving NODE n{i+1}")
                print(f"Illegal position! H{i}: {HEAD} T{i+1}: {TAIL}")
                TAIL = correct_tail_position(HEAD, TAIL)
                print(f"Tail corrected: {TAIL}")

            ROPE[i] = HEAD
            ROPE[i+1] = TAIL
    
        # regardless of corrected or not
        TAIL_REGISTER.append(tuple(ROPE[9]))

#print(TAIL_REGISTER)
print(len(set(TAIL_REGISTER)))