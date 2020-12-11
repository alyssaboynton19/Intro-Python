from graphics import *
from time import *
from random import *
from math import sqrt
win = GraphWin("Game", 800, 800)
win.setBackground("light green")

# messages
welcome_message = Text(Point(400, 20), "Welcome to my game!")
explanation_message = Text(Point(400, 20), "This was made as a final project for Intro to Python.")
start_message = Text(Point(400, 20), "Click a spot on the screen to move your white ball to. This will start the game!")
quit_message = Text(Point(400, 20), " If you want to quit, press x.")
new_shot_message = Text(Point(400, 20), "When you'd like to take another shot, press n.")
win_message = Text(Point(400, 20), "Congratulations, you won!")
start_over_message = Text(Point(400, 20), "The game will automatically start over. If you don't want to play again, press x and close the game window.")

# circle distance
def circleDistance(cir1, cir2):
    center1 = cir1.getCenter()
    center2 = cir2.getCenter()
    x1 = center1.getX()
    y1 = center1.getY()
    x2 = center2.getX()
    y2 = center2.getY()
    dist = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
    return dist

# user moving the white circle
def user_move(usercircle, my_circles):
    newCenter = win.getMouse()
    new_x = newCenter.getX()
    new_y = newCenter.getY()
    my_circles[len(my_circles)-1].undraw()
    usercircle = Circle(Point(new_x, new_y), 25)
    my_circles[len(my_circles)-1] = usercircle
    usercircle.setFill("white")
    usercircle.draw(win)

plays = 0

while not win.checkKey() == "x":
    print(plays)
    if plays > 0:
        start_over_message.undraw()
        score_board.undraw()
        score_rectangle.undraw()
    # keeping score
    score_number = 0
    score_rectangle = Rectangle(Point(350, 30), Point(450, 70))
    score_board = Text(Point(400, 50), score_number)
    score_rectangle.draw(win)
    score_board.draw(win)

    # pockets
    pocket1 = Circle(Point(15, 15), 30)
    pocket1.setFill("gray")
    pocket1.setOutline("gray")
    pocket1.draw(win)
    pocket2 = Circle(Point(785, 15), 30)
    pocket2.setFill("gray")
    pocket2.setOutline("gray")
    pocket2.draw(win)
    pocket3 = Circle(Point(785, 785), 30)
    pocket3.setFill("gray")
    pocket3.setOutline("gray")
    pocket3.draw(win)
    pocket4 = Circle(Point(15, 785), 30)
    pocket4.setFill("gray")
    pocket4.setOutline("gray")
    pocket4.draw(win)
    pocket5 = Circle(Point(10, 400), 30)
    pocket5.setFill("gray")
    pocket5.setOutline("gray")
    pocket5.draw(win)
    pocket6 = Circle(Point(790, 400), 30)
    pocket6.setFill("gray")
    pocket6.setOutline("gray")
    pocket6.draw(win)

    # user circle
    user_circle = Circle(Point(400, 750), 25)
    user_circle.setFill("white")
    user_circle.draw(win)

    # top row of circles
    my_circle1 = Circle(Point(280, 200), 25)
    my_circle2 = Circle(Point(340, 200), 25)
    my_circle3 = Circle(Point(400, 200), 25)
    my_circle4 = Circle(Point(460, 200), 25)
    my_circle5 = Circle(Point(520, 200), 25)
    my_circle1.setFill("red")
    my_circle2.setFill("orange")
    my_circle3.setFill("yellow")
    my_circle4.setFill("green")
    my_circle5.setFill("blue")
    my_circle1.draw(win)
    my_circle2.draw(win)
    my_circle3.draw(win)
    my_circle4.draw(win)
    my_circle5.draw(win)

    # second row of circles
    my_circle6 = Circle(Point(310, 250), 25)
    my_circle7 = Circle(Point(370, 250), 25)
    my_circle8 = Circle(Point(430, 250), 25)
    my_circle9 = Circle(Point(490, 250), 25)
    my_circle6.setFill("purple")
    my_circle7.setFill("misty rose")
    my_circle8.setFill("dark orange")
    my_circle9.setFill("gold")
    my_circle6.draw(win)
    my_circle7.draw(win)
    my_circle8.draw(win)
    my_circle9.draw(win)

    # third row of circles
    my_circle10 = Circle(Point(340, 300), 25)
    my_circle11 = Circle(Point(400, 300), 25)
    my_circle12 = Circle(Point(460, 300), 25)
    my_circle10.setFill("olive drab")
    my_circle11.setFill("deep sky blue")
    my_circle12.setFill("magenta")
    my_circle10.draw(win)
    my_circle11.draw(win)
    my_circle12.draw(win)

    # fourth row of circles
    my_circle13 = Circle(Point(370, 350), 25)
    my_circle14 = Circle(Point(430, 350), 25)
    my_circle13.setFill("maroon")
    my_circle14.setFill("wheat")
    my_circle13.draw(win)
    my_circle14.draw(win)

    # fifth row of circles
    my_circle15 = Circle(Point(400, 400), 25)
    my_circle15.setFill("pale goldenrod")
    my_circle15.draw(win)

    # list of circles and velocities
    my_circles = [my_circle1, my_circle2, my_circle3, my_circle4, my_circle5, my_circle6, my_circle7, my_circle8, my_circle9, my_circle10, my_circle11, my_circle12, my_circle13, my_circle14, my_circle15, user_circle]
    x_velocities = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y_velocities = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # list of pockets
    my_pockets = [pocket1, pocket2, pocket3, pocket4, pocket5, pocket6]

    if plays == 0:
        # printing instructions
        welcome_message.draw(win)
        sleep(2)
        welcome_message.undraw()
        explanation_message.draw(win)
        sleep(2)
        explanation_message.undraw()
        quit_message.draw(win)
        sleep(2)
        quit_message.undraw()
        start_message.draw(win)

    # original user ball launch
    user_move(user_circle, my_circles)
    print(plays)
    if plays == 0:
        start_message.undraw()
        new_shot_message.draw(win)
        sleep(1.5)
        new_shot_message.undraw()

    # main movement loop
    while score_number < 1500:
        for circle in my_circles:
            circle.move(x_velocities[my_circles.index(circle)], y_velocities[my_circles.index(circle)])
        for circle in my_circles:
            circle_index = my_circles.index(circle)
            for circle2 in my_circles:
                circle2_index = my_circles.index(circle2)
                center_1 = circle.getCenter()
                center_2 = circle2.getCenter()
                x1 = center_1.getX()
                x2 = center_2.getX()
                y1 = center_1.getY()
                y2 = center_2.getY()
                if circle_index == circle2_index:
                    continue
                else:
                    if circleDistance(circle, circle2) <= 50:             # this moves the circles on contact and helps them move correctly without overlapping
                        if x1 > x2:
                            x_velocities[circle_index] = randint(0, 3)
                            y_velocities[circle_index] = randint(-3, 3)
                            x_velocities[circle2_index] = randint(-3, 0)
                            y_velocities[circle2_index] = randint(-3, 3)
                        elif x2 > x1:
                            x_velocities[circle_index] = randint(-3, 0)
                            y_velocities[circle_index] = randint(-3, 3)
                            x_velocities[circle2_index] = randint(0, 3)
                            y_velocities[circle2_index] = randint(-3, 3)
                        elif y1 > y2:
                            x_velocities[circle_index] = randint(-3, 3)
                            y_velocities[circle_index] = randint(-0, 3)
                            x_velocities[circle2_index] = randint(-3, 3)
                            y_velocities[circle2_index] = randint(-3, 0)
                        elif y2 > y1:
                            x_velocities[circle_index] = randint(-3, 3)
                            y_velocities[circle_index] = randint(-3, 0)
                            x_velocities[circle2_index] = randint(-3, 3)
                            y_velocities[circle2_index] = randint(0, 3)
        for circle in my_circles:
            index_circle = my_circles.index(circle)
            center = circle.getCenter()
            x = center.getX()
            y = center.getY()
            if x <= 24:                                         # bouncing off the walls
                x_velocities[index_circle] = randint(0, 3)
                y_velocities[index_circle] = randint(-3, 3)
            if x >= 776:
                x_velocities[index_circle] = randint(-3, 0)
                y_velocities[index_circle] = randint(-3, 3)
            if y <= 24:
                x_velocities[index_circle] = randint(-3, 3)
                y_velocities[index_circle] = randint(0, 3)
            if y >= 776:
                x_velocities[index_circle] = randint(-3, 3)
                y_velocities[index_circle] = randint(-3, 0)
        for circle in my_circles:
            is_it_usercircle = my_circles.index(circle)
            for pocket in my_pockets:
                if circleDistance(circle, pocket) <= 40:
                    if is_it_usercircle == len(my_circles) - 1:   # keeps the user circle out of the pockets
                        continue
                    else:
                        circle.undraw()
                        score_number = score_number + 100
                        score_board.undraw()
                        score_board = Text(Point(400, 50), score_number)
                        score_board.draw(win)
                        whichcircle = my_circles.index(circle)
                        del my_circles[whichcircle]
        if win.checkKey() == "n":                                 # lets the user stop and take another shot
            x_velocities = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            y_velocities = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            user_move(user_circle, my_circles)
    win_message.draw(win)
    sleep(1)
    win_message.undraw()
    my_circles[len(my_circles)-1].undraw()
    start_over_message.draw(win)
    plays = plays + 1
    sleep(4)
