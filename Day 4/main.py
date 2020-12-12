import re


def read_input(file_name):
    f = open(file_name, "r")
    return [str(x) for x in f.read().split('\n\n')]  # split input to strings


def main():
    print(calculate(read_input("input.txt"), 1))  # Task 1
    print(calculate(read_input("input.txt"), 2))  # Task 2


def calculate(passports, task):
    required_field_list = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_passports = 0
    for passport in passports:
        passport = passport.replace(' ', '\n')
        passport = list(passport.split('\n'))
        correct_field_name = 0
        current_password_status = True
        for field in required_field_list:
            for field_in_passport in passport:
                if field == field_in_passport[:3]:
                    if is_valid_field(field, field_in_passport[4:], task):
                        passport.remove(field_in_passport)
                        correct_field_name += 1
                        break
                    else:
                        current_password_status = False
                        break
            if not current_password_status:
                break
        if correct_field_name == 7:
            valid_passports += 1
    return valid_passports


def is_valid_field(field, value, task):
    if task == 1:   # If task 1 then there is no need to check the correctness of the values
        return True
    else:
        if field == "byr":
            return byr(value)
        if field == "iyr":
            return iyr(value)
        if field == "eyr":
            return eyr(value)
        if field == "hgt":
            return hgt(value)
        if field == "hcl":
            return hcl(value)
        if field == "ecl":
            return ecl(value)
        if field == "pid":
            return pid(value)


def byr(value):
    try:
        if 1920 <= int(value) <= 2002:
            return True
    except ValueError:
        pass
    return False


def iyr(value):
    try:
        if 2010 <= int(value) <= 2020:
            return True
    except ValueError:
        pass
    return False


def eyr(value):
    try:
        if 2020 <= int(value) <= 2030:
            return True
    except ValueError:
        pass
    return False


def hgt(value):
    try:
        temp = re.compile("([0-9]+)([a-zA-Z]+)")
        res = list(temp.match(value).groups())
        if 150 <= int(res[0]) <= 193 and res[1] == "cm" or 59 <= int(res[0]) <= 76 and res[1] == "in":
            return True
    except:
        pass
    return False


def hcl(value):
    try:
        if value[0] == "#" and int(value[1:], 16) and len(value[1:]) == 6:
            return True
    except ValueError:
        pass
    return False


def ecl(value):
    correct_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for color in correct_eye_colors:
        if color == value:
            return True
    return False


def pid(value):
    if len(value) == 9 and value.isdigit():
        return True
    return False


main()
