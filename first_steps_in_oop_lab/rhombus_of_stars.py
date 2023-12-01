def print_row(n, count):
    print(" " * (n - count), end="")
    print(*["*"] * count)


n = int(input())


def print_rhombus(n):
    for count in range(1, n + 1):
        print_row(n, count)

    for count in range(n - 1, 0, -1):
        print_row(n, count)


print_rhombus(n)
