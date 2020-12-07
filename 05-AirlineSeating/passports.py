def main():
    # TO-DO: Write a function that reads where to seat passengers.
    # Encoding is binary.
    f = open("data.txt", "r")
    highest_id = 0

    for line in f:
        row, col = list(line)[:7], list(line)[7:]
        row_min, row_max, increment = 0, 127, 64
        for r in row:
            if r == "F":
                row_max -= increment
            else:
                row_min += increment
            increment //= 2
            print(row_min, row_max)
        col_min, col_max, increment = 0, 7, 4
        for c in col:
            if c == "L":
                col_max -= increment
            else:
                col_min += increment
            increment //= 2
        new_id = row_max * 8 + col_max
        if new_id > highest_id:
            highest_id = new_id
        print(line, new_id, col_max, row_max)

    print(highest_id)


if __name__ == "__main__":
    main()
