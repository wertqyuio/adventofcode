def main():
    # TO-DO: Write a function that takes in numbers, and returns
    # the first number that is not a sum of exactly 2 of previous
    # preamble numbers.
    # Part 2: Identifying the number and then identifying a range
    # s.t. summing over all the numbers in range eqauls the number.
    f = open("data.txt", "r")
    nums = []
    cum_nums = []

    for line in f:
        nums.append(int(line.strip('\n')))
        if not len(cum_nums):
            cum_nums = [0]
        else:
            cum_nums.append(cum_nums[-1]+nums[-1])

    def process_nums(preamble=25):
        current = []
        while len(current) < preamble:
            current.append(nums[len(current)])
        idx = len(current)
        while idx < len(nums):
            is_valid = False
            for idx_one in range(len(current)-1):
                for idx_two in range(len(current)):
                    if current[idx_one] + current[idx_two] == nums[idx]:
                        is_valid = True
                        break
            if not is_valid:
                return (nums[idx])
            else:
                current[idx % preamble] = nums[idx]
            idx += 1

    num_breaker = process_nums()
    sum_to_num_breaker = 0
    idx_left = 0
    idx_right = 1
    while sum_to_num_breaker != num_breaker:
        sum_to_num_breaker = cum_nums[idx_right] - cum_nums[idx_left]
        if sum_to_num_breaker < num_breaker:
            idx_right += 1
        elif sum_to_num_breaker > num_breaker:
            idx_left += 1
    narrow_range = nums[idx_left+1:idx_right+1]
    narrow_range.sort()
    print(narrow_range[0]+narrow_range[-1])

if __name__ == "__main__":
    main()
