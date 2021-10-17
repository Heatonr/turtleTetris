import turtle
import random
import datetime

pen = turtle.Turtle()
screen = turtle.Screen()
frames = 0
start = datetime.datetime.now()
move = 0
drop = 0

pen.hideturtle()
pen.speed(0)
turtle.update()

screen.tracer(0,0)

class Tetromino:
    blocks = []
    xPos = 0
    yPos = 0
    color = ""


def create_i_block():
    l_block = Tetromino()
    l_block.blocks = [
        [None, None, None, None],
        [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()],
        [None, None, None, None],
        [None, None, None, None]
    ]
    l_block.color = "cyan"

    l_block.xPos = 4
    l_block.yPos = 0

    return l_block

def create_j_block():
    l_block = Tetromino()
    l_block.blocks = [
        [None, None, turtle.Turtle()],
        [turtle.Turtle(), turtle.Turtle(), turtle.Turtle()],
        [None, None, None],
    ]
    l_block.color = "blue"

    l_block.xPos = 4
    l_block.yPos = 0

    return l_block

def create_l_block():
    l_block = Tetromino()
    l_block.blocks = [
        [turtle.Turtle(), None, None],
        [turtle.Turtle(), turtle.Turtle(), turtle.Turtle()],
        [None, None, None],
    ]
    l_block.color = "orange"

    l_block.xPos = 4
    l_block.yPos = 0

    return l_block

def create_o_block():
    l_block = Tetromino()
    l_block.blocks = [
        [turtle.Turtle(), turtle.Turtle()],
        [turtle.Turtle(), turtle.Turtle()],
    ]
    l_block.color = "yellow"

    l_block.xPos = 4
    l_block.yPos = 0

    return l_block

def create_s_block():
    l_block = Tetromino()
    l_block.blocks = [
        [ None, turtle.Turtle(), turtle.Turtle()],
        [turtle.Turtle(), turtle.Turtle(), None],
        [None, None, None],
    ]
    l_block.color = "green"

    l_block.xPos = 4
    l_block.yPos = 0

    return l_block

def create_t_block():
    l_block = Tetromino()
    l_block.blocks = [
        [ None, turtle.Turtle(), None],
        [turtle.Turtle(), turtle.Turtle(), turtle.Turtle()],
        [None, None, None],
    ]
    l_block.color = "purple"

    l_block.xPos = 4
    l_block.yPos = 0

    return l_block

def create_z_block():
    l_block = Tetromino()
    l_block.blocks = [
        [ turtle.Turtle(), turtle.Turtle(), None],
        [None, turtle.Turtle(), turtle.Turtle()],
        [None, None, None],
    ]
    l_block.color = "red"

    l_block.xPos = 4
    l_block.yPos = 0

    return l_block

def create_random_block():
    rand_num = random.randint(1, 7)
    if rand_num == 1:
        return create_i_block()
    if rand_num == 2:
        return create_j_block()
    if rand_num == 3:
        return create_l_block()
    if rand_num == 4:
        return create_o_block()
    if rand_num == 5:
        return create_s_block()
    if rand_num == 6:
        return create_z_block()
    if rand_num == 7:
        return create_t_block()

def move_left():
    global move
    move = 1

def move_right():
    global move
    move = 2

def rotate_cw():
    global move
    move = 3

def rotate_ccw():
    global move
    move = 4

def do_drop():
    global drop
    drop = 1


screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(do_drop, "s")
screen.onkey(rotate_ccw, "q")
screen.onkey(rotate_cw, "e")
screen.listen()

grid = [
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None]
]


for i in range(-6, 5):
    pen.penup()
    pen.goto(i * 30, 300)
    pen.pendown()
    pen.goto(i * 30, -300)

for i in range(-10, 11):
    pen.penup()
    pen.goto(120, i * 30)
    pen.pendown()
    pen.goto(-180, i * 30)



previousY = 0
previousX = 0


new_game = True

while(True):

    make_new_block = False

    if (((datetime.datetime.now() - start) * 4).seconds > frames):

        if(drop == True):
            while(drop == True):
                for y, item in enumerate(tetris_block.blocks):
                    for x, block in enumerate(item):
                        if (tetris_block.yPos + y < 19 and block != None):

                            temp_block = grid[tetris_block.yPos + y + 1][tetris_block.xPos + x]
                            if temp_block != None:
                                make_new_block = True
                            for row in tetris_block.blocks:
                                if temp_block in row:
                                    make_new_block = False
                            if (make_new_block == True):
                                drop = False
                                break
                        elif(tetris_block.yPos + y >= 19):
                            drop = False
                            break
                if(drop == True):
                    tetris_block.yPos += 1

                previousY = tetris_block.yPos - 1
                previousX = tetris_block.xPos

                i = len(tetris_block.blocks) - 1
                while (i >= 0):
                    j = len(tetris_block.blocks[i]) - 1
                    while (j >= 0):
                        if (isinstance(tetris_block.blocks[i][j], turtle.Turtle)):
                            tetris_block.blocks[i][j].penup()
                            tetris_block.blocks[i][j].shape("square")
                            tetris_block.blocks[i][j].color(tetris_block.color)
                            tetris_block.blocks[i][j].turtlesize = 1000
                            tetris_block.blocks[i][j].shapesize(1.5)
                            tetris_block.blocks[i][j].goto((j * 30) - 165 + (tetris_block.xPos * 30),
                                                           (i * -30) + 285 - (tetris_block.yPos * 30))
                            screen.update()

                            grid[tetris_block.yPos + i][tetris_block.xPos + j] = tetris_block.blocks[i][j]

                            if (previousY != None and previousX != None and make_new_block == False):
                                grid[previousY + i][previousX + j] = None
                        j -= 1
                    i -= 1

        else:
            for y, item in enumerate(tetris_block.blocks):
                for x, block in enumerate(item):
                    if(tetris_block.yPos + y < 19 and block != None):
                        temp_block = grid[tetris_block.yPos + y + 1][tetris_block.xPos + x]
                        if temp_block != None:
                            make_new_block = True
                        for row in tetris_block.blocks:
                            if temp_block in row:
                                make_new_block = False
                        if(make_new_block == True):
                            break
                        if(move == 1):
                            if(tetris_block.xPos + x == 0):
                                move = 0
                                break
                            temp_block = grid[tetris_block.yPos + y][tetris_block.xPos + x - 1]

                            if(temp_block != None):
                                move = 0

                            for row in tetris_block.blocks:
                                if temp_block in row:
                                    move = 1

                            if (move == 0):
                                break
                        if(move == 2):
                            if(tetris_block.xPos + x == 9):
                                move = 0
                                break
                            temp_block = grid[tetris_block.yPos + y][tetris_block.xPos + x - 1]

                            if(temp_block != None):
                                move = 0

                            for row in tetris_block.blocks:
                                if temp_block in row:
                                    move = 2


                            if(move == 0):
                                break

                if (make_new_block == True):
                    break
        for y2, item in enumerate(tetris_block.blocks):
            for x2, block in enumerate(item):
                if (tetris_block.yPos + y2 > 20):
                    break
        previousY = tetris_block.yPos
        previousX = tetris_block.xPos

        tetris_block.yPos += 1
        if(move == 1):
            tetris_block.xPos -= 1
            move = 0
        if(move == 2):
            tetris_block.xPos += 1
            move = 0
        if(move == 3):

            for i, row in enumerate(tetris_block.blocks):
                for j, block in enumerate(row):
                    if(not block == None):
                        grid[tetris_block.yPos + i - 1][tetris_block.xPos + j] = None

            tetris_block.blocks = list(zip(*tetris_block.blocks[::-1]))
            move = 0

            i = len(tetris_block.blocks) - 1
            """"
            while (i >= 0):
                j = len(tetris_block.blocks[i]) - 1
                while (j >= 0):
                    if (isinstance(tetris_block.blocks[i][j], turtle.Turtle)):

                        if (previousY != None and previousX != None and make_new_block == False):
                            grid[previousY + i][previousX + j] = None
                        grid[tetris_block.yPos + i][tetris_block.xPos + j] = tetris_block.blocks[i][j]
                    j -= 1
                i -= 1
                """
        if(move == 4):
            for i, row in enumerate(tetris_block.blocks):
                for j, block in enumerate(row):
                    if(not block == None):
                        grid[tetris_block.yPos + i - 1][tetris_block.xPos + j] = None

            tetris_block.blocks = list(zip(*tetris_block.blocks[::-1]))
            tetris_block.blocks = list(zip(*tetris_block.blocks[::-1]))
            tetris_block.blocks = list(zip(*tetris_block.blocks[::-1]))
            move = 0
            i = len(tetris_block.blocks) - 1
            """
            while (i >= 0):
                j = len(tetris_block.blocks[i]) - 1
                while (j >= 0):
                    if (isinstance(tetris_block.blocks[i][j], turtle.Turtle)):

                        if (previousY != None and previousX != None and make_new_block == False):
                            grid[previousY + i][previousX + j] = None
                        grid[tetris_block.yPos + i][tetris_block.xPos + j] = tetris_block.blocks[i][j]
                    j -= 1
                i -= 1
                """
        for index, row in enumerate(tetris_block.blocks):
            for block in row:
                if (tetris_block.yPos + index == 20 and not block == None):
                    make_new_block = True

        frames += 1

    if(make_new_block == True):
        tetris_block = create_random_block()

        is_empty = 0
        for i, row in enumerate(grid):
            is_empty = 0
            for block in row:
                if block == None:
                    is_empty = 1
            if not is_empty:
                for j, block in enumerate(row):
                    grid[i][j].hideturtle()
                    grid[i][j] = None


    else:
        if(new_game == True):
            tetris_block = create_random_block()
            make_new_block = True
            new_game = False

        i = len(tetris_block.blocks) - 1
        while(i >= 0):
            j = len(tetris_block.blocks[i]) - 1
            while(j >= 0):
                if(isinstance(tetris_block.blocks[i][j], turtle.Turtle)):
                    tetris_block.blocks[i][j].penup()
                    tetris_block.blocks[i][j].shape("square")
                    tetris_block.blocks[i][j].color(tetris_block.color)
                    tetris_block.blocks[i][j].turtlesize = 1000
                    tetris_block.blocks[i][j].shapesize(1.5)
                    tetris_block.blocks[i][j].goto((j * 30) - 165 + (tetris_block.xPos * 30), (i * -30) + 285 - (tetris_block.yPos * 30))
                    screen.update()

                    grid[tetris_block.yPos + i][tetris_block.xPos + j] = tetris_block.blocks[i][j]

                    if(previousY != None and previousX != None and make_new_block == False):
                        grid[previousY + i][previousX + j] = None
                j -= 1
            i -= 1

    make_new_block = False
    previousX = None
    previousY = None



screen.mainloop()