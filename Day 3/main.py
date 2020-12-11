def read_input(file_name):
    f = open(file_name, "r")
    return [str(x) for x in f.read().split('\n')]  # split input to strings


def main():
    trees = read_input("input.txt")
    print("Solution 1 = ", calculate(trees, 3, 1))
    print("Solution 2 = ",
          calculate(trees, 1, 1) * \
          calculate(trees, 3, 1) * \
          calculate(trees, 5, 1) * \
          calculate(trees, 7, 1) * \
          calculate(trees, 1, 2) \
          )


def calculate(trees, right, down):
    index = 0
    i = 0
    elements_in_row = len(trees[0])

    for x in range(0, len(trees), down):

        while index >= elements_in_row:
            index -= elements_in_row

        if trees[x][index] == "#":
            i += 1
        index += right

    return i


main()
