def main():
    # TO-DO: Write a function that reads in each policy, and a corresponding
    # password if the password passes the policy, count it!
    # The policy is # of min appearances, # of max appearance of a char
    f = open("data.txt", "r")
    count = 0
    for line in f:
        line_arr = line.split(" ")
        appearances = line_arr[0].split("-")
        min_appearances, max_appearances = int(appearances[0]), int(appearances[1])
        char = line_arr[1][:-1]
        password = line_arr[2]
        comparison = password.count(char)
        count += (comparison >= min_appearances) * (comparison <= max_appearances)

    print(count)


if __name__ == "__main__":
    main()
