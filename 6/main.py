#!/usr/bin/env python3

with open("input.txt", "r") as f:
    indata = f.read()

# with open("test_input.txt", "r") as f:
#     indata = f.read()

first_answer_groups = [
    "".join(set(ans.replace("\n", ""))) for ans in indata.split("\n\n")
]
first_answer_scores = [len(s) for s in first_answer_groups]


second_answer_groups = [ans.strip().split("\n") for ans in indata.split("\n\n")]
second_answer_scores = []
for answer_group in second_answer_groups:
    ag_score = 0
    if len(answer_group) == 1:
        ag_score += len(set(answer_group[0]))
    else:
        seen = []
        for ans in answer_group:
            seen += list(set(ans))
        for c in list(set(seen)):
            if seen.count(c) == len(answer_group):
                ag_score += 1
    second_answer_scores.append(ag_score)


print(sum(first_answer_scores))
print(sum(second_answer_scores))
