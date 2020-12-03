def main():
    # TO-DO: Write a function that reads in repeating terrain. Repeats to the right.
    f = open("data.txt", "r")
    position, count = 0, 0
    for line in f:
        terrain = list(line)[:-1]
        print(terrain)
        if terrain[position] == "#":
            count += 1
        position = (position + 3) % len(terrain)
        print(count)

    print(count)


if __name__ == "__main__":
    main()
