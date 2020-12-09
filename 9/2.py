# innum = "2_test_input.txt"
# infile = "test_input.txt"
innum = "2_input.txt"
infile = "input.txt"

with open(innum, "r") as f:
    target_number = int(f.read().strip())
with open(infile, "r") as f:
    indata = [int(n.strip()) for n in f.readlines()]


head = 0
tail = head + 1
while True:
    head_num = indata[head]
    tail_num = indata[tail]
    working_sum = sum(indata[head:tail])
    if working_sum == target_number:
        break
    if working_sum > target_number:
        head += 1
        tail = head + 1
        continue
    tail += 1

target_range = indata[head:tail]
small, high = sorted(target_range)[0], sorted(target_range)[-1]
encryption_weakness = small + high
print(encryption_weakness)
