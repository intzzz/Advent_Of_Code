def read_input(file_name):
    f = open(file_name, "r")
    return [int(x) for x in f.read().split('\n')]


def main():
    input_from_file = read_input("input.txt")
    ans = task1(input_from_file)
    print(ans.count(1) * ans.count(3))
    print(task2(ans))


def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count += 1
        else:
            return count


def task2(difference_list):
    difference_list.insert(0, "3")
    diff_str = ''.join([str(elem) for elem in difference_list])
    pattern1 = occurrences(diff_str, "3113")
    pattern2 = occurrences(diff_str, "31113")
    pattern3 = occurrences(diff_str, "311113")
    return pow(7, pattern3) * pow(4, pattern2) * pow(2, pattern1)


def task1(jolts):
    jolts.append(max(jolts) + 3)
    jolts.append(0)
    jolts.sort()
    difference_list = []
    for i in range(len(jolts) - 1):
        if jolts[i + 1] - jolts[i] == 1:
            difference_list.append(1)
        if jolts[i + 1] - jolts[i] == 3:
            difference_list.append(3)
    return difference_list


if __name__ == '__main__':
    main()
