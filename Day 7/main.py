import re


def read_input(file_name):
    f = open(file_name, "r")
    return [str(x) for x in f.read().split('\n')]


def main():
    # print(task1(read_input("input1.txt"), "shiny gold"))
    print(task2(read_input("input.txt"), "shiny gold"))


def task1(rules, bag):
    global bag_colors
    for rule in rules:
        rule = rule.split('contain')
        node = rule[0].replace("bags", "").strip()
        children = rule[1].split(',')
        if node.find(bag) == -1:
            for child in children:
                if child.find(bag) != -1:
                    bag_colors.add(node)
                    task1(rules, node)
    return len(bag_colors)


def task2(rules, bag):
    global total_bags, multiplier_from_previous_iteration, multiplier_list
    for rule in rules:
        rule = rule.split('contain')
        node = rule[0].replace("bags", "").strip()
        children = rule[1].split(',')
        if node.find(bag) != -1:
            for child in children:
                try:
                    current_bag_count = int(re.search(r'\d+', child).group())
                    child = ''.join([i for i in child if not i.isdigit()])
                except:
                    break  # Last bag that contains no other bags
                child = child.replace("bags", "").replace("bag", "").replace(".", "").replace("no other", "").strip()
                total_bags += current_bag_count * multiplier_from_previous_iteration
                multiplier_from_previous_iteration *= current_bag_count
                multiplier_list.append(current_bag_count)
                task2(rules, child)

    multiplier_from_previous_iteration /= multiplier_list.pop()
    return int(total_bags)


multiplier_from_previous_iteration = 1
multiplier_list = [1]
total_bags = 0
bag_colors = set()
main()
