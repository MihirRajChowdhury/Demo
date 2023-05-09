from turtle import Turtle, Screen

mil = Turtle()
mil.shape("turtle")
mil.color("green")
screen = Screen()


def move_forwards():
    mil.forward(10)


def move_backwards():
    mil.backward(10)


def turn_right():
    mil.right(10)


def turn_left():
    mil.left(10)


def clear():
    # mil.reset()

    mil.home()
    mil.clear()


screen.listen()
screen.onkeypress(key="w",fun=move_forwards)
screen.onkeypress(key="s",fun=move_backwards)
screen.onkeypress(key="a",fun=turn_right)
screen.onkeypress(key="d",fun=turn_left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()


