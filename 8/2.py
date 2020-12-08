import pathlib

infile = pathlib.Path(__file__).with_name("input.txt")

with open(infile, "r") as f:
    original_instructions = [line.strip() for line in f.readlines()]


def parse_instruction(instruction):
    return instruction.split(" ")[0], int(instruction.split(" ")[1])


def format_instruction(op, n):
    if n >= 0:
        n = f"+{n}"
    return f"{op} {n}"


def next_jn(jmps_and_nops, jn_head):
    # returns the next element of jmps_and_nops
    if jn_head == None:
        return jmps_and_nops[0]
    return jmps_and_nops[jmps_and_nops.index(jn_head) + 1]


def next_instructions(instructions, inst_index):
    # return a new instruction list
    # with the element at inst_index flipped between nop and jmp
    new_instructions = [i for i in instructions]
    old_inst = instructions[inst_index]
    op, n = parse_instruction(old_inst)
    if op == "nop":
        new_instructions[inst_index] = format_instruction("jmp", n)
    if op == "jmp":
        new_instructions[inst_index] = format_instruction("nop", n)
    return new_instructions


instructions = [i for i in original_instructions]
head = 0
acc = 0
seen = []


# gets a list of all the indexes of instructions that are "jmp" or "nop"
jmps_and_nops = []
for i, inst in enumerate(original_instructions):
    op, n = parse_instruction(inst)
    if op in ["jmp", "nop"]:
        jmps_and_nops.append(i)
# using jn_head, we can iterate through the list of jmps and nops and change the next occurrence
# until the program completes successfully
# we start with None, because we start by assuming the original instructions work
jn_head = None


while True:
    if head in seen:
        # oops, we're repeating now, let's reset everything
        # and set jn_head to the index of the next element of our jmps and nops list
        jn_head = next_jn(jmps_and_nops, jn_head)
        head = 0
        acc = 0
        seen = []
        instructions = next_instructions(original_instructions, jn_head)

    line = instructions[head]
    op, n = parse_instruction(line)

    # print(f"|{line}|  head:{head} acc:{acc} jn_head:{jn_head} seen:{seen}")

    seen.append(head)

    if op == "nop":
        head += 1
    if op == "acc":
        acc += n
        head += 1
    if op == "jmp":
        head += n

    if head == len(instructions):
        # win condition!
        print(acc)
        break

    # input()
