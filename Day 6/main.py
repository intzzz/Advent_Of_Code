def read_input(file_name):
    f = open(file_name, "r")
    return [str(x) for x in f.read().split('\n\n')]


def main():
    print(task1(read_input("input.txt")))
    print(task2(read_input("input.txt")))


def task1(customs_declaration_forms):
    ans = 0
    for customs_declaration_form in customs_declaration_forms:
        unique_answers = len(''.join(set(customs_declaration_form.replace('\n', ''))))  # Find all unique chars
        ans += unique_answers
    return ans


def task2(customs_declaration_forms):
    ans = 0
    for customs_declaration_form in customs_declaration_forms:
        group_answers = customs_declaration_form.split('\n')
        ans += calculate_answers(group_answers)
    return ans


def calculate_answers(group_answers):
    matched_answers = set("abcdefghijklmnopqrstuvwxyz")  # Set initial alphabet
    for part_of_group in group_answers:
        matched_answers &= set(part_of_group)  # find matching characters
    return len(matched_answers)


main()
