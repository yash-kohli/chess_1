def check(pieces, firsttap, from_x, from_y, to_x, to_y):
    # Universal False
    final_pos = pieces[to_x][to_y]
    first_char = final_pos[0]

    if (firsttap[0] == first_char):
        return False

    # pawn_rules

    final_pos = pieces[to_x][to_y]
    first_char = final_pos[0]
    if (firsttap == "wp" and first_char != "w"):
        if (to_y != from_y and pieces[to_x][to_y] == "-"):
            return False
        if (from_x == 6):
            if (to_x == 4 and to_y == from_y):
                return True
        if (to_x == (from_x - 1) and (abs(to_y - from_y) == 0 or abs(to_y - from_y) == 1)):
            return True
    if (firsttap == "bp" and first_char != "b"):
        if (to_y != from_y and pieces[to_x][to_y] == "-"):
            return False
        if (from_x == 1):
            if (to_x == 3 and to_y == from_y):
                return True
        if (to_x == (from_x + 1) and (abs(to_y - from_y) == 0 or abs(to_y - from_y) == 1)):
            return True
    #knight rules
            # knight
    if firsttap == "bh" or firsttap == "wh":
            print("knight move")
            x1 = from_x + 1
            y1 = from_y + 2
            if (x1 == to_x and y1 == to_y):
                return True
            x2 = from_x + 1
            y2 = from_y - 2
            if (x2 == to_x and y2 == to_y):
                return True
            x3 = from_x - 2
            y3 = from_y + 1
            if (x3 == to_x and y3 == to_y):
                return True
            x4 = from_x - 2
            y4 = from_y - 1
            if (x4 == to_x and y4 == to_y):
                return True
            x5 = from_x + 2
            y5 = from_y + 1
            if (x5 == to_x and y5 == to_y):
                return True
            x6 = from_x + 2
            y6 = from_y - 1
            if (x6 == to_x and y6 == to_y):
                return True
            x7 = from_x - 1
            y7 = from_y + 2
            if (x7 == to_x and y7 == to_y):
                return True
            x8 = from_x - 1
            y8 = from_y - 2
            if (x8 == to_x and y8 == to_y):
                return True
            else:
                return False

