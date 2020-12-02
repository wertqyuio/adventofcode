def main():
    # TO-DO: Write a function that reads the numbers from the data
    # file and find the unique pair of numbers that sum to 2020. 
    # Return the product of the unique pair of integers.
    f = open("data.txt", "r")
    num_dict = set()
    for line in f:
        num = int(line)
        if 2020 - num in num_dict:
            print((2020-num)*num)
        else:
            num_dict.add(num)


if __name__ == "__main__":
    main()
