def read_input(file_name):
    with open(file_name, "r") as file:
        result = [str(x) for x in file.read().split('\n')]
    return create_correct_list(result)


def create_correct_list(first_list):
    rows = len(first_list)
    columns = len(first_list[0])
    correct_list = [[] for _ in range(len(first_list))]
    for x in range(rows):
        for y in range(columns):
            correct_list[x].append(first_list[x][y])
    return correct_list


def main():
    task1 = True
    task2 = False
    layout = read_input("input.txt")
    task(layout, [4, 1], task1)
    task(layout, [5, 1], task2)


def task(seat_layout, task_rules, first_task):
    rows = len(seat_layout)
    columns = len(seat_layout[0])
    new_layout = [[] for _ in range(rows)]
    for x in range(rows):
        for y in range(columns):
            if seat_layout[x][y] == '#':
                if check_if_adjacent_occupied(x, y, seat_layout, task_rules[0], first_task):
                    new_layout[x].append('L')
                else:
                    new_layout[x].append('#')
            elif seat_layout[x][y] == 'L':
                if check_if_adjacent_occupied(x, y, seat_layout, task_rules[1], first_task):
                    new_layout[x].append('L')
                else:
                    new_layout[x].append('#')
            elif seat_layout[x][y] == '.':
                new_layout[x].append('.')
    if seat_layout == new_layout:
        print(sum(sublist.count('#') for sublist in new_layout))
    else:
        task(new_layout, task_rules, first_task)


def check_if_adjacent_occupied(x, y, seat_map, allowed_count, first_task):
    if first_task:
        return check_if_adjacent_occupied_task1(x, y, seat_map, allowed_count)
    else:
        return check_if_adjacent_occupied_task2(x, y, seat_map, allowed_count)


def check_if_adjacent_occupied_task1(x, y, seat_map, allowed_count):
    count = 0
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if i == j == 0 or x + i < 0 or y + j < 0:
                continue
            try:
                if seat_map[x + i][y + j] == '#':
                    count += 1
                    if count >= allowed_count:
                        return True
            except IndexError:
                pass
    return False


def check_if_adjacent_occupied_task2(x, y, seat_map, allowed_count):
    count = 0
    rows = len(seat_map)
    columns = len(seat_map[0])

    for k in range(1, columns):
        try:
            if y - k < 0:
                break
            if seat_map[x][y - k] == 'L':
                break
            if seat_map[x][y - k] == '#':
                count += 1
                if count >= allowed_count:
                    return True
                break
        except IndexError:
            break

    for k in range(1, columns):
        try:
            if seat_map[x][y + k] == 'L':
                break
            if seat_map[x][y + k] == '#':
                count += 1
                if count >= allowed_count:
                    return True
                break
        except IndexError:
            break

    for m in range(1, rows):
        try:
            if x - m < 0:
                break
            if seat_map[x - m][y] == 'L':
                break
            if seat_map[x - m][y] == '#':
                count += 1
                if count >= allowed_count:
                    return True
                break
        except IndexError:
            break

    for a in range(1, rows):
        try:
            if seat_map[x + a][y] == 'L':
                break
            if seat_map[x + a][y] == '#':
                count += 1
                if count >= allowed_count:
                    return True
                break
        except IndexError:
            break

    for i in range(1, max(rows, columns)):
        try:
            if x - i < 0 or y - i < 0:
                break
            if seat_map[x - i][y - i] == 'L':
                break
            if seat_map[x - i][y - i] == '#':
                count += 1
                if count >= allowed_count:
                    return True
                break
        except IndexError:
            break

    for j in range(1, max(rows, columns)):
        try:
            if seat_map[x + j][y + j] == 'L':
                break
            if seat_map[x + j][y + j] == '#':
                count += 1
                if count >= allowed_count:
                    return True
                break
        except IndexError:
            break

    for n in range(1, max(rows, columns)):
        try:
            if y - n < 0:
                break
            if seat_map[x + n][y - n] == 'L':
                break
            if seat_map[x + n][y - n] == '#':
                count += 1
                if count >= allowed_count:
                    return True
                break
        except IndexError:
            break

    for o in range(1, max(rows, columns)):
        try:
            if x - o < 0:
                break
            if seat_map[x - o][y + o] == 'L':
                break
            if seat_map[x - o][y + o] == '#':
                count += 1
                if count >= allowed_count:
                    return True
                break
        except IndexError:
            break
    return False


if __name__ == '__main__':
    main()
