import cProfile

infile = "test_input2.txt"

with open(infile, "r") as f:
    indata = [int(n.strip()) for n in f.readlines()]


# first we sort them low to high
nums = list(sorted(indata))

# charging port is 0 jolts
nums.insert(0, 0)

# end is always 3 higher than last
nums.append(nums[-1] + 3)


def ans(nums):
    valid = [nums]
    for nums in valid:
        # print(f"{len(valid)}", end="\r")
        for i, n in enumerate(nums):
            try:
                if 0 <= (nums[i + 1] - nums[i - 1]) <= 3:
                    l = list(nums)
                    del l[i]
                    if l not in valid:
                        valid.append(l)
            except IndexError:
                pass
    return len(valid)


# print(ans(nums))

cProfile.run("print(ans(nums))")
