#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    entries = [line.strip() for line in f.readlines()]

def input_parser(entry):
    r,l,p = entry.split(' ')
    l = l.strip(':')
    r1 = int(r.split('-')[0])
    r2 = int(r.split('-')[1])
    return r1, r2, l, p


def answer1(entries):
    correct = 0
    for entry in entries:
        r1,r2,l,pw = input_parser(entry)
        if pw.count(l) >= int(r1) and pw.count(l) <= int(r2):
            correct += 1
    return correct

def answer2(entries):
    correct = 0
    for entry in entries:
        r1,r2,l,pw = input_parser(entry)
        c1 = pw[r1-1]
        c2 = pw[r2-1]
        if bool(c1 == l) ^ bool(c2 == l):
            correct += 1
    return correct

print(answer1(entries))
print(answer2(entries))
