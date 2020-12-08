def main():
    a = read_input("input.txt")
    a.sort(reverse=True)
    for x in a:
        if x >= 2020:
            a.remove(x)
        else:
            break
    print(calculate(a))


def read_input(file_name):
    f = open(file_name, "r")
    a = [int(x) for x in f.read().split()]
    return a


def calculate(numbers):

    for x in numbers:
        number1 = x
        for y in reversed(numbers):
            number2 = y
            if (number1 + number2) == 2020:
                ans = number1*number2
                return ans


main()
