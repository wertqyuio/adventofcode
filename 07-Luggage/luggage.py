def main():
    # TO-DO: Write a function that processes how many bags that can contain a
    # shiny gold bag.
    f = open("data.txt", "r")

    wardrobe = dict()

    for line in f:
        start, end = line.find("bags")-1, line.find("contain")+len("contain ")
        container = line[:start]
        bags = line[end:-2].split(", ")
        processed_bags = [bag[2:bag.find("bag")-1] for bag in bags]
        print(processed_bags)
        for bag in processed_bags:
            if bag == "shiny gold":
                print(line)
            if bag in wardrobe:
                wardrobe[bag].append(container)
            else:
                wardrobe[bag] = [container]

    next_bag = ["shiny gold"]
    all_possible = set()
    while len(next_bag):
        current_bag = next_bag.pop()
        if current_bag in wardrobe:
            for bag in wardrobe[current_bag]:
                if bag not in all_possible:
                    all_possible.add(bag)
                    next_bag.append(bag)

    print(len(all_possible))


def second():
    # TO-DO: Write a function that counts how many bags are inside the gold bag.
    f = open("data.txt", "r")

    wardrobe = dict()

    def _qty(bag):
        return int(bag[:bag.find(" ")]) if bag[:bag.find(" ")] != "no" else 1

    def _bag(bag):
        return bag[bag.find(" ")+1:]

    for line in f:
        start, end = line.find("bags")-1, line.find("contain")+len("contain ")
        container = line[:start]
        bags = line[end:-2].split(", ")
        processed_bags = [bag[:bag.find("bag")-1] for bag in bags]
        wardrobe[container] = processed_bags

    next_bag = ["1 shiny gold"]
    count = 0
    while len(next_bag):
        current_bag = next_bag.pop()
        current_num = _qty(current_bag)
        print(current_bag)
        for bag in wardrobe[_bag(current_bag)]:
            next_num = _qty(bag)
            print(count)
            if _bag(bag) in wardrobe:
                count += (current_num) * next_num
                next_num = (_qty(bag)) * (current_num)
                next_pot_bag = str(next_num) + " " + _bag(bag)
                next_bag.append(next_pot_bag)

    print(count)


if __name__ == "__main__":
    second()
