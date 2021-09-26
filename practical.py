"""
author: Michael Vaughan <mav8557@rit.edu>

Error messages
"""
import turtle

SIZE = 250


def draw_messages(size, count):
    for _ in range(count):
        turtle.up()
        turtle.right(90)
        turtle.forward(size / 2)
        turtle.left(90)
        turtle.forward(size / 2)
        turtle.down()
        draw_message(size)


def draw_box(size):
    """
    Draw a box of a particular size
    """
    for i in range(4):
        if i % 2 == 0:
            turtle.forward(size * 2)
        else:
            turtle.forward(size)

        turtle.right(90)


def draw_x(size):
    """
    Draw the "X" button for the message,
    with a specific size

    :param: size is size of the button
    """
    turtle.fillcolor("red")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

    turtle.end_fill()

    # save pen size
    oldsize = turtle.pensize()

    turtle.pensize(size / 8)
    turtle.pencolor("white")
    turtle.right(45)
    turtle.up()
    turtle.forward(size * 0.2)
    turtle.down()
    turtle.forward(size)
    turtle.up()

    # draw second part
    turtle.backward(size)
    turtle.backward(size * 0.2)
    turtle.left(45)
    turtle.forward(size)

    turtle.right(90 + 45)

    turtle.up()
    turtle.forward(size * 0.2)
    turtle.down()
    turtle.forward(size)
    turtle.up()

    turtle.pensize(oldsize)
    turtle.backward(size)
    turtle.backward(size * 0.2)
    turtle.right(45)
    turtle.forward(size)
    turtle.left(180)
    turtle.pencolor("black")
    turtle.down()


def write_error(size):
    """
    Write the string "ERROR!" for the message,
    making the size relative to the size of the box
    """
    turtle.write("ERROR!", font=("Courier", size // 8, "normal"), align="center")


def draw_message(size):
    """
    Draw a message of a particular size
    """
    turtle.fillcolor("grey")
    turtle.begin_fill()
    draw_box(size)
    turtle.end_fill()
    # draw x
    turtle.forward((size * 2) - size / 5)
    draw_x(size / 5)
    turtle.backward((size * 2) - size / 5)

    turtle.right(90)
    turtle.forward(size / 5)
    turtle.left(90)
    turtle.forward(size * 2)
    turtle.backward(size * 2)
    turtle.right(90)
    turtle.backward(size / 5)
    turtle.forward(size / 2)
    turtle.left(90)
    turtle.up()
    turtle.forward(size)
    write_error(size)
    turtle.backward(size)

    turtle.right(90)
    turtle.backward(size / 2)
    turtle.left(90)


def main():
    """
    Take user input and draw the error messages
    """
    init()  # initialize the board
    messages = -1

    while messages < 0:
        try:
            messages = int(input("Enter the number of messages: "))
        except ValueError:
            print("Enter a number!")

    print("Drawing " + str(messages) + " error messages...")

    draw_messages(SIZE, messages)
    # turtle.hideturtle()

    input("Press enter to stop...")


def init():
    turtle.setworldcoordinates(-440, -440, 440, 440)
    turtle.up()
    turtle.goto(-440, 400)
    turtle.down()
    # double the pensize
    turtle.pensize(2 * turtle.pensize())
    turtle.speed(0)


if __name__ == "__main__":
    main()
