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
    reset_dict = list()

    for line in f:
        lines[line_num] = line[:-1] if line[-1] == "\n" else line
        line_num += 1

    current = [0, 0, 0, None]

    def _remap(field):
        action = field[2][0]
        if action == "nop":
            action = "jmp"
        elif action == "jmp":
            action = "nop"
        field[2][0] = action

    def _process(visited, current, printvar=False):
        while current[0] not in visited and current[0] < line_num:
            if printvar:
                print(current[0])
            visited.append(current[0])
            reset_dict.append(current[1])
            process_line = lines[current[0]].split(" ")
            action = process_line[0]
            num = int(process_line[1])
            current[2] = process_line
            if action == "nop":
                current[0] += 1
            elif action == "acc":
                current[1] += num
                current[0] += 1
            else:
                current[0] += num
        if current[3] is None:
            current[3] = len(visited)

    def _modify_process(visited, current):
        if current[0] == line_num:
            return
        current[3] -= 1
        while len(visited) and len(visited) > current[3]:
            latest = visited.pop()
        _remap(current)
        visited.append(latest)
        current[0] = latest
        current[1] = reset_dict[len(visited)-1]
        action = current[2][0]
        num = int(current[2][1])
        if action == "acc":
            current[1] += num
            current[0] += 1
        elif action == "nop":
            current[0] += 1
        else:
            current[0] += num
        _process(visited, current)

    _process(visited, current)
    counter = 3000
    while current[0] != line_num and counter and current[0] < line_num:
        counter -= 1
        _modify_process(visited, current)

    print('answer is ' + str(current[1]))


if __name__ == "__main__":
    second()
