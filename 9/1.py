# infile = "test_input.txt"
infile = "input.txt"

with open(infile, "r") as f:
    indata = [int(n.strip()) for n in f.readlines()]

PRE_LEN = 25
if "test" in infile:
    PRE_LEN = 5


valid = 0
while True:
    pre = indata[valid : PRE_LEN + valid]
    data_num = indata[valid + PRE_LEN]
    print(f"looking for nums for: {data_num}")
    check = False
    for i in pre:
        for j in pre:
            if i + j == data_num:
                print(f"found combo: {i} + {j}")
                check = True
                valid += 1
    if not check:
        print(data_num)
        break
