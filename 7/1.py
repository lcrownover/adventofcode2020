#!/usr/bin/env python3

import re

# with open("test_input.txt", "r") as f:
#     rules = [line.strip() for line in f.readlines() if line.strip() != ""]

with open("input.txt", "r") as f:
    rules = [line.strip() for line in f.readlines() if line.strip() != ""]

# sample rule:
#'light red bags contain 1 bright whte bag, 2 muted yellow bags.
# sample dataform:
# {'light red': ['bright white', 'muted yellow', 'muted yellow']}

parsed_rules = []

# parse the rules
for rule in rules:
    key = re.match(r"^([\w ]+) bags contain", rule).group(1)
    parsed_rule = {}
    parsed_bags = []
    parsed_rule[key] = parsed_bags

    bags_string = re.match(r".*?contain (.*)", rule).group(1)
    if bags_string == "no other bags.":
        parsed_rules.append(parsed_rule)
        continue
    for bag_string in bags_string.split(","):
        bag_string = bag_string.strip()
        m = re.match(r"(\d) ([\w ]+)bag", bag_string)
        n = int(m[1].strip())
        b = m[2].strip()
        for i in range(0, n):
            parsed_bags.append(b)
    parsed_rules.append(parsed_rule)

# print(parsed_rules)

my_bag = "shiny gold"

good_bags = []
tracker = []
for rule in parsed_rules:
    for k, v in rule.items():
        if my_bag in v:
            good_bags.append(k)
            tracker.append(k)
while tracker:
    for bag in tracker:
        for rule in parsed_rules:
            for k, v in rule.items():
                if bag in v:
                    good_bags.append(k)
                    tracker.append(k)
        tracker.remove(bag)

verified_good_bags = list(set(good_bags))

print(len(verified_good_bags))
