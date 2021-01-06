def read_input(file_name):
    f = open(file_name, "r")
    return [str(x) for x in f.read().split('\n')]


def main():
    input_from_file = read_input("test.txt")
 #   print("test1 - ", task1(input_from_file))
    print("test2 - ", task2(input_from_file))
   # task2(["17","x","13","19"])
    input_from_file = read_input("input.txt")
  #  print("task 1 - ", task1(input_from_file))


def task1(notes):
    earliest_department = int(notes[0])
    bus_ids = [int(x) for x in notes[1].split(',') if x.isdigit()]
    bus_waiting_times = []
    for bus in bus_ids:
        bus_waiting_times.append(bus - earliest_department % bus)
    index = bus_waiting_times.index(min(bus_waiting_times))
    return bus_ids[index] * bus_waiting_times[index]


def task2(bus_ids):
    bus_ids.pop(0)
    bus_ids = bus_ids[0].split(',')
    j = 1
    k = 1
    timestamp = 0
    consecutive = False
    for i in range(len(bus_ids)):
        consecutive = False
        if bus_ids[i] == 'x':
            continue
        else:
            while not consecutive:
                timestamp = j * int(bus_ids[i])
                if i + 1 < len(bus_ids):
                    while True:
                        if bus_ids[i + 1] == 'x':
                            break
                        if k * int(bus_ids[i + 1]) == (i + 1 + timestamp):
                            print("SOMETHING")
                            print(timestamp)
                            print(bus_ids[i])
                            print(bus_ids[i + 1])
                            print(i)
                            consecutive = True
                            break
                        if k * int(bus_ids[i + 1]) > i + timestamp:
                            break
                        k += 1
                j += 1
    print(timestamp)







if __name__ == '__main__':
    main()


'''
    x = []
    y = []
    bus_id = bus_ids[0].split(',')
    print(bus_id)
    print(len(bus_id))
    exit()
    consecutive = False
    i = 0
    while True:
        if not consecutive:
            x.append(int(bus_id[0]) * i)
            y.append(int(bus_id[1]) * i)
            for j in y:
                if j - 1 == x[i]:
                    print("DONE")
                    print(j)
                    consecutive = True
                    break
        if consecutive:
            print(x[i] % int(bus_id[4]))
            break
        i += 1
    print(x)
    print(y)

'''