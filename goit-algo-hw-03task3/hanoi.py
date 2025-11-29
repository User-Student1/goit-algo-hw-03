def hanoi(n, A, B, C, pegs):
    if n == 1:
        disk = pegs[A].pop()
        pegs[C].append(disk)
        print(f"Перемістити диск з {A} на {C}: {disk}")
        print("Проміжний стан:", pegs)
        return

    hanoi(n - 1, A, C, B, pegs)

    disk = pegs[A].pop()
    pegs[C].append(disk)
    print(f"Перемістити диск з {A} на {C}: {disk}")
    print("Проміжний стан:", pegs)

    hanoi(n - 1, B, A, C, pegs)


n = int(input("Введіть кількість дисків: "))

pegs = {
    'A': list(range(n, 0, -1)),
    'B': [],
    'C': []
}

print("Початковий стан:", pegs)
hanoi(n, 'A', 'B', 'C', pegs)
print("Кінцевий стан:", pegs)