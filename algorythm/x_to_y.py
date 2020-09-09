def x_to_y(x, y):
    count = 0
    while x != y:
        ytemp = y
        while (x < ytemp):
            ytemp = ytemp / 2
        if x < ytemp + 1:
            f_x = x
            x = x * 2
            print(f"{f_x}*2 = {x}")
        else:
            f_x = x
            x = x - 1
            print(f"{f_x}-1 = {x}")
        count += 1

    print(count)


x_to_y(5,11)
