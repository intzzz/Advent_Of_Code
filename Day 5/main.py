def read_input(file_name):
    f = open(file_name, "r")
    return [str(x) for x in f.read().split('\n')]  # split input to strings


def main():
    print("Task 1 = ", calculate(read_input("input.txt")))


def calculate(boarding_passes):
    highest_seat_id = 0
    seat_ids = []
    for boarding_pass in boarding_passes:
        binary_str = "".join(binary.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0') for binary in boarding_pass)
        row = int(binary_str[:7], 2)
        column = int(binary_str[7:], 2)
        seat_id = row * 8 + column
        seat_ids.append(seat_id)
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id
    print("Task 2 = ", find_missing(seat_ids))
    return highest_seat_id


def find_missing(numbers):
    numbers.sort()
    ans = int(list(set(range(numbers[0], numbers[-1])) - set(numbers))[0])
    return ans


main()
