def read_input(file_name):
    f = open(file_name, "r")
    return [int(x) for x in f.read().split('\n')]


def main():
    input = read_input("input.txt")
    print(task2(input, task1(input)))


def task2(xmas, incorrect_nr):
    new_xmas = [n for n in xmas if n < incorrect_nr]
    contiguous_set_of_nr = 2
    contiguous_set_of_nr_list = []
    tmp_nr = 0
    while contiguous_set_of_nr < len(new_xmas):
        for i in range(len(new_xmas) - 1):
            contiguous_set_of_nr_list.append(new_xmas[i])
            if len(contiguous_set_of_nr_list) == contiguous_set_of_nr:
                for x in contiguous_set_of_nr_list:
                    tmp_nr += x
                if tmp_nr == incorrect_nr:
                    return min(contiguous_set_of_nr_list) + max(contiguous_set_of_nr_list)
                else:
                    tmp_nr = 0
                    contiguous_set_of_nr_list.pop(0)
        contiguous_set_of_nr += 1


def task1(xmas):
    preamble = 25
    tmp_preamble_list = []
    for i in range(len(xmas)):
        if i + 1 >= len(xmas):
            print("All correct")
            exit()
        tmp_preamble_list.append(int(xmas[i]))
        if len(tmp_preamble_list) == preamble:
            if not if_valid(tmp_preamble_list, int(xmas[i + 1])):
                return xmas[i + 1]
            tmp_preamble_list.pop(0)


def if_valid(preamble_list, next_number):
    for x in preamble_list:
        for y in reversed(preamble_list):
            if x != y and x + y == next_number:
                return True
    return False


if __name__ == '__main__':
    main()
