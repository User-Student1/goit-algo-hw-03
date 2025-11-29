import turtle

def koch_line(t, lenght, level):
    """
    Малює одну лінію Коха.
    t - черепашка
    lenght - довжина лінії
    level - рівень рекурсії
    """

    if level == 0:
        t.forward(lenght)
        return
    
    lenght /= 3

    koch_line(t, lenght, level - 1)
    t.left(60)
    koch_line(t, lenght, level - 1)
    t.right(120)
    koch_line(t, lenght, level -1)
    t.left(60)
    koch_line(t, lenght, level - 1)

def koch_showflake(level):
    """
    Малює повну сніжинку Коха з трьох ліній.
    """

    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)

    t.penup()
    t.goto(-150, 100) #зміщення фігури(для розміщення на екрані)
    t.pendown()

    for _ in range(3):
        koch_line(t, 300, level)
        t.right(120)

    turtle.done()

def main():
    level = int(input("Ввкдіть рівень рекрусії (0-6): "))
    koch_showflake(level)

if __name__ == "__main__":
    main()