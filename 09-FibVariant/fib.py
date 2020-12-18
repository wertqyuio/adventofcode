def main():
    # TO-DO: Write a function that processes numbers :D
    # Later- write everything as a Fibonacci number basically
    f = open("data.txt", "r")
    nums = []

    for line in f:
        nums.append(int(line.strip('\n')))

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

    print(process_nums())


if __name__ == "__main__":
    main()
