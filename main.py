from random import randint
from pprint import pprint
from itertools import product

def make_table(corners):

    table = [
        [0 for x in range(9)]
        for y in range(9)
    ]   

    left_bound = 0
    right_bound = 8
    bot_bound = 8
    top_bound = 0

    # corners = [0, 2, 3, 0, 0, 1, 2]

    for i in range(8,-1,-1):
        if i > 0:
            corner = corners[7-i]
        else:
            table[top_bound][left_bound] = 1
            continue

        if corner == 0: # TL corner
            for x in range(i+1):
                table[top_bound][left_bound+x] = i+1

            for y in range(i+1):
                table[top_bound+y][left_bound] = i+1

            left_bound += 1
            top_bound += 1
        elif corner == 1: # TR corner
            for x in range(i+1):
                table[top_bound][left_bound+x] = i+1

            for y in range(i+1):
                table[top_bound+y][right_bound] = i+1

            right_bound -= 1
            top_bound += 1
        elif corner == 2: # BL corner
            for x in range(i+1):
                table[bot_bound][left_bound+x] = i+1

            for y in range(i+1):
                table[top_bound+y][left_bound] = i+1

            left_bound += 1
            bot_bound -= 1
        elif corner == 3: # BR corner
            for x in range(i+1):
                table[bot_bound][left_bound+x] = i+1

            for y in range(i+1):
                table[top_bound+y][right_bound] = i+1

            right_bound -= 1
            bot_bound -= 1
    
    # pprint(table)
    return table




# check constraint

# direction = 0 # from: top, right, bot, left
# n = 0   # which row/col (absolute, not relative)
# target = 41

constraints = [

    (0,0,41),
    (0,1,8),
    (0,4,14),
    (0,6,15),

    (3,2,25),
    (3,4,15),
    (3,6,26),


    (0,1,9),
    (0,3,17),
    (0,5,15),
    (0,7,35),

    (1,0,25),
    (1,4,10),
    (1,8,27),


]

def test_table(table, direction, n, target):
    for width in range(9):
        if direction == 0:
            for start in range(9-width):
                end = start + width

                total_try = 0
                for x in range(start, end+1):
                    total_try += table[x][n]
                    if target - total_try == 0:
                        return True
                    if target - total_try < 0:
                        return False
        elif direction == 3:
            for start in range(9-width):
                end = start + width

                total_try = 0
                for x in range(start, end+1):
                    total_try += table[n][x]
                    if target - total_try == 0:
                        return True
                    if target - total_try < 0:
                        return False


# table = make_table([0, 2, 3, 0, 0, 1, 2, 0])

for rotation_code in product([0,1,2,3], repeat=7):
    table = make_table(rotation_code)



    # print(*rotation_code)
    
    x = True
    for i in range(7):
        x &= test_table(table, *(constraints[i]))
        if not x:
            break
    if x:
        print(*rotation_code)
        # pprint(table)
        # input()


