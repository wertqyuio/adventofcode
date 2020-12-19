def main():
    # TO-DO: Write a function that reads the seating (there are floor
    # occupied, empty)
    f = open("data.txt", "r")
    seating, next_seating, row_max, col_max = [], [], None, None
    comparison = False

    def check_direction(row, col, seating, row_c, col_c):
        if row < 0 or row >= row_max:
            return 0
        elif col < 0 or col >= col_max:
            return 0
        elif seating[row][col] == "#":
            return 1
        elif seating[row][col] == "L":
            return 0
        else:
            return check_direction(row+row_c, col+col_c, seating, row_c, col_c)

    def adjacent_occupied(row, col, seating):
        occupied = 0
        for (adj_row, adj_col) in [(-1, 0), (1, 0), (0, -1), (0, 1),
                                   (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            occupied += check_direction(row+adj_row, col+adj_col,
                                        seating, adj_row, adj_col)
        return occupied

    def seat_passenger(row, col, seating, next_seating):
        adjacencies = adjacent_occupied(row, col, seating)
        if seating[row][col] == "L" and adjacencies == 0:
            next_seating[row][col] = "#"
        elif seating[row][col] == "#" and adjacencies >= 5:
            next_seating[row][col] = "L"
        else:
            next_seating[row][col] = seating[row][col]

    def seat_passengers(seating, next_seating):
        for row in range(row_max):
            for col in range(col_max):
                seat_passenger(row, col, seating, next_seating)

    for line in f:
        seating.append(list(line.strip('\n')))
        next_seating.append([None]*len(seating[-1]))

    row_max = len(seating)
    col_max = len(seating[0])
    iteration = 0

    while not comparison and iteration < 30000:
        if not iteration % 2:
            seat_passengers(seating, next_seating)
        else:
            seat_passengers(next_seating, seating)
        iteration += 1
        comparison = True
        for row in range(row_max):
            for col in range(col_max):
                if seating[row][col] != next_seating[row][col]:
                    comparison = False

    seats = 0
    for row in range(row_max):
        for col in range(col_max):
            if next_seating[row][col] == "#":
                seats += 1

    print(seats)


if __name__ == "__main__":
    main()
