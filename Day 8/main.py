import re


def read_input(file_name):
    f = open(file_name, "r")
    return [str(x) for x in f.read().split('\n')]


def main():
    print(task1(read_input("input.txt")))
    find_correct_instruction(read_input("input.txt"))


def task1(modifiable_instructions):
    i = 0
    acc = 0
    used_instructions = []
    while True:
        if modifiable_instructions[i].find("jmp") != -1:
            for x in used_instructions:
                if x == i:
                    return acc
            jmp_nr = int(re.search(r'-?\d+', modifiable_instructions[i]).group())
            used_instructions.append(i)
            i += jmp_nr
            if i >= len(modifiable_instructions):
                print(acc)
                exit()

        if modifiable_instructions[i].find("nop") != -1:
            for x in used_instructions:
                if x == i:
                    return acc
            used_instructions.append(i)
            i += 1
            continue

        if modifiable_instructions[i].find("acc") != -1:
            for x in used_instructions:
                if x == i:
                    return acc
            acc_nr = int(re.search(r'-?\d+', modifiable_instructions[i]).group())
            acc += acc_nr
            used_instructions.append(i)
            i += 1
        if i >= len(modifiable_instructions):
            print(acc)
            exit()


def find_correct_instruction(instructions):
    for i in range(len(instructions)):
        #print("i - ", i)
        switch_instructions(instructions, i)
        task1(instructions)
        switch_instructions(instructions, i)


def switch_instructions(instructions, i):
    instructions[i] = instructions[i].split(" ")
    if instructions[i][0] == "nop":
        instructions[i][0] = "jmp"
    elif instructions[i][0] == "jmp":
        instructions[i][0] = "nop"
    instructions[i] = instructions[i][0] + " " + instructions[i][1]
    return instructions


main()
