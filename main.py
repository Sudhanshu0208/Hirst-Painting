import turtle as turtle_module
import random
colour_list = [(1, 12, 31), (53, 25, 17), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20), (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217), (122, 193, 147), (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178), (252, 197, 0), (29, 84, 92), (228, 174, 166), (186, 190, 201), (73, 73, 39)]

tim = turtle_module.Turtle()

tim.shape("turtle")
turtle_module.colormode(255)

row = 1
tim.speed("fastest")
tim.setheading(225)
tim.penup()
tim.fd(400)
tim.setheading(0)
while row < 11:
    for x in range(9):
        tim.dot(20, random.choice(colour_list))
        tim.penup()
        tim.fd(50)
        tim.pendown()
    tim.dot(20, random.choice(colour_list))
    tim.left(90)
    tim.penup()
    tim.fd(50)
    tim.left(90)
    tim.fd(450)
    tim.left(180)
    row += 1




turtle_module.Screen().exitonclick()
