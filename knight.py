def knight(pieces, firsttap, from_x, from_y, to_x, to_y)
    x1=from_x+1
    y1=from_y+2
    if(x1 == to_x and y1 == to_y)
        return true
    x2=from_x+1
    y2=from_y-2
    if( x2==to_x and y2 == to_y)
        return true
    x3=from_x-2
    y3=from_y+1
    if( x3==to_x and y3 == to_y)
        return true
    x4=from_x-2
    y4=from_y-1
    if(x4 == to_x and y4 == to_y)
        return true
    x5=from_x+2
    y5=from_y+1
    if(x5 == to_x and y5 == to_y)
        return true
    x6=from_x+2
    y6=from_y-1
    if(x6 == to_x and y6 == to_y)
        return true
    x7=from_x-1
    y7=from_y+2
    if(x7 == to_x and y7 == to_y)
        return true
    x8=from_x-1
    y8=from_y-2
    if(x8 == to_x and y8== to_y)
        return true
    else
        return false
