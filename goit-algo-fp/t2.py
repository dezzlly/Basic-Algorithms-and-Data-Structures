import turtle
import math

def draw_pythagoras_tree(t, length, level):
    if level == 0:
        return

    # Рисуем основание квадрата
    t.forward(length)

    # Сохраняем текущее положение и направление
    pos = t.pos()
    angle = t.heading()

    # Поворачиваем и рисуем левую ветвь
    t.left(45)
    new_length = length * math.sqrt(2) / 2
    draw_pythagoras_tree(t, new_length, level - 1)

    # Возвращаемся к исходному положению
    t.setpos(pos)
    t.setheading(angle)

    # Поворачиваем и рисуем правую ветвь
    t.right(45)
    draw_pythagoras_tree(t, new_length, level - 1)

    # Возвращаемся назад
    t.setpos(pos)
    t.setheading(angle)
    t.backward(length)

if __name__ == "__main__":
    # Запрашиваем уровень рекурсии у пользователя
    level = int(input("Введите уровень рекурсии (например, 7): "))

    # Настройка turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.color("brown")
    t.speed(0)
    t.left(90)  # направим вверх

    # Начальная позиция
    t.penup()
    t.goto(0, -200)
    t.pendown()

    # Запуск рисования
    draw_pythagoras_tree(t, 100, level)

    # Ждём клика мышкой
    screen.exitonclick()
