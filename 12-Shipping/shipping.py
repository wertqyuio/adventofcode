def main():
    # TO-DO: Write a function that reads ships instructions.
    # Each instruction is an action and magnitude.
    f = open("data.txt", "r")
    instructions = []
    distance = [0, 0]
    waypoint = [1, 10]

    def orientation(angle, waypoint):
        temp = waypoint[0]
        if angle == 1:
            waypoint[0] = waypoint[1]
            waypoint[1] = -temp
        elif angle == 2:
            waypoint[0] = -waypoint[0]
            waypoint[1] = -waypoint[1]
        elif angle == 3:
            waypoint[0] = -waypoint[1]
            waypoint[1] = temp

    for line in f:
        process_line = line.strip('\n')
        instructions.append((process_line[0], int(process_line[1:])))

    for instruction in instructions:
        action = instruction[0]
        magnitude = instruction[1]
        if action in ["N", "E", "S", "W"]:
            idx = ["N", "E", "S", "W"].index(action)
            if idx < 2:
                waypoint[idx % 2] += magnitude
            else:
                waypoint[idx % 2] -= magnitude
        elif action == "L":
            print(magnitude)
            orientation(magnitude//90 % 4, waypoint)
        elif action == "R":
            orientation(-magnitude//90 % 4, waypoint)
        else:
            for idx in range(len(waypoint)):
                distance[idx] += waypoint[(idx) % 2]*magnitude

    print(abs(distance[0])+abs(distance[1]))


if __name__ == "__main__":
    main()
