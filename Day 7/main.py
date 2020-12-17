def read_input(file_name):
    f = open(file_name, "r")
    return [str(x) for x in f.read().split('\n')]


def main():
    global bag_colors
    print(calculate(read_input("input.txt"), "shiny gold"))
    #print(task2(read_input("input.txt")))


def calculate(rules, bag):
    global bag_colors
    for rule in rules:
        rule = rule.split('contain')
        node = rule[0].replace("bags", "").strip()
        children = rule[1].split(",")
        if node.find(bag) == -1:
            for child in children:
                if child.find(bag) != -1:
                    bag_colors.add(node)
                    calculate(rules, node)
    return len(bag_colors)


bag_colors = set()
main()




