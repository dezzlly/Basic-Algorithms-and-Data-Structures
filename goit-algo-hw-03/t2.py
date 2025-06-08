import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(5)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


if __name__ == "__main__":
    while True:
        user_input = input("Please enter the deepth of the snowflake ")
        try:
            deepth = int(user_input)
            if deepth > 3:
                print("Integer is too big. Please enter integer less or equal 3")
            elif deepth < 0:
                print("Please enter a non-negative integer.")
            else:
                draw_koch_curve(deepth)
                break
        except ValueError:
            print("This is not integer. Please enter an integer.")