def main():
    # TO-DO: Write a function that processes gaming instructions
    f = open("data.txt", "r")
    count = 0
    lines = dict()
    line_num = 0
    visited = set()

    for line in f:
        lines[line_num] = line[:-1]
        line_num += 1

    current = 0
    while current not in visited and current in lines:
        print(current)
        visited.add(current)
        process_line = lines[current].split(" ")
        action = process_line[0]
        num = int(process_line[1])
        if action == "nop":
            current += 1
        elif action == "acc":
            count += num
            current += 1
        else:
            current += num

    print(count)


def second():
    # TO-DO: identify the one change that allows the program to not
    # run in an infinite loop.
    f = open("data.txt", "r")
    lines = dict()
    line_num = 0
    visited = list()

    for line in f:
        lines[line_num] = line[:-1]
        line_num += 1

    current = [0, 0]

    def _process(visited, current):
        while current[0] not in visited:
            visited.append(current[0])
            process_line = lines[current[0]].split(" ")
            action = process_line[0]
            num = int(process_line[1])
            if action == "nop":
                current[0] += 1
            elif action == "acc":
                current[1] += num
                current[0] += 1
            else:
                current[0] += num

        return current

    current = _process(visited, current)
    print(visited)


if __name__ == "__main__":
    second()
