def read_input(file_name):
    f = open(file_name, "r")
    return [str(x) for x in f.read().split('\n')]


def main():
    input_from_file = read_input("test.txt")
    print("test1 - ", task1(input_from_file))
    print("test2 - ", task2(input_from_file))

    input_from_file = read_input("input.txt")
    print("task1 - ", task1(input_from_file))
    print("task2 - ", task2(input_from_file))


def task1(instructions):
    north = 0
    east = 0
    current_direction = 'E'
    direction_list = ['N', 'E', 'S', 'W']
    for instruction in instructions:

        if instruction[:1] == 'N':
            north += int(instruction[1:])

        elif instruction[:1] == 'E':
            east += int(instruction[1:])

        elif instruction[:1] == 'S':
            north -= int(instruction[1:])

        elif instruction[:1] == 'W':
            east -= int(instruction[1:])

        elif instruction[:1] == 'F':
            if current_direction == 'N':
                north += int(instruction[1:])
            elif current_direction == 'E':
                east += int(instruction[1:])
            elif current_direction == 'S':
                north -= int(instruction[1:])
            elif current_direction == 'W':
                east -= int(instruction[1:])

        elif instruction[:1] == 'L':
            turn_degrees = int(instruction[1:]) % 360
            current_direction_index = direction_list.index(current_direction)
            if turn_degrees == 0:
                pass
            elif turn_degrees == 90:
                current_direction = direction_list[current_direction_index - 1]
            elif turn_degrees == 180:
                current_direction = direction_list[(current_direction_index + 2) % 4]
            elif turn_degrees == 270:
                current_direction = direction_list[(current_direction_index + 1) % 4]

        elif instruction[:1] == 'R':
            turn_degrees = int(instruction[1:]) % 360
            current_direction_index = direction_list.index(current_direction)
            if turn_degrees == 0:
                pass
            elif turn_degrees == 90:
                current_direction = direction_list[(current_direction_index + 1) % 4]
            elif turn_degrees == 180:
                current_direction = direction_list[(current_direction_index + 2) % 4]
            elif turn_degrees == 270:
                current_direction = direction_list[(current_direction_index - 1) % 4]

    return abs(north) + abs(east)


def task2(instructions):
    waypoint = [1, 10]  # 1 north, 10 east
    ship = [0, 0]
    for instruction in instructions:

        if instruction[:1] == 'F':
            ship[0] = ship[0] + waypoint[0] * int(instruction[1:])
            ship[1] = ship[1] + waypoint[1] * int(instruction[1:])

        elif instruction[:1] == 'N':
            waypoint[0] += int(instruction[1:])

        elif instruction[:1] == 'E':
            waypoint[1] += int(instruction[1:])

        elif instruction[:1] == 'S':
            waypoint[0] -= int(instruction[1:])

        elif instruction[:1] == 'W':
            waypoint[1] -= int(instruction[1:])

        elif instruction[:1] == 'R':
            turn_degrees = int(instruction[1:]) % 360

            if turn_degrees == 0:
                pass
            elif turn_degrees == 90:
                temp = waypoint[0]
                waypoint[0] = 0 - waypoint[1]
                waypoint[1] = temp
            elif turn_degrees == 180:
                waypoint[0] = 0 - waypoint[0]
                waypoint[1] = 0 - waypoint[1]
            elif turn_degrees == 270:
                temp = waypoint[0]
                waypoint[0] = waypoint[1]
                waypoint[1] = 0 - temp

        elif instruction[:1] == 'L':
            turn_degrees = int(instruction[1:]) % 360

            if turn_degrees == 0:
                pass
            elif turn_degrees == 90:
                temp = waypoint[0]
                waypoint[0] = waypoint[1]
                waypoint[1] = 0 - temp
            elif turn_degrees == 180:
                waypoint[0] = 0 - waypoint[0]
                waypoint[1] = 0 - waypoint[1]
            elif turn_degrees == 270:
                temp = waypoint[0]
                waypoint[0] = 0 - waypoint[1]
                waypoint[1] = temp

    return abs(ship[0]) + abs(ship[1])


if __name__ == '__main__':
    main()
