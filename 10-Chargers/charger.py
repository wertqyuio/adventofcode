def main():
    # TO-DO: Write a function that sorts all the unique adapters.
    # Note how many 1-volt differences time the # of 3-volt differences
    f = open("data.txt", "r")
    nums = [0]
    answer = [1]

    def is_bound(num, min_num):
        # check if a number is within 3 inclusive.
        return num + 3 >= min_num

    for line in f:
        nums.append(int(line.strip('\n')))

    nums.sort()
    nums.append(nums[-1]+3)

    for idx in range(1, len(nums)):
        sub_count = 0
        for idx_left in range(max(0, idx-3), idx):
            if is_bound(nums[idx_left], nums[idx]):
                sub_count += answer[idx_left]
        answer.append(sub_count)

    print(answer[-1])


if __name__ == "__main__":
    main()
