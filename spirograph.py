import turtle as tt
tt.Turtle()
tt.bgcolor("black")
tt.pensize(1)
tt.speed(9)

while(True):
    for i in range (6):
        for colors in ["indigo","red","green","yellow","cyan","maroon"]:
            tt.color(colors)
            tt.circle(100)
            tt.left(10)

tt.hideturtle()
tt.mainloop()