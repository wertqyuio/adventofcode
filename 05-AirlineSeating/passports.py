def main():
    # TO-DO: Write a function that reads where to seat passengers.
    # Encoding is binary.
    # Two-part problem.
    # Find highest id, and your seat (knowing that your seat
    # is the "missing seat of the plane")
    f = open("data.txt", "r")
    boarding = set()

    for line in f:
        row, col = list(line)[:7], list(line)[7:]
        row_min, row_max, increment = 0, 127, 64
        for r in row:
            if r == "F":
                row_max -= increment
            else:
                row_min += increment
            increment //= 2
        col_min, col_max, increment = 0, 7, 4
        for c in col:
            if c == "L":
                col_max -= increment
            else:
                col_min += increment
            increment //= 2
        new_id = row_max * 8 + col_max
        boarding.add(new_id)

    print(max(boarding))

    for num in boarding:
        if (num + 1) not in boarding and (num + 2) in boarding:
            print(num+1)

if __name__ == "__main__":
    main()
