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

diffs = []
for i, n in enumerate(nums):
    if i == (len(nums) - 1):
        # at the end, so dont diff and just add 3
        diffs.append(3)
        continue
    diffs.append(diff(n, nums[i + 1]))

ones = diffs.count(1)
threes = diffs.count(3)

ans = ones * threes
print(ans)
