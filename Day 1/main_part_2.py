def main():
    a = read_input("input.txt")
    a.sort()
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
    size = len(numbers)
    for i in range(len(numbers)):
        number1 = numbers[i]
        for k in range(len(numbers)):
            number2 = numbers[k + 1]
            if k + 1 >= size - 1:
                break
            for j in range(len(numbers)):
                number3 = numbers[j + 2]
                if j + 2 >= size - 1:
                    break
                if number1 + number2 + number3 == 2020:
                    return number1*number2*number3


main()
