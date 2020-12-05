def main():
    # TO-DO: Write a function that reads passports.
    # First, split the passport out.
    f = open("data.txt", "r")
    count, passport, reset = 0, set(), False

    def _check_passport(passport):
        increment = 1
        for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if key not in passport:
                increment = 0
        return increment

    for line in f:
        if line == "\n":
            reset = True
        if not reset:
            [passport.add(ele[:ele.find(":")]) for ele in line.split(" ")]
        else:
            reset = False
            count += _check_passport(passport)
            passport = set()

    if len(passport): # TO check the last passport
        count += _check_passport(passport)

    print(count)


if __name__ == "__main__":
    main()
