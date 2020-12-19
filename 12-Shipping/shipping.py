def main():
    # TO-DO: Write a function that reads ships instructions.
    # Each instruction is an action and magnitude.
    f = open("data.txt", "r")
    instructions = []
    distance = [0, 0, 0, 0]
    orientation = 1

    for line in f:
        process_line = line.strip('\n')
        instructions.append((process_line[0], int(process_line[1:])))

    for instruction in instructions:
        action = instruction[0]
        magnitude = instruction[1]
        if action in ["N", "E", "S", "W"]:
            idx = ["N", "E", "S", "W"].index(action)
            distance[idx] += magnitude
        elif action == "L":
            orientation = (orientation - magnitude//90) % 4
        elif action == "R":
            orientation = (orientation + magnitude//90) % 4
        else:
            distance[orientation] += magnitude

    print(abs(distance[0]-distance[2])+abs(distance[1]-distance[3]))


if __name__ == "__main__":
    main()
