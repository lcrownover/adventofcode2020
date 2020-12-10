infile = "input.txt"

with open(infile, "r") as f:
    indata = [int(n.strip()) for n in f.readlines()]


def diff(x, y):
    # return the abs difference between x and y
    return abs(x - y)


# first we sort them low to high
nums = list(sorted(indata))

# charging port is 0 jolts
nums.insert(0, 0)

# end is always 3 higher than last
nums.append(nums[-1] + 3)

valid = [nums]
for nums in valid:
    print(f"{len(valid)}", end="\r")
    for i, n in enumerate(nums):
        if (i == 0) or (i == (len(nums) - 1)):  # dont run this on the first or last num
            continue
        if (diff(n, nums[i - 1]) + diff(n, nums[i + 1])) <= 3:
            new = [x for x in nums]
            new.remove(n)
            if new not in valid:
                valid.append(new)


print(len(valid))
