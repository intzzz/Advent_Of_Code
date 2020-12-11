import re


def read_input(file_name):
    f = open(file_name, "r")
    return [str(x) for x in f.read().split('\n')] # split input to strings


def main():
    print(calculate(read_input("input.txt")))
    print(calculate_2(read_input("input.txt")))


def calculate(passwords):
    i = 0
    for x in range(len(passwords)):
        cypher = passwords[x].split(':')   # Cypher[0] is password policy and cypher[1] is password
        letter = (cypher[0][len(cypher[0]) - 1])
        letter_count_in_password = cypher[1].count(letter)
        number_range = re.findall('\d+', cypher[0])
        if int(number_range[0]) <= letter_count_in_password <= int(number_range[1]):
            i += 1
    return i


def calculate_2(passwords):
    i = 0
    for x in range(len(passwords)):
        cypher = passwords[x].split(':')
        letter = (cypher[0][len(cypher[0]) - 1])
        number_range = re.findall('\d+', cypher[0])
        if cypher[1][int(number_range[0])] == letter and \
            cypher[1][int(number_range[1])] != letter or \
            cypher[1][int(number_range[0])] != letter and \
            cypher[1][int(number_range[1])] == letter:
            i += 1
    return i


main()
