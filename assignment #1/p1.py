from swampy.TurtleWorld import *
import typing, random


def main():
    print("***** Welcome to Sehir Minesweeper *****")
    print("------- First Turtle -------")
    t1_name = set_turtle_name("Please type the name of the first Turtle: ")
    t1_color = set_turtle_color(f"Please choose turtle color for {t1_name}: ")
    print("------ Harry IS READY TO GO :) ------")

    print("------- Second Turtle -------")
    t2_name = set_turtle_name("Please type the name of the second Turtle: ", t1_name)
    t2_color = set_turtle_color(f"Please choose turtle color for {t2_name}: ", t1_color)
    print("------ Ron IS READY TO GO :) ------")

    race_track()
    location_of_bombs = create_bombs()

    # turtles

    t1 = create_turtle(t1_color, (-150, 100))
    t2 = create_turtle(t2_color, (-150, 50))

    result = coin_toss(t1_name, t2_name)

    if result == 1:
        turn = True
    else:
        turn = False
    movement(t1, t1_name, t2, t2_name, location_of_bombs, turn)
    wait_for_user()


def set_turtle_name(text: str, enemy_t_name=None) -> str:
    t_name = input(text)
    while t_name == "" or t_name == enemy_t_name:
        if t_name == "":
            print(f"ERROR! name can not be empty !")
            t_name = input(text)
        else:
            print(f"ERROR! {t_name} is already taken, please enter another name !")
            t_name = input(text)
    return t_name


def set_turtle_color(text: str, enemy_t_color=None) -> str:
    t_color = input(text)
    valid_colors = ["red", "blue", "green"]
    while t_color == enemy_t_color or t_color not in valid_colors:
        if t_color not in valid_colors:
            print(f"ERROR! {t_color} is not a valid color, please select one of red, blue, or green colors: ")
            t_color = input(text)
        else:
            print(f"ERROR! {t_color} is already taken, please enter another name !")
            t_color = input(text)
    return t_color


def create_turtle(t_color: str, t_location: typing.Tuple[int, int]) -> Turtle:
    t = Turtle()
    t.set_color(t_color)
    t.x = t_location[0]
    t.y = t_location[1]
    t.fd(0)

    return t


def race_track():
    world = TurtleWorld()
    world.geometry('1000x300')

    temp_t = Turtle()
    temp_t.delay = 0.0001

    # initial position for turtle 1
    temp_t.x = -150
    temp_t.y = 100
    for i in range(30):
        for j in range(4):
            temp_t.fd(5)
            temp_t.lt(90)
        temp_t.pu()
        temp_t.fd(30)
        for k in range(4):
            temp_t.pd()
            temp_t.fd(5)
            temp_t.lt(90)

    # initial position for turtle 2
    temp_t.x = -150
    temp_t.y = 50
    for i in range(30):
        for j in range(4):
            temp_t.fd(5)
            temp_t.lt(90)
        temp_t.pu()
        temp_t.fd(30)
        for k in range(4):
            temp_t.pd()
            temp_t.fd(5)
            temp_t.lt(90)

    temp_t.x = -180
    temp_t.y = 20

    temp_t.fd(950)
    temp_t.lt(90)
    temp_t.fd(110)
    temp_t.lt(90)
    temp_t.fd(950)
    temp_t.lt(90)
    temp_t.fd(110)

    temp_t.die()
    return world


def create_bombs() -> list:
    possible_bomb_places = list(range(150, 900, 30))
    location_of_bombs = []

    for i in range(5):
        bomb1a = Turtle()
        bomb1a.set_color("#000000")
        bomb1a.x = -150
        bomb1a.y = 100
        bomb1a.pu()
        bomb1a.delay = 0

        bomb1b = Turtle()
        bomb1b.set_color("#000000")
        bomb1b.x = -150
        bomb1b.y = 50
        bomb1b.pu()
        r = random.choice(possible_bomb_places)
        if r not in list(location_of_bombs):
            possible_bomb_places.remove(r)
            location_of_bombs.append(r)
            bomb1a.fd(r)
            bomb1b.fd(r)
    return [x - 150 for x in location_of_bombs]


def coin_toss(t1_name, t2_name):
    _coin_toss = random.choice([0, 1])
    print("Lets Start the game with coin toss")
    if _coin_toss == 1:
        print(t1_name + " won the toss, " + t1_name + " starts first.")
    else:
        print(t2_name + " won the toss, " + t2_name + " starts first.")

    return _coin_toss


def roll_dice():
    return random.randint(1, 6)


def movement(t1: typing.Union[Turtle,None], t1_name: str, t2: typing.Union[Turtle,None], t2_name: str, bombs: list, turn: bool):
    if turn:
        if t1 is not None:
            turtle = t1
            t_name = t1_name
        else:
            turtle = t2
            t_name = t2_name
    else:
        if t2 is not None:
            turtle = t2
            t_name = t2_name
        else:
            turtle = t1
            t_name = t1_name

    # check whether both turtles are dead
    if turtle is None:
        play_again = input("No one could win this game. Would you like to play again? (yes/no)")
        if play_again == "yes":
            main()
        else:
            exit()

    input(f"Please press Enter to roll the dice {t_name}")

    dice_result = roll_dice()
    print(f"Dice Result: {dice_result}")

    turtle.fd(dice_result * 30)
    if int(turtle.get_x()) >= 720:
        print(f"Hooorrayy !! {t_name} has won.")
        play_again = input(f"{t_name} wins the game, would you like to play again? (yes/no)")
        if play_again == "yes":
            main()
        else:
            exit()
    elif int(turtle.get_x()) in bombs:
        print(f"{t_name} stepped on bomb. BOOOM !!! \n {t_name} is eliminated")
        if t_name == t1_name:
            movement(None, t1_name, t2, t2_name, bombs, not turn)
        elif t_name == t2_name:
            movement(t1, t1_name, None, t2_name, bombs, not turn)


    elif dice_result == 6:
        print(f"{t_name} will roll again!!!")
        movement(t1, t1_name, t2, t2_name, bombs, turn)


    else:
        turn = not turn
        movement(t1, t1_name, t2, t2_name, bombs, turn)


main()
