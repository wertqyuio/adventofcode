def main():
    # TO-DO: Write a function that processes how many unique letters
    # a-z in each group (punctuated by a space)
    # return the sum of each group count with two variants
    f = open("data.txt", "r")
    count, group, size = 0, dict(), 0

    for line in f:
        if line == "\n":
            for answer in group:
                if group[answer] == size:
                    count += 1
            group = dict()
            size = 0
        else:
            size += 1
            for answer in list(line):
                if answer != "\n":
                    if size == 1:
                        group[answer] = 1
                    elif answer in group:
                        group[answer] += 1

    for answer in group:
        if group[answer] == size:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
