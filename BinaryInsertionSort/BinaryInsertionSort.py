
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ran_num = int(input('Введите число от 1 до 10: '))


def binary_insertion_sort(x, y):
    while True:
        median = int(len(x) / 2)
        left = x[:median]
        right = x[median:]
        if y == x[median]:
            print(x[median], "index:", a.index(x[median]))
            break
        elif y < x[median]:
            x = left
            print(x)
        else:
            x = right
            print(x)
        median = int(len(x) / 2)


binary_insertion_sort(a, ran_num)