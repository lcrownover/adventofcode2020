with open("input.txt", "r") as f:
    instructions = [line.strip() for line in f.readlines()]


head = 0
acc = 0
seen = []

while True:
    if head in seen:
        print(acc)
        break
    line = instructions[head]
    op, n = line.split(" ")[0], int(line.split(" ")[1])
    if op == "nop":
        seen.append(head)
        head += 1
    if op == "acc":
        seen.append(head)
        acc += n
        head += 1
    if op == "jmp":
        seen.append(head)
        head += n
