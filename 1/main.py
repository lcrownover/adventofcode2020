#!/usr/bin/env python3

def answer1(input_file):
    with open(input_file, 'r') as f:
        expenses = [int(e.strip()) for e in f.readlines()]

    for i in expenses:
        for j in expenses:
            if (i + j) == 2020:
                return i*j

def answer2(input_file):
    with open(input_file, 'r') as f:
        expenses = [int(e.strip()) for e in f.readlines()]

    for i in expenses:
        for j in expenses:
            for k in expenses:
                if (i + j + k) == 2020:
                    return i*j*k

print(answer1('input.txt'))
print(answer2('input.txt'))
